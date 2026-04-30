import json
import re

audit_path = "/Users/jet/.accio/accounts/1661502182/agents/DID-F456DA-2B0D4C/agent-core/tool-results/DID-F456DA-2B0D4C_CID-78502182U1776649-9D67C1-1120-846940/bash_7f2c15a4-58ad-4478-a0a2-99e0903d2959.txt"

with open(audit_path, 'r') as f:
    for line in f:
        # Remove line prefix like "00020| " and the path prefix
        line = re.sub(r'^[0-9]+\| ', '', line).strip()
        if ':{"' in line:
            json_str = line[line.find(':{"')+1:]
            try:
                data = json.loads(json_str)
                command = data.get('command', [])
                if command and 'build_manifest.py' in str(command):
                    full_cmd = str(command)
                    # Extract content between << "PYEOF" and PYEOF
                    # Since it's a list string, we might need a different approach
                    # But the 'command' field should contain the raw string if we're lucky
                    for part in command:
                        if 'PYEOF' in part:
                            match = re.search(r'<< "PYEOF"\n(.*?)\nPYEOF', part, re.DOTALL)
                            if match:
                                script_content = match.group(1)
                                with open('build_manifest_recovered.py', 'w') as out:
                                    out.write(script_content)
                                print("Successfully recovered build_manifest_recovered.py")
                                return
            except:
                continue

recover_script()
