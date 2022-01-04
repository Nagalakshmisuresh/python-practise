#Write a Python program to read a number n from the user and compute n+nn+nnn
#Example: If the n = 5
#5+55+555 = 615

#Input:
#Enter a number n: 5
#Output:
#The value is: 615

#Input:
#Enter a number n: 20
#Output:
#The value is: 204060
n=int(input("Enter a number"))
temp=str(n)
t=temp+temp
tt=temp+temp+temp
compute=n+int(t)+int(tt)
print(compute)
