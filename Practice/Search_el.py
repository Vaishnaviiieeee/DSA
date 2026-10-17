# Search an element
n = int(input("Enter your number:"))
arr = []

for i in range(n):
    arr.append(int(input(f"Element{i +1}:")))
key = int(input("Number to search:"))
found = False

for i in range(n):
    if arr[i] == key:
        print(key, "is present at position", i +1)
        found = True
        break

if found == False:
    print(key,"is not present in the array")    