
import os
from PIL import Image

ASSETS_DIR = "/Users/emrxh/Documents/Bricks/assets/sets"

def standardize():
    for filename in os.listdir(ASSETS_DIR):
        if filename.startswith('.'): continue
        
        # Only target back/side images to avoid messing with original front images if possible
        # (Though consistency would be nice, let's stick to what we need for the modal logic)
        if '_back' in filename or '_side' in filename:
            name, ext = os.path.splitext(filename)
            if ext.lower() != '.png':
                print(f"Converting {filename} to .png")
                try:
                    filepath = os.path.join(ASSETS_DIR, filename)
                    img = Image.open(filepath)
                    new_filepath = os.path.join(ASSETS_DIR, name + ".png")
                    img.save(new_filepath)
                    # Remove old file
                    os.remove(filepath)
                except Exception as e:
                    print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    standardize()
