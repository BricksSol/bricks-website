
import os
import subprocess

ASSETS_DIR = "/Users/emrxh/Documents/Bricks/assets/sets"

def standardize():
    for filename in os.listdir(ASSETS_DIR):
        if filename.startswith('.'): continue
        
        if '_back' in filename or '_side' in filename:
            name, ext = os.path.splitext(filename)
            if ext.lower() != '.png':
                print(f"Converting {filename} to .png using sips")
                filepath = os.path.join(ASSETS_DIR, filename)
                new_filepath = os.path.join(ASSETS_DIR, name + ".png")
                
                try:
                    subprocess.run(["sips", "-s", "format", "png", filepath, "--out", new_filepath], check=True)
                    # Remove old file
                    os.remove(filepath)
                except Exception as e:
                    print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    standardize()
