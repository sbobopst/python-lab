import re
from collections import Counter

with open('auth.log', 'r') as fh:
    lines = fh.readlines()
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ip_list = []
for line in lines:
    match = pattern.search(line)

    if (match and "failed password" in line.lower()):
        ip_list.append(match.group())

for item, count in (Counter(ip_list).most_common()):
        print('Access failed for', item, count, 'times')
