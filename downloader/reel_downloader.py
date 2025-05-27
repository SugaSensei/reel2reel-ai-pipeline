import os
import instaloader
from .utils import get_latest_file

def download_reel(shortcode: str, output_dir: str = "assets/input_reels") -> str:
    os.makedirs(output_dir, exist_ok=True)
    loader = instaloader.Instaloader(dirname_pattern=output_dir, save_metadata=False, post_metadata_txt_pattern='')

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        print(f"🔽 Downloading Reel: {shortcode}")
        loader.download_post(post, target="reel")
        print("✅ Download complete.")
    except Exception as e:
        print(f"❌ Failed to download reel {shortcode}: {e}")
        return ""
    return get_latest_file(output_dir)

def bulk_download_reels(shortcodes, output_dir="assets/input_reels"):
    results = {}
    for code in shortcodes:
        print(f"Starting download for: {code}")
        path = download_reel(code, output_dir)
        results[code] = path
    return results
