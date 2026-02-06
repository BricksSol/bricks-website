import os
import json
import re

# Get list of files
assets_dir = 'Sets/Web/assets/minifigures'
files = sorted([f for f in os.listdir(assets_dir) if not f.startswith('.')])

# Read script.js
script_path = 'Sets/Web/script.js'
with open(script_path, 'r') as f:
    content = f.read()

# Create new array string
new_array = 'const minifigures = ' + json.dumps(files, indent=4) + ';'

# Replace existing array using regex
# Matches "const minifigures = [ ... ];" spanning multiple lines
pattern = r'const minifigures = \[.*?\];'
# We use DOTALL to let . match newlines
new_content = re.sub(pattern, new_array, content, flags=re.DOTALL)

# Write back
with open(script_path, 'w') as f:
    f.write(new_content)

print(f"Updated script.js with {len(files)} files.")
