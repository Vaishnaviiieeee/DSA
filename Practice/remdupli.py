# Q6: Create a new array with unique elements only
n = int(input("Enter your number: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Element {i + 1}: ")))
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Original:", arr)
print("Unique:", unique)