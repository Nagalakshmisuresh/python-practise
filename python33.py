#3. Mr.Kumar went to purchase stationary items for his office. He asked the shopkeeper for a discount. The shopkeeper 
#said that if he purchases more than 200 quantity of the item, then a discount of 20% can be applied on the total bill amount, excluding the GST.
#Get the Quantity and price per item as an input and calculate and tell whether Mr.Kumar is eligible for the discount and what
#would be the net amount he has to pay after the discount.
#Take the GST at 18%.
#Net Amount = Total bill amount after discount + GST
#Input-
#Enter the required Quantity: 100
 
#price per unit is:Rs.5
#Output:
#Quantity Ordered 100 Price per item is Rs.5 Total Amount = Rs.500 GST - Rs.90.0
#Net Amount Payable is Rs.590.0

#Input-
#Enter the required Quantity: 350 price per unit is :Rs.20
#Output:
#Quantity Ordered 350 Price per item is Rs.20 Total Amount = Rs.7000
#Discount Earned = Rs.1400.0 Amount after Discount - Rs.5600.0 GST - Rs.1008.0
#Net Amount Payable is Rs.6608.0
quantity =int(input('Enter purchase quantity: '))
price=int(input('Enter price per unit: '))
total_amount = quantity*price
if quantity>200:
    total_amount = quantity*price*0.20
else:
    total_amount = price*quantity
    gst=total_amount*0.18
    final_amount=total_amount+gst
    print(final_amount)

