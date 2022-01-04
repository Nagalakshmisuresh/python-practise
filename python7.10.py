#unique
def printWords(l):
    for i in l:
        print(i)
str = "hi hello hi"
s = set(str.split(" "))
printWords(s)