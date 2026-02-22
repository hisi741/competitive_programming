"""
Problem: abc446f
Algorithm: BFS + Boundary counting
Difficulty: 1543
Key Insight: 
Feasible for k iff every vertex 1..k is reachable from 1 inside the induced subgraph on {1..k}.
If feasible, you must delete exactly the vertices v>k that have an incoming edge from some u<=k; removing them blocks every path that first enters >k.

Time Complexity: O(N+M)
Space Complexity: O(N+M)
"""


from collections import deque

N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    g[u-1].append(v-1)

inP = [False]*N; reach = [False]*N; wait = [False]*N; fromP = [False]*N

q = deque()
r=0; out=0
ans = []

for i in range(N):
    inP[i] = True

    if fromP[i]:
        out -= 1

    for v in g[i]:
        if not fromP[v]:
            fromP[v] = True
            if v > i:
                out += 1

    if (i==0 or wait[i]) and (not reach[i]):
        reach[i] = True
        r += 1
        q.append(i)

    while q:
        x = q.popleft()
        for y in g[x]:
            if inP[y]:
                if not reach[y]:
                    reach[y] = True
                    r += 1
                    q.append(y)
            else:
                wait[y] = True

    print(out if r==i+1 else -1)
