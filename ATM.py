current_balance=10000
flag=True

def display_balance():
    print("Account balance is : {}".format(current_balance))
    
def cash_withdrawal(amount):
    global current_balance
    
    if amount>(current_balance-1000):
        print("Your balance is insufficient")
        display_balance()
        
    elif amount>100000:
        print("Maximum withdrawal amount is 100000")
        display_balance()
        
    else:
        current_balance-=amount
        display_balance()
        
def cash_deposit(amount):
    global current_balance
    current_balance+=amount
    display_balance()
    
def check():
    global flag
    print("Do you want to do anything more? (y/n)")
    do=input()
    
    if do=="n":
        print("Have a nice day!")
        flag=False
        
flag=True

print("****** ATM Machine ******")
print()
while flag:
    print("___Select what you want to do___")
    print()
    print("Account balance   : Input 1")
    print("Cash withdrawal   : Input 2")
    print("Cash deposit      : Input 3")
    print()
    choice=input("Enter your choice: ")
    print()
    
    if choice=="1":
        display_balance()
        
        
    elif choice=="2":
        print("Enter the amount you want to withdraw")
        value=float(input("Amount: "))
        cash_withdrawal(value)
        
    elif choice=="3":
        print("Enter the amount you need to deposit")
        value=float(input("Amount: "))
        cash_deposit(value)
        
    check()        
        
        
        
    
    
        
        
