
from pathlib import Path
import random
import shutil

PROJECT_DIR = Path(__file__).resolve().parent.parent

SOURCE_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

CLASSES = ["ulcer", "non_ulcer"]
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

random.seed(42)

for class_name in CLASSES:
    source_folder = SOURCE_DIR / class_name

    if not source_folder.exists():
        raise FileNotFoundError(f"Folder not found: {source_folder}")

    images = [
        file for file in source_folder.rglob("*")
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    ]

    random.shuffle(images)

    total = len(images)
    train_end = int(total * 0.70)
    val_end = train_end + int(total * 0.15)

    splits = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split_name, split_images in splits.items():
        destination = OUTPUT_DIR / split_name / class_name
        destination.mkdir(parents=True, exist_ok=True)

        for

