import re

file_path = 'expresswater-v7-final/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = 'languages: {'
start_index = content.find(start_marker)
if start_index == -1:
    print("Marker not found")
    exit(1)

# Start counting from the '{' after 'languages: '
current_index = start_index + len('languages: ') - 1 # at '{'
brace_count = 0
end_index = -1

for i in range(current_index, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end_index = i + 1
            break

if end_index != -1:
    extracted = content[current_index:end_index]
    print(f"Extracted length: {len(extracted)}")
    with open('debug_langs.json', 'w', encoding='utf-8') as f:
        f.write(extracted)
else:
    print("End index not found")
