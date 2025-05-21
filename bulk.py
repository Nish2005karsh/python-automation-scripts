import os
for count, filename in enumerate(os.listdir("my_folder")):
    dst = f"file_{count}.txt"
    os.rename(f"my_folder/{filename}", f"my_folder/{dst}")
