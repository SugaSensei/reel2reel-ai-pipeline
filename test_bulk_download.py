from downloader import bulk_download_reels

shortcodes = ['DKEjzAShOTL', 'DJ_RHI3hri7', 'DJ66U3ZBk8r', 'DJ086tyh5Yc', 'DJytd4UhGgx', 'DJlOiPaBurB', 'DJd1irGBiNI', 'DJWG4_pBoXC', 'DJJbRoEBtUD', 'DJBtdm6hYOg', 'DI8lb5IBW0o', 'DI5zbAihUJ3', 'DI3Hl7XBx6x', 'DIsq9ZOBhPg', 'DIp8xiziQNt', 'DInuoC2hxdX', 'DIk-IcZhoMH', 'DIiOBLGheD2', 'DIfzSiehuVj', 'DIdXJasConI', 'DIaxsvDNBLc', 'DIYXRklBHL4', 'DIVx1V_NQ0H', 'DITgN0mh3LV']

results = bulk_download_reels(shortcodes)

print("\nDownload Summary:")
for code, path in results.items():
    if path:
        print(f"{code}: Downloaded to {path}")
    else:
        print(f"{code}: Failed to download")
