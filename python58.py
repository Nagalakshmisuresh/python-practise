#Program to find the position of min and max elements of a list in Python.
n = [4,5,7,3,2]

max = 0
maxp = 0
min = n[1]

for i in n:
    if max < i:
        max = i
print(max)        
    
if min > i:
    min = i
print(min)