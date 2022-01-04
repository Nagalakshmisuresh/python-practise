#Write a Python program to check whether the given number is a Fibonacci Number or not.

#Input Format:
#Line 1: <Integer Number>
#Output Format:
#Line 1: <1 -> if the number is a Prime Number>
#<0 -> if the number is not a Prime Number>

#Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, .. (Fibonacci series is the sum of the previous two terms)

#Input:
#8
#Output:
#1
n1,n2=0,1
print(n1,n2,end=' ')
for i in range(1,11):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3

