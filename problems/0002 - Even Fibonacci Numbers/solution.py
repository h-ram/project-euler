
fib = [1, 2]
sum_ = 2
while fib[-1] <= 4000000:
    fib.append(fib[-1] + fib[-2])
    sum_ += fib[-1] if fib[-1] % 2 == 0 else 0

print(sum_)

