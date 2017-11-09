s = 'AABCAAADA'
k = 3


t = [s[c:c+k] for c in range(len(s)) if c % k == 0]
u = []
for ti in t:
    new_ti = ''
    for c in ti:
        if not c in new_ti:
            new_ti+=c
    u.append(new_ti)
for u in u:
    print(u)
