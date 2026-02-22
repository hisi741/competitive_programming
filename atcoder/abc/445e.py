"""
Problem: abc445e
Algorithm: SPF + Prime Factorization
Difficulty: 1337
Key Insight: 
Compute the LCM of all N numbers via prime exponents. For each prime p, keep (max exponent m1, second max m2, count of m1).
The LCM excluding A_k differs from the full LCM only when A_k is the unique element achieving m1 for some p; then that prime’s exponent drops to m2, so we adjust by dividing by p^{m1-m2} mod MOD.
Time Complexity: O(MAXA log log MAXA + (∑N) log MAXA)
Space Complexity: O(MAXA + ∑N)
"""

MOD = 998244353
T = int(input())
MAXA = 10**7
spf = [0 for _ in range(MAXA+1)]
for i in range(2, MAXA+1):
    if spf[i] == 0:
        spf[i] = i
        if i*i<=MAXA:
            for j in range(i*i,MAXA+1,i):
                if spf[j] == 0:
                    spf[j] = i
spf[1]=1

def factorize(n):
    r = []
    while n > 1:
        p = spf[n]
        e = 0
        while n%p==0:
            n//=p
            e+=1
        r.append([p,e])
    return r

for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))

    info = {}
    facts = []
    for a in A:
        f = factorize(a)
        facts.append(f)
        for p,e in f:
            if p not in info:
                info[p] = [e,0,1]
            else:
                if e > info[p][0]:
                    info[p] = [e,info[p][0],1]
                elif e == info[p][0]:
                    info[p][2] = info[p][2]+1
                elif e > info[p][1]:
                    info[p][1] = e
    lcm = 1
    for p, (a, b, c) in info.items():
        lcm = (lcm*pow(p, a, MOD)) % MOD

    inv = {}
    ans = []
    for f in facts:
        c = lcm
        for p,e in f:
            m1,m2,c1=info[p]
            if c1==1 and e==m1:
                i = inv.get(p)
                if i is None:
                    i = pow(p, MOD-2, MOD)
                    inv[p] = i
                c = (c * pow(i, m1-m2, MOD)) % MOD
        print(c, end=" ")
    print()
