import re

path = '/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/expresswater-v7-final/index.html'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i in range(len(lines)):
    line = lines[i]
    stripped = line.strip()
    
    # If this line is just a closing brace (end of a language block)
    # AND the next non-empty line starts with a language key like "th: {"
    if stripped == "}":
        # Look ahead for next non-empty line
        next_line = None
        for j in range(i + 1, len(lines)):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
        
        if next_line and re.match(r'^[a-z]{2,3}:\s*\{', next_line):
            # Add a comma to the brace line
            line = line.replace("}", "},")
    
    new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fix applied via line iteration.")
