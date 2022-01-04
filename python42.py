#Ross is stepping into the concept of Odd and Even numbers.
 
#His teacher has explained him that any number that can be exactly divided by 2 without any reminder means that the number is even, otherwise 
#the number is odd. She has given him an homework. Ross has to write a list of Even and Odd numbers between the numbers 0 to 50.
#Our task is to help him to prepare this list.

#Sample Input:
#n = 50
#Expected Output:
#Even Numbers
#2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48
#50
#Odd Numbers
#1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49
n=int(input("Enter a number"))
i=1
print("Even numbers")
while(i<=n):
    if(i%2==0):
        print(i,end='\t')
    i=i+1
print('')
print("odd numbers")
for i in range(1,n):
    if(i%2!=0):
        print(i,end='\t')
    i=i+1
    

