"""
Problem: abc445f
Algorithm: Matrix Exponentiation
Difficulty: 1514
Key Insight:
I model one move along a directed edge as a min-plus matrix multiplication, where combining paths means adding costs and taking the minimum.
Raising the cost matrix to the K-th power under min-plus algebra yields the minimum cost for every pair of vertices using exactly K edges.
The answer for each start vertex s is simply the diagonal entry (s,s) of the resulting matrix.

Time Complexity: O(N^3 log K)
Space Complexity: O(N^2)
"""

INF = 10**20

def mult(A,B,n):
    C = [[INF for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if A[i][k]+B[k][j]<C[i][j]:
                    C[i][j] = A[i][k]+B[k][j]
    return C

N,K=map(int,input().split())
C = [list(map(int,input().split())) for i in range(N)]
P = pow(C,K,N)

P = [[INF for _ in range(N)] for __ in range(N)]
for i in range(N): P[i][i]=0
B=C
while e:
    if e&1: P = mult(P,B,N)
    e >>= 1
    if e: B = mult(B,B,N)
[print(P[i][i]) for i in range(N)]