import random
character = []


for i in range(ord('a'), ord('z')+1):
    character.append(chr(i))

plainText = raw_input("Enter your plain text to be encrypted: ")
permutationNumber = int(raw_input("Enter the number of permutation for each alphabet: "))

encryptedText = ""
plainText = plainText.strip(" \t\n\r\v\f")

for c in plainText:
    permutation = [0]*permutationNumber
    for i in range(0,permutationNumber):
        characterIndex = random.randint(0,len(character)-1)
        permutation[i] = character[characterIndex]

    encryptedText+=permutation[random.randint(0,len(permutation)-1)]
    print "Permutation for Key "+ c +" is: " + ", ".join(permutation)

print encryptedText