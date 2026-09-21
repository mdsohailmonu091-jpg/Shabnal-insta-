"""Daily engine: pick today's content -> build post + reel -> save (or auto-post).

Usage:
  python daily.py                  # draft mode: files saved to outbox/YYYY-MM-DD/
  python daily.py --post           # also auto-post if IG creds present
  python daily.py --date 2026-11-08
"""
import argparse
import datetime as dt
import os

from common import OUTBOX
from content_bank import POSTS, REELS, FESTIVALS, HASHTAG_SETS, WEEKEND_LINE, START_DATE
from designer import build_post
from reel_maker import build_reel

try:
    from ai_writer import rewrite_caption
except Exception:
    def rewrite_caption(*a, **k):
        return None


def read_trend():
    """Weekly trending audio/topic from trends.txt (user-editable)."""
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trends.txt")
    try:
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                return line
    except FileNotFoundError:
        pass
    return None


def pick_content(day):
    key = day.strftime("%Y-%m-%d")
    if key in FESTIVALS:
        f = FESTIVALS[key]
        return f["post"], f["reel"], f"Festival: {f['name']}"
    start = dt.date.fromisoformat(START_DATE)
    idx = (day - start).days % len(POSTS)
    return POSTS[idx], REELS[idx], f"Day {idx + 1}/30 rotation"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--post", action="store_true", help="auto-post if creds present")
    args = ap.parse_args()

    day = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    post, reel, source = pick_content(day)
    start = dt.date.fromisoformat(START_DATE)
    htag = HASHTAG_SETS[(day - start).days % len(HASHTAG_SETS)]

    post_cap = post["caption"]
    reel_cap = reel["caption"]
    if day.weekday() >= 5:  # Sat-Sun
        post_cap += WEEKEND_LINE

    # optional AI freshening (silent fallback to bank text)
    ai_p = rewrite_caption(post_cap, f"Feed post: {post['hook']}")
    if ai_p:
        post_cap = ai_p
    ai_r = rewrite_caption(reel_cap, f"Reel: {reel['title']}")
    if ai_r:
        reel_cap = ai_r

    post_cap_full = post_cap + "\n\n.\n.\n" + htag
    trend = read_trend()
    reel_cap_full = reel_cap + "\n\n" + htag
    if trend:
        reel_cap_full += f"\n\n🎵 Is hafte ka trend: {trend}"

    folder = os.path.join(OUTBOX, day.strftime("%Y-%m-%d"))
    os.makedirs(folder, exist_ok=True)
    photo_path = os.path.join(folder, "post_4x5.jpg")
    reel_path = os.path.join(folder, "reel_9x16.mp4")

    print(f"Date: {day} | {source}")
    print("Building post image...")
    build_post(post["product"], post["hook"], post["sub"], out_path=photo_path)
    print("Building reel video...")
    build_reel(reel["scenes"], reel_path)
    with open(os.path.join(folder, "caption.txt"), "w", encoding="utf-8") as f:
        f.write(post_cap_full)
    with open(os.path.join(folder, "reel_caption.txt"), "w", encoding="utf-8") as f:
        f.write(f"[Audio tip: {reel.get('audio', '')}]\n\n" + reel_cap_full)
    print(f"Saved to {folder}/")

    from publisher import post_day
    post_day(photo_path, reel_path, post_cap_full, reel_cap_full,
             dry_run=not args.post)


if __name__ == "__main__":
    main()
