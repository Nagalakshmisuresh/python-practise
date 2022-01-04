#2. Progam to remove duplicate elements from the list.

num = [10,15,48,45,65,10]

c = []

for i in  num:
    
    if i not in c:
        c.append(i)
print(c)