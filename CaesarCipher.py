numberOfRotations = raw_input("Enter Number of Rotations: ")
numberOfRotations = int(numberOfRotations) % 26
character = []
for i in range(ord('a'), ord('z')+1):
    character.append(chr(i))

plainText = raw_input("Enter your plain text to be encrypted: ")
encryptedText = ""
plainText = plainText.strip(" \t\n\r\v\f")

for c in plainText:

    index = character.index(c)+ numberOfRotations
    encryptedText+=character[index]

print encryptedText