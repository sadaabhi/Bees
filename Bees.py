s = input()

from collections import Counter
d = Counter(s)
if d['b']*2 == d['e']:
    print("Yes")
else:
    print("No")