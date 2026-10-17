# Largest, Seond Largest, Smallest, Second smallest number
n = int(input("Enter your number:"))
arr = []
for i in range(n):
    arr.append(int(input(f"Element{i+1}:")))

Largest = arr [0]
second_largest = arr [0]

Smallest = arr[0]
second_smallest = arr [0]

for num in arr:
    if num > Largest:
        second_largest = Largest
        Largest = num
    elif num > second_largest:
        second_largest = num
    if num < Smallest:
        second_smallest = Smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num

print("Largest:",Largest)
print("Second Largest", second_largest)
print("Smallest", smallest)
print("Second Smallest", second_smallest)               
