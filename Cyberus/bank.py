

def introduction():
    print("~-----------------------------------------~")
    print("Welcome to Abasseya's National Bank !")
    print("~-----------------------------------------~")
    fname=input("Please enter your first name : ")
    lname=input("Please enter your last name : ")
    age=int(input("Please enter your age : "))
    
    fullname=fname+lname
    print("----------------------------------------------------------------------------------------")
    print("Account Name: ",fullname)
    print("Age: ",age)
    print("----------------------------------------------------------------------------------------")
      
    if age>21:
        print("You have an account and it's active !") 
        
        while(True):
         pin_code=int(input("Enter your 4 digit PIN code : "))
         if(pin_code>9999 or pin_code<1000):
            print("Invalid PIN code please try again")
         else:
          break
            
            
        print("Your current balance :",displaybalance(),"EGP")
        print (transaction())
    
    elif age==18 and age<21:
     print("You have an account but it isn't active !")

    
    else :
         print("You don't have an account !")
   
   
   
   
   
def displaybalance(balance=2000):
       return balance
   
   
   
   
def transaction(balance=2000):
    
    while(True): 
     transaction_amount=int(input("Enter the amount you need : "))
     if(transaction_amount>balance):
         print("Invalid Transaction, your balance has insufficient funds, Please try again ! ")
     else:
        balance-=transaction_amount
        print("Remaining Balance : ",balance)
        print("`````````````````````````````````````")
        more_transactions=input("Do you want to make any other transactions ? (y/n)")
        if(more_transactions=='y'):
            continue
        else:
            break
        
    
    

introduction()



