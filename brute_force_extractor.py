import re
import json

log_path = "/Users/jet/.accio/accounts/1661502182/subagent-sessions/agent_agent_DID-F456DA-2B0D4C_main_cid_CID-78502182U1776649-9D67C1-1120-846940_sub_browser_81e15a6d.messages.jsonl"
with open(log_path, 'r') as f:
    raw_data = f.read()

# Find all occurrences of [Result] and the following JSON block
# We look for [Result] followed by escaped or non-escaped curly braces
matches = re.findall(r'\[Result\]\\n(.*?)(?=\\n"|")', raw_data, re.DOTALL)

products = []
seen_names = set()

for m in matches:
    # Unescape the match
    clean_json = m.replace('\\\\n', '\n').replace('\\n', '\n').replace('\\"', '"').replace('\\\\"', '"')
    try:
        # Try to find the valid JSON object within the junk
        start = clean_json.find('{')
        end = clean_json.rfind('}') + 1
        if start != -1 and end != -1:
            data = json.loads(clean_json[start:end])
            name = data.get('productName')
            if name and name not in seen_names:
                products.append(data)
                seen_names.add(name)
    except:
        continue

print(f"Total Products Recovered: {len(products)}")
with open('/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/RECOVERED_187.json', 'w') as f:
    json.dump(products, f, indent=2)
