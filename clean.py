import os
import shutil
downloads = "C:/Users/YourName/Downloads"

for file in os.listdir(downloads):
    if file.endswith(".zip"):
        shutil.move(f"{downloads}/{file}", f"{downloads}/Zips/{file}")
