import random

character = []
for i in range(ord('a'), ord('z')+1):
    character.append(chr(i))

shuffleCharacter = list(character)
random.shuffle(shuffleCharacter)

print "Original alphabets: " + ', '.join(character)
print "This is your key: " + ', '.join(shuffleCharacter)

plainText = raw_input("Enter your plain text to be encrypted: ")
encryptedText = ""
plainText = plainText.strip(" \t\n\r\v\f").lower()


for c in plainText:

    index = character.index(c)
    encryptedText+=shuffleCharacter[index]

print encryptedText