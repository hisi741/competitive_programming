"""
Problem: abc447f
Algorithm: Tree DP
Difficulty: 1480
Key Insight: 
A length-x centipede is equivalent to a spine path of x vertices where each spine vertex has enough extra neighbors to attach two legs.
Root the tree and do DP: keep the best downward chain that can still extend to the parent, and the best chain that already ends here.
At each node, combining the best two child chains gives the best answer passing through that node.

Time Complexity: O(N)
Space Complexity: O(N)
"""

Q = int(input())
for _ in range(Q):
    N = int(input())
    g = [[] for _ in range(N)]
    for i in range(N-1):
        A,B = map(lambda x: int(x)-1,input().split())
        g[A].append(B)
        g[B].append(A)

    deg = [len(g[i]) for i in range(N)]

    par = [-1]*N; par[0] = N
    sorting = []
    st = [0]
    while st:
        u = st.pop()
        sorting.append(u)
        for v in g[u]:
            if v != par[u]:
                par[v] = u
                st.append(v)

    a = [0]*N; b = [0]*N
    out = 1

    for u in reversed(sorting):
        p = 0; q = 0
        for v in g[u]:
            if v == par[u]:
                continue
            if a[v] > p:
                q = p
                p = a[v]
            elif a[v] > q:
                q = a[v]

        if deg[u] >= 3:
            a[u] = 1
            if deg[u] >= 4 and p:
                a[u] = 1+p

        if deg[u] >= 2:
            b[u] = 1
            if deg[u] >= 3 and p:
                b[u] = max(b[u], 1+p)
            out = max(out, b[u])

        if deg[u] >= 4 and q:
            out = max(out, 1+p+q)

    print(out)