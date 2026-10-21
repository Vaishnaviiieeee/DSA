# WAC TO PRINT MAKE FREQUENCY ZERO OF AN ARRAY
n = 125367489
freq = [0] * 10

while n > 0:
    digit = n % 10
    freq[digit] += 1
    n //= 10

for i in range(10):
    print(f"Frequency of {i}: {freq[i]}")
