import json
import re

log_path = "/Users/jet/.accio/accounts/1661502182/subagent-sessions/agent_agent_DID-F456DA-2B0D4C_main_cid_CID-78502182U1776649-9D67C1-1120-846940_sub_browser_81e15a6d.messages.jsonl"
output_path = "full_products_187_recovered.json"

products = []
unique_ids = set()

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            msg = json.loads(line)
            # Look for content in assistant messages or tool results
            content = msg.get('content', '')
            if not isinstance(content, str):
                content = json.dumps(content)
            
            # Find JSON-like structures that look like product data
            # Typically products have 'productName', 'mainImageUrl', or similar keys
            matches = re.findall(r'(\{[^{]*?"productName":.*?\})', content, re.DOTALL)
            for m in matches:
                try:
                    # Clean up the match (it might be partial or have extra stuff)
                    # We try to fix common JSON issues in logs
                    p_data = json.loads(m)
                    name = p_data.get('productName')
                    if name and name not in unique_ids:
                        products.append(p_data)
                        unique_ids.add(name)
                except:
                    continue
        except:
            continue

print(f"Extracted {len(products)} products from browser log.")

# Also try to load the 96 products from the other agent's directory if accessible
other_agent_products = "/Users/jet/.accio/accounts/1661502182/agents/DID-2799F4-428BC9/project/products.json"
if os.path.exists(other_agent_products):
    try:
        with open(other_agent_products, 'r') as f:
            other_data = json.load(f)
            count = 0
            for p in other_data:
                name = p.get('productName') or p.get('name')
                if name and name not in unique_ids:
                    products.append(p)
                    unique_ids.add(name)
                    count += 1
            print(f"Added {count} products from secondary agent source.")
    except Exception as e:
        print(f"Could not load other agent products: {e}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print(f"Final count: {len(products)}. Saved to {output_path}")
