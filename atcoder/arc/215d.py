"""
Problem: arc215d
Algorithm: Combinatorics
Difficulty: 1975
Key Insight: 
S_i <= S_{i+1}  ⇔  A_i + A_{i+1} <= A_{i+1} + A_{i+2}  ⇔  A_i <= A_{i+2},
so odd-indexed A and even-indexed A become two independent non-decreasing sequences in [0,M].
S is invariant under shifting (odd +d, even −d); take the maximal d so that either max(odd)=M or min(even)=0,
which gives a unique representative per S and reduces counting to binomial coefficients.

Time Complexity: O(N+M)
Space Complexity: O(N+M)
"""

p = 10**9+7
N,M = map(int,input().split())
kaij = [1]
t = 1
for i in range(1,M+N//2+100):
    t *= i; t %= p
    kaij.append(t)

def nCr(n,r):
    return (kaij[n]*pow(kaij[r],-1,p)*pow(kaij[n-r],-1,p)%p)

print((nCr(M+N//2,N//2)*nCr(M+(N+1)//2,(N+1)//2)+nCr(M+(N+1)//2-1,(N+1)//2-1)*nCr(M+N//2,N//2+1))%p)