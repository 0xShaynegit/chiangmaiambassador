import re

# Read redirects file
with open('_redirects', 'r') as f:
    content = f.read()

# Parse redirects
redirects = []
for line in content.split('\n'):
    line = line.strip()
    if line and not line.startswith('#'):
        parts = line.split()
        if len(parts) >= 2:
            redirects.append({
                'from': parts[0],
                'to': parts[1],
                'status': int(parts[2]) if len(parts) > 2 else 301
            })

print(f"Total redirects configured: {len(redirects)}\n")
print("Sample redirects to test:")
for i, r in enumerate(redirects[:5]):
    print(f"  {r['from']} -> {r['to']} ({r['status']})")

print(f"\n... and {len(redirects) - 5} more redirects configured")

# Check for format issues
print("\nValidation:")
status_codes = set(r['status'] for r in redirects)
print(f"  Status codes used: {sorted(status_codes)}")

invalid = [r for r in redirects if not r['from'].startswith('/') or not r['to'].startswith('/')]
if invalid:
    print(f"  WARNING: {len(invalid)} redirects with invalid format")
else:
    print(f"  All redirect paths properly formatted")
