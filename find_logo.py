import os

file_path = 'expresswater_source.html'
search_str = '雨晨三溢'

if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        idx = content.find(search_str)
        if idx != -1:
            print(content[max(0, idx-100):idx+100])
        else:
            print("Not found")
else:
    print("File not found")
