def sum_odd_squares(n):
    m = (n + 1) // 2
    return m * (2 * m - 1) * (2 * m + 1) // 3

print(sum_odd_squares(5))  
print(sum_odd_squares(285)) 
