def sum_multiples(k, n):
    m = (n - 1) // k
    return k * m * (m + 1) // 2

def solve(n):
    return sum_multiples(3, n) + sum_multiples(5, n) - sum_multiples(15, n)

print(solve(10))
print(solve(1000))
