"""
Problem: arc215c
Algorithm: Monotone Fixed-Point + Suffix-Min Preprocessing
Difficulty: 1767
Key Insight: 
The last surname must belong to a top corner S such that every surname in S strictly dominates every surname outside S, so outsiders can never be the final one.
This corner is described by thresholds (A,B,C) that form the smallest fixed point of cross-implications (x>=A, y>=B, z>=C) enforced by existing points.

Time Complexity: O(ΣN)
Space Complexity: O(ΣN)
"""

INF = 10**6
T = int(input())
for _ in range(T):
    N = int(input())
    P = []
    tx=ty=tz=0

    yx = [INF]*(N+2)
    yz = [INF]*(N+2)
    xy = [INF]*(N+2)
    xz = [INF]*(N+2)
    zx = [INF]*(N+2)
    zy = [INF]*(N+2)

    for i in range(N):
        x,y,z = map(int,input().split())
        P.append([x,y,z])
        if x > tx:
            tx,ty,tz = x,y,z

        if x<yx[y]: yx[y]=x
        if z<yz[y]: yz[y]=z
        if y<xy[x]: xy[x]=y
        if z<xz[x]: xz[x]=z
        if x<zx[z]: zx[z]=x
        if y<zy[z]: zy[z]=y

    for i in range(N,0,-1):
        if yx[i+1]<yx[i]: yx[i]=yx[i+1]
        if yz[i+1]<yz[i]: yz[i]=yz[i+1]
        if xy[i+1]<xy[i]: xy[i]=xy[i+1]
        if xz[i+1]<xz[i]: xz[i]=xz[i+1]
        if zx[i+1]<zx[i]: zx[i]=zx[i+1]
        if zy[i+1]<zy[i]: zy[i]=zy[i+1]

    A,B,C=tx,ty,tz
    while True:
        a = min(A,yx[B],zx[C])
        b = min(B,xy[A],zy[C])
        c = min(C,xz[A],yz[B])
        if a==A and b==B and c==C:
            break
        A,B,C=a,b,c
    print(sum(1 for x,y,z in P if x>=A or y>=B or z>=C))
