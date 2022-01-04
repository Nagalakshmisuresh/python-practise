# Write a program that accepts cost of goods sold (cgos) revenue generated, operating costs (oc) and prints Gross profit, net profit and net profit percentage.
#Hint: Net profit = Revenue – cgos – oc

#Input:
#500
#3000
#300
#Output:
#Gross profit is 2500 Net profit is 2200
#Net profit percentage is 73.33333333333333
cgos=int(input("Enter cost of goods sold:"))
rg=int(input("revenue generated:"))
oc=int(input("Enter operating costs:"))
grossprofit=rg-cgos
netprofit=rg-cgos-oc
netprofitpercentage=(netprofit)/(rg)*(100)
print("grossprofit:",grossprofit)
print("netprofit:",netprofit)
print("netprofitpercentage:",netprofitpercentage)







