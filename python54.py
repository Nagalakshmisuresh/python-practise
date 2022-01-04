#Program to find the differences of two lists.
l1 = [1,3,5,7,8,9]
l2 = [2,4,6,3,5,7]
d = []


for i in l1:
    if i not in l2:
        d.append(i)
for i in l2:
    if i not in l1:
        d.append(i)
print(d)