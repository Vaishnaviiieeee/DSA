#Reverse each word in a sentence
sentence = input("Enter a sentence: ")
result = ""

for word in sentence.split():

    reversed_word = ""

    for ch in word:
        reversed_word = ch + reversed_word

    result = result + reversed_word + " "

print(result.strip())