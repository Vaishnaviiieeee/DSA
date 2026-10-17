# Calculate array sum
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))
total = 0
for x in arr:
    total += x

print("Array:", arr)
print("Sum:", total)


