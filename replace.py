import os

folder = 'my_project'
for file in os.listdir(folder):
    if file.endswith('.txt'):
        path = os.path.join(folder, file)
        with open(path, 'r+') as f:
            content = f.read().replace("OLD_TEXT", "NEW_TEXT")
            f.seek(0)
            f.write(content)
            f.truncate()
