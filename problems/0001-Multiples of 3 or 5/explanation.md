## Problem 1: Multiples of 3 or 5

Find the sum of all multiples of 3 or 5 below 1000.

---

### Approach 1 (optimal): Arithmetic Series

Instead of iterating through all numbers, use the arithmetic series formula.

**Sum of multiples of k below n:**
$$S(k, n) = k \cdot \frac{m(m+1)}{2}$$
where $m = \lfloor(n-1)/k\rfloor$

**Apply inclusion-exclusion:**
$$\text{Answer} = S(3, n) + S(5, n) - S(15, n)$$

We subtract $S(15, n)$ because multiples of both 3 and 5 (i.e., multiples of 15) are counted twice.

```
function sumMultiples(k, n):
    m = floor((n - 1) / k)
    return k * m * (m + 1) / 2

function solve(n):
    return sumMultiples(3, n) + sumMultiples(5, n) - sumMultiples(15, n)
```

---

### Approach 2: Brute Force

Iterate through all numbers from 1 to n-1 and sum those divisible by 3 or 5.

```python
sum = 0
for i from 1 to n-1:
    if i%3 == 0 or i%5==0:
        sum += i
return sum
```

Simple but scales linearly with n.

---

## Complexity

| Approach              | Time     | Space    |
| --------------------- | -------- | -------- |
| **Arithmetic series** | **O(1)** | **O(1)** |
| Brute force           | O(n)     | O(1)     |
