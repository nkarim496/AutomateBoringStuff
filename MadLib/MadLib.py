import re


# regex pattern ADJECTIVE, NOUN, ADVERB, VERB
pattern = re.compile(r"\bADJECTIVE|\bNOUN|\bADVERB|\bVERB")

# open text file and read in a list
with open('text.txt', encoding='utf-8') as textFile:
    text = textFile.read().split()

# search in a list and substitute founded word
for i in range(len(text)):
    found = pattern.search(text[i])
    if found is None:
        continue
    else:
        found = found.group()
        word = input("Enter %s: " % found)
        text[i] = pattern.sub(word, text[i])

# print to the screen and save to a new file
with open('madText.txt', 'w', encoding='utf-8') as madFile:
    madFile.write(" ".join(text))
print(" ".join(text))
