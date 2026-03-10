s = 0
m = 0
d = {}
for i, v in enumerate(arr):
    s += v
    if s == k:
        m = i + 1
    if s - k in d:
        m = max(m, i - d[s - k])
    if s not in d:
        d[s] = i
return m