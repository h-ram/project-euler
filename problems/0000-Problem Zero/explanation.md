## Problem 0: Sum of Odd Squares

Find the sum of all odd perfect squares from 1² to n².

---

### Approach 1 (optimal): Closed-Form Formula

Odd squares come from squaring odd numbers: 1², 3², 5², 7², ...

The number of odd integers from 1 to n is:
$$m = \lfloor(n+1)/2\rfloor$$

The sum of the first m odd squares (1² + 3² + 5² + ... + (2m-1)²) is:
$$S = \frac{m(2m-1)(2m+1)}{3}$$

```
function sumOddSquares(n):
    m = floor((n + 1) / 2)
    return m * (2m - 1) * (2m + 1) / 3
```

---

### Approach 2: Brute Force

```
sum = 0
for i from 1 to n:
    square = i * i
    if square is odd:
        sum += square
return sum
```

---

## Complexity

| Approach        | Time     | Space    |
| --------------- | -------- | -------- |
| **Closed-form** | **O(1)** | **O(1)** |
| Brute force     | O(n)     | O(1)     |
