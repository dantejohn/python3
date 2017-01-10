g = {}
for _ in range(int(input())):
    t = int(input())
    if t not in g:
        g[t] = f(t)
    print(g[t])
