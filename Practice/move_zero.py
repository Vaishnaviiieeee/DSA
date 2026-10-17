# Q7: Move all zeros to the end
n = int(input("Enter your number: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Element {i + 1}: ")))
result = []

for num in arr:
    if num != 0:
        result.append(num)
for num in arr:
    if num == 0:
        result.append(num)

print("Original:", arr)
print("Result:", result)