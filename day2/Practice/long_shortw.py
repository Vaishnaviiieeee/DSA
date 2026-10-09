#Longest and shortest word in a sentence
sentence = input("Enter a sentence: ")
words = []

for word in sentence.split():
    word = word.strip(".,!?;:\"'()")

    if word != "":
        words.append(word)

if len(words) == 0:
    print("No words found")

else:
    longest = words[0]
    shortest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word

    print("Longest word:", longest)
    print("Shortest word:", shortest)