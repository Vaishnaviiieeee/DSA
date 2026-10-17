# Count even and odd numbers
n = int(input("Enter your number:"))
arr = []
for i in range(n):
    arr.append(int(input(f"Element {i + 1}:")))
even = 0
odd = 0

for num in arr:
    if num %2 == 0:
        even += 1
    else:
        odd +=1

print("Even count:", even)
print("Odd count:", odd)        

                         
