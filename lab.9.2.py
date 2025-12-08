n = input().strip()
d = input().strip()

pos = 0
for i, ch in enumerate(reversed(n), start=1):
    if ch == d:
        pos = i
        break
print(pos)