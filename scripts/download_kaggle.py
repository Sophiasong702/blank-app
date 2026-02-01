import kagglehub
from pathlib import Path
import shutil

# Download latest version
download_dir = Path(kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset"))
print("Downloaded to:", download_dir)

# Find CSVs
csvs = list(download_dir.rglob("*.csv"))
print("Found CSVs:", [c.name for c in csvs])

# Pick the main one (if multiple, you'll choose one)
target_dir = Path("data/raw")
target_dir.mkdir(parents=True, exist_ok=True)

# If there is only one CSV, copy it automatically
if len(csvs) == 1:
    dst = target_dir / csvs[0].name
    shutil.copy2(csvs[0], dst)
    print("Copied to:", dst)
else:
    print("Multiple CSVs found. Copy the one you want into data/raw/.")
