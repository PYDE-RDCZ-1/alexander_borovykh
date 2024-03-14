x=[()]
res = [False] * 2
if x:
    res[0] = True
if x[0]:
    res[1] = True

print(res)
