#Write a Python program to calculate the Simple Interest by taking the values dynamically from the user. Formula: PNR/100

#Input:
#Enter the principal amount: Rs.25000 Enter the time(years): 2
#Enter the rate: 5
#Output:
#The simple interest is: R 2500.0
P=float(input("Enter principle amount"))
N=float(input("Enter time"))
R=float(input("Enter rate of interest "))
SimpleInterest=(P*N*R)/(100)
print(SimpleInterest)


