import json
import re

log_path = "/Users/jet/.accio/accounts/1661502182/subagent-sessions/agent_agent_DID-F456DA-2B0D4C_main_cid_CID-78502182U1776649-9D67C1-1120-846940_sub_browser_81e15a6d.messages.jsonl"
products = []
seen_names = set()

with open(log_path, 'r') as f:
    for line in f:
        if '"output": "' in line:
            # Extract the content inside the "output" field
            match = re.search(r'"output":\s*"(.*?)"', line)
            if match:
                content = match.group(1).replace('\\n', '\n').replace('\\"', '"')
                # Find the JSON block starting with [Result]
                if '[Result]\n' in content:
                    json_str = content.split('[Result]\n')[1]
                    try:
                        data = json.loads(json_str)
                        name = data.get('productName')
                        if name and name not in seen_names:
                            products.append(data)
                            seen_names.add(name)
                    except:
                        continue

print(f"Extracted {len(products)} unique products.")
with open('/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/full_products_187.json', 'w') as f:
    json.dump(products, f, indent=2)
