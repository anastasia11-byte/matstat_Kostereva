s = input().strip()

if len(s) <= 3:
    print(s)
else:
    rev = s[::-1]
    groups = [rev[i:i+3] for i in range(0, len(rev), 3)]

    result = " ".join(g[::-1] for g in groups[::-1])
    print(result)
