import os
import re

i18n_dir = 'expresswater_v26_04_26_1700/assets/i18n'
files = [f for f in os.listdir(i18n_dir) if f.endswith('.json')]

for f_name in files:
    path = os.path.join(i18n_dir, f_name)
    with open(path, 'r') as f:
        content = f.read()
    
    # Simple unescape: \" -> " and \\\" -> \"
    # But wait, if it's double escaped, we might have more.
    # Looking at the sample: \"ui\":
    # That should be "ui":
    # And <a href=\\\"mailto:info@...\\\">
    # That should be <a href=\"mailto:info@...\">
    
    fixed = content.replace('\\"', '"').replace('\\\\"', '\\"')
    
    # If it was wrapped in quotes itself (like a stringified JSON), 
    # we might need to remove start/end quotes.
    if fixed.startswith('"') and fixed.endswith('"'):
        fixed = fixed[1:-1]
        # Re-fix internal escapes if it was stringified
        fixed = fixed.replace('\\"', '"').replace('\\\\', '\\')

    try:
        import json
        json.loads(fixed)
        with open(path, 'w') as f:
            f.write(fixed)
        print(f"Fixed {f_name}")
    except Exception as e:
        print(f"Failed to fix {f_name}: {e}")
