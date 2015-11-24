numberOfRows = raw_input("Enter Number of Fences: ")
plainText = raw_input("Enter your plain text to be encrypted: ")
plainText = plainText.strip(" \t\n\r\v\f")

rails = [plainText[n::int(numberOfRows)] for n in range(int(numberOfRows))]
output = ""
for list in rails:
    output+=list


print output