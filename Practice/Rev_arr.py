# Q5: Display array in reverse order without changing the original
n = int(input("Enter your number: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Element {i + 1}: ")))
print("Reverse order:", end=" ")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")

print("\nOriginal array:", arr)