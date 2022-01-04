#print maximum value with out using predefined functuon
n = {6,78,95,2,4,77}


for i in n:
    max = i
    break

for i in n:
    if i > max:
        max = i
print(max)