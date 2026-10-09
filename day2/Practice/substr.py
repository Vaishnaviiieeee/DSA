#Find all occurrences of a substring
s = input("Enter string: ")
sub = input("Enter substring: ")
count = 0
positions = []
start = s.find(sub)

while start != -1 and sub != "":
    count += 1
    positions.append(start)

    start = s.find(sub, start + 1)

print("Occurrences:", count)
print("Start indexes:", positions)