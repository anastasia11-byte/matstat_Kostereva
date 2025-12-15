s = input().split()[0]
s = s.zfill(4)

if s == s[::-1]:
    print(1)
else:
    print(0)
