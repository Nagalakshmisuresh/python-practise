# Program to create two lists with EVEN numbers and ODD numbers from a list.
l=[1,2,3,4,5,6,7,8,9]
lodd=[]
leven=[]
for num in l:
    if num%2==0:
        leven.append(num)
    else:
        lodd.append(num)
        print(leven)
        print(lodd)

