
import os
import shutil
import difflib

ASSETS_DIR = "/Users/emrxh/Documents/Bricks/assets/sets"
SOURCE_DIR = "/Users/emrxh/Documents/Bricks/back and front"

# Manual mapping for tricky ones
MANUAL_MAP = {
    "its a boy": "Gender Reveal",
    "the window break": "The tunnel",
    "ice": "ICE",
    "top g": "TOP G",
    "blacked": "Blacked",
    "chillhouse": "Chillhouse",
    "deathnote": "Deathnote",
    "doakes": "Doakes",
    "freakoff": "Freak Off",
    "i cant breate": "I Cant Breathe",
    "i cant breathe": "I Cant Breathe",
    "migrants": "Migrants",
    "monke": "Monke",
    "pablo": "Pablo",
    "pride": "Pride",
    "striped pyjamas": "Striped Pyjamas",
    "the crashout": "The Crashout",
    "the cybertruck": "The Cybertruck",
    "cybertruck": "The Cybertruck",
    "the deep dive": "The Deep Dive",
    "the drive": "The Drive",
    "the glove": "The Glove",
    "the ice wall": "The Ice Wall",
    "the mask": "The Mask",
    "the slap": "The Slap",
    "the turning point": "THE TURNING POINT",
    "tmt": "TMT Set",
    "tiger king": "Tiger King",
    "tokabu": "Tokabu",
    "wif": "wif",
    "alcatraz": "Alcatraz",
    "clinton": "Clinton Set",
    "db cooper": "DB Cooper",
    "dexter": "Dexter",
    "jfk": "JFK",
    "meth lab": "Meth Lab",
    "the island": "The island", # Note lowercase 'i' in destination
    "the list": "The list",
    "the beef": "The_Beef" # Destination uses underscore? Checking list... actually "The_Beef.png" exists.
}

def get_canonical_sets():
    sets = {}
    for f in os.listdir(ASSETS_DIR):
        if f.startswith('.'): continue
        name_no_ext = os.path.splitext(f)[0]
        sets[name_no_ext.lower().replace("_", " ")] = name_no_ext
    return sets

def migrate():
    canonical_sets_map = get_canonical_sets()
    # Update MANUAL_MAP with canonical names from file system for better accuracy
    # Actually, let's just use the canonical names we found
    
    # We strictly want to target the filenames we saw in the source directory
    source_files = [f for f in os.listdir(SOURCE_DIR) if not f.startswith('.')]
    
    print(f"Found {len(source_files)} files in source.")

    for filename in source_files:
        lower_name = filename.lower()
        
        # Determine strict type
        is_back = 'back' in lower_name
        is_side = 'side' in lower_name
        
        if not is_back and not is_side:
            print(f"Skipping {filename}: Not back or side")
            continue
            
        view_type = 'back' if is_back else 'side'
        
        # Clean up name to find key
        # Remove extension
        name_part = os.path.splitext(lower_name)[0]
        # Remove 'back', 'side', numbers, extra chars
        clean_name = name_part.replace('back', '').replace('side', '').replace('_', ' ').replace('-', ' ').strip()
        
        # Try to find target set
        target_set_name = None
        
        # 1. Check Manual Map
        if clean_name in MANUAL_MAP:
             # Verify this exists in canonical map (or close enough)
             mapped_name = MANUAL_MAP[clean_name]
             # Check if mapped_name is actually a real file base name
             # We need to find the exact filename in assets dir to match casing/spelling
             
             # Search for mapped_name in canonical_sets_map values
             for real_name in canonical_sets_map.values():
                 if real_name == mapped_name:
                     target_set_name = real_name
                     break
                 # Handle "The_Beef" vs "The Beef"
                 if real_name.replace('_', ' ') == mapped_name.replace('_', ' '):
                      target_set_name = real_name
                      break

        
        # 2. Fuzzy match against canonical sets if not found
        if not target_set_name:
             # exact match check first
             if clean_name in canonical_sets_map:
                 target_set_name = canonical_sets_map[clean_name]
             else:
                 # fuzzy?
                 matches = difflib.get_close_matches(clean_name, canonical_sets_map.keys(), n=1, cutoff=0.8)
                 if matches:
                     target_set_name = canonical_sets_map[matches[0]]
        
        if target_set_name:
            # Construct new filename
            # Use original extension? Or standardize to png?
            # User's files are mixed jpg/png. Browsers handle it, but consistency is nice.
            # Let's keep original extension to avoid conversion issues, just rename.
            ext = os.path.splitext(filename)[1]
            new_filename = f"{target_set_name}_{view_type}{ext}"
            
            src_path = os.path.join(SOURCE_DIR, filename)
            dst_path = os.path.join(ASSETS_DIR, new_filename)
            
            print(f"Moving {filename} -> {new_filename}")
            try:
                shutil.move(src_path, dst_path)
            except Exception as e:
                print(f"Error moving {filename}: {e}")
        else:
            print(f"Could not map {filename} (Clean: '{clean_name}')")

if __name__ == "__main__":
    migrate()
