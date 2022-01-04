
# Write a Python program to read two numbers from the user and swap the values of both the numbers and display the values.

#Input:
#10
#20
#Output:
#The value of x before swapping: 10 The value of y before swapping: 20
a=int(input("Enter a value"))
b=int(input("Enter b value"))
print("before swapping","a=",a,"b=",b)
temp=a;
a=b;
b=temp;
print("after swapping","a=",a,"b=",b)

