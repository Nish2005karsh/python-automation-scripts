note = input("What’s on your mind? ")

with open("notes.md", "a") as f:
    f.write(f"- {note}\n")
print("Note saved!")