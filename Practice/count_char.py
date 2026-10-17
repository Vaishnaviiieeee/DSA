#Count vowels, consonants, digits and special characters
s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
special = 0

for ch in s:
    if ch.isalpha():

        if ch in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch != " ":
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special:", special)