#character
charCount=0
str=input("Enter the string\n")
split_str=str.split()
for word in split_str:
    charCount+=len(word)
print("Total characters in the given string ",charCount)