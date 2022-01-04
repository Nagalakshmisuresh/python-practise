#print min variable with out using predefinrd function
n = {45,8,7,23,0,12}


for i in n:
    min = i
    break
for i in n:
    if i < min:
        min = i
    
print(min)