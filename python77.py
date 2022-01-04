class ATM:
    balance = 1000
    def validate(self):
        balance = 1000
        pin = input("Enter Pin: ")
        if pin == "1234":
            n = int(input(" \n 1. Check balance \n 2. Deposit \n 3. Withdrwal \n 4.exit \n  " ))
            if n == 1:
                print(balance)
            elif n== 2:
                dep =  int(input("Enter amount to deposit: "))
                balance = balance+dep
                print("Deposit succesfull current balance",balance)
            elif n == 3:
                wit = int(input("Enter amount to Withdrwal: "))
                balance = balance - wit
                print("withdral succesfull current balance: ",balance)
            elif n == 4:
                print("Thank you welcome again")
        else:
            print("Wrong pin")



