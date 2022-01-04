# Write code to obtain fee amount from the user and then calculate fee hike as 10% of fees and print the newly revised amount.

#Input: 28500
#Output: 31350.0
a=int(input("Enter fee amount:"))
feehike=(10)/(100)*(a)
totalfee=a+feehike
print(totalfee)
