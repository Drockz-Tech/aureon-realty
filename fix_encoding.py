import sys

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replacements
    content = content.replace("Â·", "·")
    content = content.replace("â€”", "—")
    content = content.replace("â€“", "–")
    content = content.replace("Â", "") # Clean up any stray Â
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Fixed encodings successfully!")

if __name__ == "__main__":
    fix_file("index.html")
