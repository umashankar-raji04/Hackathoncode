from user import*

newuser=None

print("*"*170)
print("            WELCOME TO FOODTRUCK      ")
print("            food delivery app            ")
print("*"*170)
print("hi")

while True:
    print("1.register")
    print("2.login")
    print("3.order,allergens")
    print("4.Bill generation")
    print("5.payment,discounts")
    print("6.track order")
    print("7.ratings")
    print("8.order history")
    print("9.chatbot")
    print("10.show profile")
    print("11.exit")
    choice=int(input("enter choice            : "))
    if choice <=11:
        match choice:
            case 1:
                ("--------------------------Register page------------------------------")
                username = input("enter your name         : ")
                password = input("enter password          : ")
                ph    =int(input("enter the phone number  : "))
                emailid   =input("enter the emailid       : ")
                accno =int(input("enter the account number: "))
                accpin=int(input("enter the account_pin   : "))
                while True:
                    allergence=input("enter the allergic name (milk,oil,seafood): ")
                    if allergence == "milk":
                        newuser=user(username,password,ph,emailid,accno,accpin,allergence)
                        newuser.register()
                        break
                    elif allergence == "oil":
                        newuser=user(username,password,ph,emailid,accno,accpin,allergence)
                        newuser.register()
                        break
                    elif allergence == "seafood":
                        newuser=user(username,password,ph,emailid,accno,accpin,allergence)
                        newuser.register()
                        break
                    else:
                        print("give proper allergic name")

            case 2:
                ("--------------------------Login page------------------------------")
                if newuser is not None:
                    userName = input("enter username          : ")
                    passWord = input("enter password          : ")
                    newuser.login(userName,passWord)
                else:
                    print("register first")
            
            
            case 3:
                print("*"*150)
                ("-------------------------restaurants and menus------------------------------")
                if newuser is not None:
                    if newuser.isloggedin:
                        while True:
                            print("Restaurants and Menus")
                            newuser.menulist()
                            newuser.isordered=True
                            print("*"*140)
                            break
                                    #newhist=newhistory.append()
                    else:
                        print("login to view your profile")
                else:
                    print("register first")
                                    

            case 4:
                if newuser is not None:
                    if newuser.isloggedin:
                        print("-----------------------printing bill------------------------")
                        newuser.bill()
                        print("*"*140)
                    else:
                        print("login to view your profile")
                else:
                    print("register first")
            case 5:
                if newuser is not None:
                    if newuser.isloggedin:
                        while True:
                            print("1.discount")
                            print("2.payment")
                            choice=int(input("enter choice: "))
                            if choice <=2:
                                match choice:
                                    case 1:
                                        print("--------------------------discount & coupon codes------------------------------")
                                        newuser.discount()
                                        print("*"*140)
                                    case 2:
                                        print("--------------------------payment-type------------------------------")
                                        print("payment type: credit/debit,digitalmethod(all payments are accepted here)")
                                        newuser.paymenttype()
                                        newuser.payhistory()
                                        print("*"*140)
                                        break
                            else:
                                print("------enter valid option-----")
                        else:
                            print("login to view your profile")
                else:
                    print("register first")

            case 6:
                ("--------------------------track_order------------------------------")
                if newuser is not None:
                    if newuser.isloggedin:
                        if newuser.isordered:
                            if newuser.payed:
                                print("tracking order")
                                newuser.track()
                                print("*"*140)
                            else:
                                print("***pay the amount then only you can track order***")
                        else:
                            print("order is not placed....first place order")
                            print("*"*140)                      
                    else:
                        print("login to view your profile")
                else:
                    print("register first")

            case 7:
                if newuser is not None:
                    if newuser.isloggedin:
                        print("--------------------------ratings &reviews------------------------------")
                        count=0
                        print("1.rating")
                        newuser.ratings()
                        print("*"*140)
                        count=count+1
                        print(count)
                        if count >=2:
                            print("you are a good reviewer")
                        else:
                            pass       
                    else:
                        print("login to enter rating")
                else:
                    print("register first")
        
            case 8:
                if newuser is not None:
                    if newuser.isloggedin:
                        print("--------------------------orderhistory & discounts------------------------------")
                        newuser.oderhis()
                        print("*"*140)
                    else:
                        print("login to view your order History")
                else:
                    print("register first")
            

            
                    
            case 9:
                if newuser is not None:
                    if newuser.isloggedin:
                        print("--------------------------chatbot------------------------------")
                        newuser.chatbot()
                        print("*"*140)
                    else:
                        print("login to use chatbot")
                else:
                    print("register first")

            case 10:
                ("--------------------------View profile------------------------------")
                if newuser is not None:
                    if newuser.isloggedin:
                        newuser.showprofile()
                    else:
                        print("login to view your profile")
                else:
                    print("register first")
            case 11:
                break 
    else:
        print("*"*120)
        print("-----enter valid option---------")  
        print("*"*120)
                
        
