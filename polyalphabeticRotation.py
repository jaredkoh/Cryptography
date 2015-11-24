import random

numberOfRotations = raw_input("Enter Number of Rotations: ")
numberOfRotations = int(numberOfRotations)
character = []
for i in range(ord('a'), ord('z')+1):
    character.append(chr(i))

random.shuffle(character)
print "This is your key: " + ', '.join(character)

plainText = raw_input("Enter your plain text to be encrypted: ")
encryptedText = ""
plainText = plainText.strip(" \t\n\r\v\f").lower()


for c in plainText:

    index = (character.index(c)+ numberOfRotations)% 26
    encryptedText+=character[index]

print encryptedText