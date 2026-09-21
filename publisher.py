"""Instagram Graph API publisher (photo + reels) with dry-run mode.

Needs env vars (only for real posting):
  IG_USER_ID, IG_ACCESS_TOKEN  -> from developers.facebook.com (see SETUP_HINDI.md)
  CLOUDINARY_URL              -> free image/video hosting, gives public URLs for IG API

Without these, runs in DRY-RUN mode (prints what WOULD be posted).
"""
import os
import sys
import time

import requests

GRAPH = "https://graph.facebook.com/v21.0"


def have_creds():
    return bool(os.environ.get("IG_USER_ID") and os.environ.get("IG_ACCESS_TOKEN"))


def upload_cloudinary(path, resource_type="image"):
    """Upload file, return public secure_url. Needs CLOUDINARY_URL env."""
    try:
        import cloudinary
        import cloudinary.uploader
    except ImportError:
        raise RuntimeError("cloudinary package missing. pip install cloudinary")
    if not os.environ.get("CLOUDINARY_URL"):
        raise RuntimeError("CLOUDINARY_URL env var missing (free signup: cloudinary.com)")
    cloudinary.config()  # reads CLOUDINARY_URL automatically
    res = cloudinary.uploader.upload(path, resource_type=resource_type,
                                     folder="shabnal-auto")
    return res["secure_url"]


def publish_photo(ig_id, token, image_url, caption):
    # 1. create container
    r = requests.post(f"{GRAPH}/{ig_id}/media", data={
        "image_url": image_url, "caption": caption, "access_token": token}, timeout=60)
    r.raise_for_status()
    creation_id = r.json()["id"]
    # 2. publish
    r = requests.post(f"{GRAPH}/{ig_id}/media_publish", data={
        "creation_id": creation_id, "access_token": token}, timeout=60)
    r.raise_for_status()
    return r.json().get("id")


def publish_reel(ig_id, token, video_url, caption):
    r = requests.post(f"{GRAPH}/{ig_id}/media", data={
        "media_type": "REELS", "video_url": video_url, "caption": caption,
        "access_token": token}, timeout=60)
    r.raise_for_status()
    creation_id = r.json()["id"]
    # wait until Meta finishes processing (up to ~3 min)
    for _ in range(36):
        time.sleep(5)
        s = requests.get(f"{GRAPH}/{creation_id}", params={
            "fields": "status_code", "access_token": token}, timeout=30).json()
        code = s.get("status_code")
        if code == "FINISHED":
            break
        if code == "ERROR":
            raise RuntimeError(f"Reel processing failed: {s}")
    else:
        raise RuntimeError("Reel processing timed out.")
    r = requests.post(f"{GRAPH}/{ig_id}/media_publish", data={
        "creation_id": creation_id, "access_token": token}, timeout=60)
    r.raise_for_status()
    return r.json().get("id")


def post_day(photo_path, reel_path, post_caption, reel_caption, dry_run=True):
    ig_id = os.environ.get("IG_USER_ID")
    token = os.environ.get("IG_ACCESS_TOKEN")
    if dry_run or not have_creds():
        print("[DRY-RUN] Would post:")
        print(f"  PHOTO: {photo_path} ({len(post_caption)} chars caption)")
        print(f"  REEL : {reel_path} ({len(reel_caption)} chars caption)")
        if not have_creds():
            print("  (IG_USER_ID / IG_ACCESS_TOKEN not set - see SETUP_HINDI.md for auto-post setup)")
        return {"photo": None, "reel": None}

    print("Uploading photo to Cloudinary...")
    photo_url = upload_cloudinary(photo_path, "image")
    print("Publishing photo to Instagram...")
    pid = publish_photo(ig_id, token, photo_url, post_caption)
    print(f"  Photo posted! media id={pid}")

    print("Uploading reel to Cloudinary...")
    reel_url = upload_cloudinary(reel_path, "video")
    print("Publishing reel to Instagram...")
    rid = publish_reel(ig_id, token, reel_url, reel_caption)
    print(f"  Reel posted! media id={rid}")
    return {"photo": pid, "reel": rid}


if __name__ == "__main__":
    # quick CLI: python publisher.py <photo> <reel> <post_caption_file> <reel_caption_file> [--post]
    args = sys.argv[1:]
    dry = "--post" not in args
    photo, reel, cap_p, cap_r = args[0], args[1], args[2], args[3]
    post_day(photo, reel, open(cap_p, encoding="utf-8").read(),
             open(cap_r, encoding="utf-8").read(), dry_run=dry)
