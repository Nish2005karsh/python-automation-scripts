import os
import shutil
from pathlib import Path
# Set your desktop path
desktop = Path.home() / "Desktop"
# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Zips": [".zip", ".rar"],
    "Code": [".py", ".js", ".html"],
    "Videos": [".mp4", ".mov"],
    "Others": []
}

def organize():
    for file in desktop.iterdir():
        if file.is_file():
            moved = False
            for folder, extensions in categories.items():
                if file.suffix.lower() in extensions:
                    move_file(file, desktop / folder)
                    moved = True
                    break
            if not moved:
                move_file(file, desktop / "Others")

def move_file(file, destination):
    destination.mkdir(exist_ok=True)
    shutil.move(str(file), str(destination / file.name))
    print(f"Moved: {file.name} → {destination}")

if __name__ == "__main__":
    organize()
