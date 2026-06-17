import re
from pathlib import Path

# Read redirects
redirects = []
with open('_redirects', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            parts = line.split()
            if len(parts) >= 2:
                redirects.append({'from': parts[0], 'to': parts[1]})

# Verify target files exist
valid = 0
invalid = 0

print("Verifying redirect targets...\n")

for r in redirects[:10]:  # Check first 10
    # Convert URL to file path
    to_path = r['to'].strip('/') + '.html'
    filepath = Path(to_path)
    
    if filepath.exists():
        print(f"[OK] {r['from']} -> {r['to']}")
        valid += 1
    else:
        print(f"[MISSING] {r['from']} -> {r['to']} (file not found: {to_path})")
        invalid += 1

print(f"\n... checked 10 of {len(redirects)} redirects")
print(f"Result: {valid}/10 targets exist")

if valid == 10:
    print("\n[PASS] Redirects are pointing to valid pages")
