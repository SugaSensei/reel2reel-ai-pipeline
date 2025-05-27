from downloader import bulk_download_reels

shortcodes = [
    "C5yW9A3PqJ9",
    "C5xXQHwpq1Z",
    "C5zC3pQjF4R",
    # Add your shortcodes here manually
]

results = bulk_download_reels(shortcodes)

print("\nDownload Summary:")
for code, path in results.items():
    if path:
        print(f"{code}: Downloaded to {path}")
    else:
        print(f"{code}: Failed to download")
