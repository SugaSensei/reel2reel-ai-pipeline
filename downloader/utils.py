import os

def get_latest_file(directory: str) -> str:
    files = [os.path.join(directory, f) for f in os.listdir(directory)]
    files = [f for f in files if os.path.isfile(f)]
    if not files:
        return ""
    return max(files, key=os.path.getmtime)
