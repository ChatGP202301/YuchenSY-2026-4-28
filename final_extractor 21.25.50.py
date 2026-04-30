import json
import re

log_path = "/Users/jet/.accio/accounts/1661502182/subagent-sessions/agent_agent_DID-F456DA-2B0D4C_main_cid_CID-78502182U1776649-9D67C1-1120-846940_sub_browser_81e15a6d.messages.jsonl"
all_products = []
seen_names = set()

with open(log_path, 'r') as f:
    for line in f:
        if 'productName' in line:
            # The line is a JSON object. We need to get the "content" or "output" field.
            try:
                data = json.loads(line)
                content = data.get('content', '') or data.get('output', '')
                # Handle cases where the data is nested inside tool_result
                if not content and 'tool_result' in data:
                    content = data['tool_result'].get('content', '')
                
                # Look for the JSON block starting with [Result]
                if '[Result]' in content:
                    json_part = content.split('[Result]')[1].strip()
                    # Remove trailing markers if any
                    json_part = json_part.split('"}')[0].strip()
                    # The JSON part itself might have escaped quotes
                    # but if it was inside a JSON string, json.loads(line) already unescaped it once.
                    product_data = json.loads(json_part)
                    name = product_data.get('productName')
                    if name and name not in seen_names:
                        all_products.append(product_data)
                        seen_names.add(name)
            except Exception as e:
                continue

print(f"Total Products Extracted: {len(all_products)}")
with open('/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/project/FULL_DATABASE_187.json', 'w') as f:
    json.dump(all_products, f, indent=2)
