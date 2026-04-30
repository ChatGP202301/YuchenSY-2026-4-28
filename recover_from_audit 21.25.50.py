import json
import re

audit_path = "/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/agent-core/tool-results/DID-F456DA-2B0D4C_CID-78502182U1776649-9D67C1-1120-846940/bash_7f2c15a4-58ad-4478-a0a2-99e0903d2959.txt"

with open(audit_path, 'r') as f:
    for line in f:
        # Remove line prefix like "00020| "
        clean_line = re.sub(r'^[0-9]+\| ', '', line).strip()
        try:
            data = json.loads(clean_line)
            command = data.get('command', [])
            if command and 'build_manifest.py' in command[-1]:
                full_cmd = command[-1]
                # Extract content between << "PYEOF" and PYEOF
                match = re.search(r'<< "PYEOF"\n(.*?)\nPYEOF', full_cmd, re.DOTALL)
                if match:
                    script_content = match.group(1)
                    with open('build_manifest_recovered.py', 'w') as out:
                        out.write(script_content)
                    print("Successfully recovered build_manifest_recovered.py")
                    break
        except:
            continue
