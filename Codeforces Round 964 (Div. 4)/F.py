MOD = int(1e9 + 7)
N = int(2e5 + 5)

fact = [1] * N

def pw(a, b):
    r = 1
    while b > 0:
        if b % 2 == 1:
            r = (r * a) % MOD
        b //= 2
        a = (a * a) % MOD
    return r

def precompute_factorials():
    for i in range(2, N):
        fact[i] = (fact[i - 1] * i) % MOD

def C(n, k):
    if n < k:
        return 0
    return (fact[n] * pw((fact[n - k] * fact[k]) % MOD, MOD - 2)) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    precompute_factorials()
    
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        a = list(map(int, data[index + 2:index + 2 + n]))
        index += 2 + n
        
        ones = sum(a)
        
        ans = 0
        for cnt_ones in range(k // 2 + 1, min(ones, k) + 1):
            ans = (ans + C(ones, cnt_ones) * C(n - ones, k - cnt_ones)) % MOD
        
        results.append(ans)
    
    for res in results:
        print(res)

main()