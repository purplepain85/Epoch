"""
Extract in-scope assets from an Immunefi program page.
The full asset list is embedded in the page as escaped JSON in a
Next.js flight payload, under the key "assets".
"""
import json, re, sys, urllib.request
from pathlib import Path

OUT_DIR = Path.home() / "epoch" / "data" / "scopes"
ADDR_RE = re.compile(r'0x[a-fA-F0-9]{40}')


def fetch(slug):
    url = f"https://immunefi.com/bug-bounty/{slug}/"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def extract_assets(html):
    """Find the 'assets':[...] array in the embedded flight payload."""
    marker = '\\"assets\\":'
    idx = html.find(marker)
    if idx < 0:
        return []
    # start of the array
    start = html.find('[', idx)
    if start < 0:
        return []

    # walk forward to matching close bracket, respecting string state
    depth = 0
    in_str = False
    esc = False
    end = start
    for i in range(start, len(html)):
        c = html[i]
        if esc:
            esc = False
            continue
        if c == '\\':
            esc = True
            continue
        if c == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                end = i
                break

    raw = html[start:end + 1]
    # unescape the payload: \" -> ", \u003c -> <, etc.
    unescaped = raw.encode("utf-8").decode("unicode_escape")
    try:
        return json.loads(unescaped)
    except Exception as e:
        print(f"json parse failed: {e}")
        print("first 500 chars:")
        print(unescaped[:500])
        return []


def main():
    slug = sys.argv[1] if len(sys.argv) > 1 else "thegraph"
    print(f"fetching scope for: {slug}")
    html = fetch(slug)
    print(f"page size: {len(html)} bytes")
    assets = extract_assets(html)
    print(f"extracted {len(assets)} assets")

    # enrich: pull address out of url
    for a in assets:
        m = ADDR_RE.search(a.get("url", ""))
        a["address"] = m.group(0).lower() if m else None

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{slug}.json"
    out.write_text(json.dumps({"slug": slug, "assets": assets}, indent=2))
    print(f"wrote {out}")
    print()
    print(f"{'address':<44} {'type':<14} description")
    print("-" * 110)
    for a in assets:
        print(f"{(a.get('address') or ''):<44} {(a.get('type') or ''):<14} {(a.get('description') or '')[:60]}")


if __name__ == "__main__":
    main()
