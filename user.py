users={}

class user():
    def __init__(self,username,password,phonenum,emailid,accountno,acpin,allergence):
        self.username=username
        self.password=password
        self.phonenum=phonenum
        self.emailid=emailid
        self.accountno=accountno
        self.allergence=allergence
        self.acpin=acpin
        self.isloggedin=False
        self.orderhistory=[]
        self.isordered=False
        self.amount=0
        self.payed=False
        self.dish=[]
        self.isorderd=False
        self.discountcode="food"
        self.paymenthistorry=[]
        
        

    def register(self):
        users['username']=self.username
        users['password']=self.password
        users['acpin']=self.acpin
        print("*"*140)
        print("Welcome to FOODTRUCK")
        print(f'account is created for {self.username}')
        print("*"*140)

    
    def login(self,userName,passWord):
        if userName in users['username']:
            if passWord == self.password:
                print("*"*140)
                print("acoount logged in successful")
                self.isloggedin=True
                print("*"*140)
            else:
                print("password not matched")
                
        else:
            print("username not found register your account first")
        print("="*100)    
    
    def showprofile(self):
        if self.isloggedin:
            print("............................profile status......................")
            print(f'username    : {self.username}')
            print(f'phone_number: {self.phonenum}')
            print(f'email_id    : {self.emailid}')
            print(f'allergence  : {self.allergence}')

            print("="*140)
        else:
            print("login your account first")
    def oderhis(self):
        print(f'order history : {self.orderhistory}')
        print(f'Recommended food: [ biriyani,dosa,pizza]')


    def track(self):
        min=int(input("enter minutes: "))
        if min<=5:
            print("your order is preparing now")
        elif min<=10:
            print("your order is out of delivery")
        elif min<=15:
            print("your order will deliver soon")
        else:
            print("your order is already delivered")
            

    def bill(self):
        print(".........................billing details..............................")
        print(f'username     : {self.username}')
        print(f'phone_number : {self.phonenum}')
        print(f'dish         : {self.dish}')
        print(f'total        : {self.amount}')

    def paymenttype(self):
        coupon=input("do you have any coupon code(y or n):  ")
        if coupon == "y":
            code=input("enter the code:  ")
            if code == self.discountcode:
                #self.amount =self.amount -200
                a=self.amount
                cal=(80/100)*a
                print("original price: ",self.amount)
                print("after_discount: ",cal)
                pin=int(input("enter the pin: "))
                if  pin == self.acpin:
                    print(f'bill payed successfully {cal} rupees')
                    self.payed=True
                    self.paymenthistorry.append(cal)
                else:
                    print("you have entered wrong pin")
            else:
                    print("you have entered wrong code")
        else:
            print(self.amount)
            pin=int(input("enter acpin:  "))
            if  pin == self.acpin:
                print(f'bill payed successfully {self.amount} rupees')
                self.payed=True
                self.paymenthistorry.append(self.amount)
            else:
                print("you have entered wrong pin")

    def payhistory(self):
        print(f'payment history: [{self.paymenthistorry}]' )

    def ratings(self):
        rate=int(input("give your ratings ( out of /5): "))
        if rate <=5:
            review=[]
            while True:
                print("enter your experience: ")
                print("1.good")
                print("2.average")
                print("3.bad")
                print("4.exit")
                choice=int(input("enter choice: "))
                if choice <=4:
                    match choice:
                        case 1:
                            review.append("good")
                            break
                        case 2:
                            review.append("average")
                            break
                        case 3:
                            review.append("bad")
                            break
                        case 4:
                            break
                else:
                    print("enter valid option")
                
            print("My rating is ","*"*rate,rate,"star")
            print("My review about this order ",review)
        else:
            print("-------enter valid rating below 5----")
        

    def discount(self):
        print("***SUMMER SALE IS GOING NOW***")
        print("***DISCOUNT CODE: food***")
        print("***if you use this code flat 20 percentage offer ***")
    
    #def tra(self):


    def chatbot(self):
        while True:
            print("1.orders")
            print("2.refund")
            print("3.account management")
            print("4.exit")
            choice=int(input("enter your queries: "))
            if choice <=4:
                match choice:
                    case 1:
                        print("-----go to orders in  main menu-----")
                        
                    case 2:
                        print("-----sorry for the inconvinience go to paymment option in main menu -----")

                    case 3:
                        print("-----please go to the account details -----")
                    case 4:
                        break
            else:
                print("------enter valid option-------")
                    
            


    def menulist(self):
        while True:
            print("1.annapoorna - VEG HOTEL")
            print("2.ss Hotel- NON-VEG HOTEL")
            print("3.dominos-PIZZA")
            print("4.BIB - chinese  cuisine")
            print("5.Thalapakatti - southindian cuisine")
            print("6.exit")

            choice1=int(input("enter hotel name: "))
            if choice1 <=6:
                match choice1:
                    case 1:
                        while True:
                            print("...................... ANNAPOORANA MENU .................................................")
                            print("1.dosa........................................................................... 40")
                            print("2.idli........................................................................... 20")
                            print("3.gobi chilli.................................................................... 65")
                            print("4.paneer tikka.................................................................. 150")
                            print("5.veg salad...................................................................... 90")
                            print("6.channa masala................................................................. 100")
                            print("7.gobi manchurian................................................................ 85")
                            print("8.hyderabad mushroom biriyani................................................... 125")
                            print("9.veg briyani................................................................... 110")
                            print("10.paneer fried rice............................................................ 150")
                            print("11.potato gravy.................................................................. 80")
                            print("12.veg meals.................................................................... 150")
                            print("13.poori(not recommended to people who hate oil)................................. 60")
                            print("14.paneer butter masala......................................................... 200")
                            print("15.mango milkshake(not recommended to people who hate milk)..................... 100")
                            print("16.exit")
                            choice2=int(input("enter choice: "))
                            if choice2 <=16:
                                match choice2:
                                    case 1:
                                            print("dosa ordered successfully ")
                                            self.amount =self.amount+40
                                            self.dish.append("dosa")
                                            self.orderhistory.append("dosa")
                                            print(f'dish: {self.dish}')
                                            print(f'total amount is: {self.amount}')
                                            self.isorderd=True

                                    case 2:
                                        print("idli ordered sucessfully")
                                        self.amount =self.amount+20
                                        self.dish.append("idli")
                                        self.orderhistory.append("idli")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 3:
                                        print("gobi chilli ordered sucessfully")
                                        self.amount =self.amount+65
                                        self.dish.append("gobi chilli")
                                        self.orderhistory.append("gobi chilli")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 4:
                                        print("paneer tikka ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("paneer tikka")
                                        self.orderhistory.append("paneer tikka")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 5:
                                        print("veg salad ordered sucessfully")
                                        self.amount =self.amount+90
                                        self.dish.append("veg salad")
                                        self.orderhistory.append("veg salad")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 6:
                                        print("channa masala ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("channa masala")
                                        self.orderhistory.append("channa masala")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 7:
                                        print("gobi manchurian ordered sucessfully")
                                        self.amount =self.amount+85
                                        self.dish.append("gobi manchurian")
                                        self.orderhistory.append("gobi machurian")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 8:
                                        print("hyderabad mushroom biriyani ordered sucessfully")
                                        self.amount =self.amount+125
                                        self.dish.append("hyderabad mushroom biriyani")
                                        self.orderhistory.append("hyderabad mushroom biriyani")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 9:
                                        print("veg briyani ordered sucessfully")
                                        self.amount =self.amount+110
                                        self.dish.append("veg biriyani")
                                        self.orderhistory.append("veg biriyani")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 10:
                                        chemical = "milk"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("paneer fried rice ordered sucessfully")
                                                self.amount =self.amount+150
                                                self.dish.append("paneer fried rice")
                                                self.orderhistory.append("paneer fried rice")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                            
                                    case 11:
                                        print("potato gravy ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("potato gravy")
                                        self.orderhistory.append("potato gravy")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 12:
                                        print("veg meals ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("veg meals")
                                        self.orderhistory.append("veg meals")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 13:
                                        chemical = "oil"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":  
                                                print("poori ordered sucessfully")
                                                self.amount =self.amount+60
                                                self.dish.append("poori")
                                                self.orderhistory.append("poori")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 14:
                                        print("paneer butter masala ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("paneer butter masala")
                                        self.orderhistory.append("paneer butter masala")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 15:
                                        chemical = "milk"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("mango milkshake ordered sucessfully")
                                                self.amount =self.amount+100
                                                self.dish.append("mango milkshake")
                                                self.orderhistory.append("mango milkshake")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                            
                                            
                                    case 16:
                                        break
                            else:
                                print("------enter valid option-------")
                    case 2:
                        while True:
                            print("............................ SS HOTEL MENU ..................................................")
                            print("1.chicken tikka..................................................................... 150")
                            print("2.chicken lolipop................................................................... 100")
                            print("3.beef 65............................................................................ 80")
                            print("4.mutton pepper fry................................................................. 150")
                            print("5.hyderabad chicken briyani......................................................... 200")
                            print("6.hyderabad mutton briyani.......................................................... 250")
                            print("7.chicken soup....................................................................... 80")
                            print("8.mutton soup....................................................................... 100")
                            print("9.grilled chicken................................................................... 300")
                            print("10.BBQ chicken...................................................................... 250")
                            print("11.butter chicken................................................................... 200")
                            print("12.mutton gravy(not recommended people who are intolerent to spicy food)............ 200")
                            print("13.tandoori chicken................................................................. 250")
                            print("14.brownie with icecream............................................................ 100")
                            print("15.falooda(not recommended people who hate nuts).................................... 150")
                            print("16.exit")
                            choice3=int(input("enter choice: "))
                            if choice3 <=16:

                                match choice3:
                                    case 1:
                                        print("chicken tikka ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("chicken tikka")
                                        self.orderhistory.append("chicken tikka")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 2:
                                        print("chicken lolipop ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("chicken lolipop")
                                        self.orderhistory.append("chicken lolipop")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 3:
                                        print("beef 65 ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("beef 65")
                                        self.orderhistory.append("beef 65")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 4:
                                        print("mutton pepper fry ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("mutton pepper fry")
                                        self.orderhistory.append("mutton pepper fry")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 5:
                                        print("hyderabad chicken briyani ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("hyderabad chicken briyani")
                                        self.orderhistory.append("hyderabad chicken biriyani")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 6:
                                        print("hyderabad mutton briyani ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("hyderabad mutton biriyani")
                                        self.orderhistory.append("hyderabad mutton biriyani")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 7:
                                        print("chicken soup ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("chicken soup")
                                        self.orderhistory.append("chicken soup")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 8:
                                        print("mutton soup ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("mutton soup")
                                        self.orderhistory.append("mutton soup")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 9:
                                        chemical = "oil"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("grilled chicken ordered sucessfully")
                                                self.amount =self.amount+300
                                                self.dish.append("grilled chicken")
                                                self.orderhistory.append("grilled chicken")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 10:
                                        chemical = "oil"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("BBQ chicken ordered sucessfully")
                                                self.amount =self.amount+250
                                                self.dish.append("BBQ chicken")
                                                self.orderhistory.append("BBQ chicken")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 11:
                                        print("butter chicken ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("butter chicken")
                                        self.orderhistory.append("butter chicken")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 12:
                                        print("mutton gravy ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("mutton gravy")
                                        self.orderhistory.append("mutton gravy")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 13:
                                        print("tandoori chicken ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("tandoori chicken")
                                        self.orderhistory.append("tandoori chicken")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 14:
                                        print("brownie with icecream ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("brownie with icecream")
                                        self.orderhistory.append("brownie with icecream")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 15:
                                        chemical = "milk"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("falooda ordered sucessfully")
                                                self.amount =self.amount+150
                                                self.dish.append("falooda")
                                                self.orderhistory.append("falooda")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 16:
                                        break
                            else:
                                print("-------enter valid option--------")
                    case 3:
                        while True:
                            print(".............................. DOMINOS MENU ............................................................")
                            print("1.margherita pizza............................................................................... 200")
                            print("2.chicken sausage pizza.......................................................................... 350")
                            print("3.veg pizza...................................................................................... 120")
                            print("4.non-veg pizza.................................................................................. 200")
                            print("5.corn cheese pizza(not recommended to people who are allergic to  cheese)....................... 180")
                            print("6.chicken tikka pizza............................................................................ 200")
                            print("7.chicken tandoori pizza......................................................................... 250")
                            print("8.pepperoni pizza................................................................................ 200")
                            print("9.chilli panner pizza............................................................................ 150")
                            print("10.tandoori pannerpizza.......................................................................... 200")
                            print("11.chicken keema pizza........................................................................... 200")
                            print("12.pork rib pizza................................................................................ 300")
                            print("13.BBQ pizza..................................................................................... 250")
                            print("14.cheese pizza(not recommended to people who are allergic to cheese)............................ 180")
                            print("15.garlic chicken pizza(not recommended to people who are allergic to garlic).................... 200")
                            print("16.new york style pizza.......................................................................... 250")
                            print("17.french fries(not recommended to people who hate oily food).................................... 150")
                            print("18.chicken strips................................................................................ 180")
                            print("19.garlic bread(not recommended to people who are allergic to garlic)............................ 100")
                            print("20.cool drinks.................................................................................... 50")
                            print("21.exit")
                            choice4=int(input("enter choice: "))
                            if choice4 <=21:
                                match choice4:
                                    case 1:
                                        print("margherita pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("margherita pizza")
                                        self.orderhistory.append("margherita pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 2:
                                        print("chicken sausage pizza ordered sucessfully")
                                        self.amount =self.amount+350
                                        self.dish.append("chicken sausage pizza")
                                        self.orderhistory.append("chicken sausage pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 3:
                                        print("veg pizza ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("veg pizza")
                                        self.orderhistory.append("veg pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 4:
                                        print("non-veg pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("non-veg pizza")
                                        self.orderhistory.append("non-veg pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 5:
                                        chemical = "milk"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("corn cheese pizza ordered sucessfully")
                                                self.amount =self.amount+180
                                                self.dish.append("corn cheese pizza")
                                                self.orderhistory.append("corn cheese pizza")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 6:
                                        print("chicken tikka pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("chicken tikka pizza")
                                        self.orderhistory.append("chicken tikka pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 7:
                                        print("chicken tandoori pizza ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("chicken tandoori pizza")
                                        self.orderhistory.append("chicken tandoori pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 8:
                                        print("pepperoni pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("pepperoni pizza")
                                        self.orderhistory.append("pepperoni pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True 
                                    case 9:
                                        print("chilli panner pizza ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("chilli panner pizza")
                                        self.orderhistory.append("chilli panner pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 10:
                                        print("tandoori panner pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("tandoori panner pizza")
                                        self.orderhistory.append("tandoori panner pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 11:
                                        print("chicken keema pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("chicken keema pizza")
                                        self.orderhistory.append("chicken keema pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 12:
                                        print("pork rib pizza ordered sucessfully")
                                        self.amount =self.amount+300
                                        self.dish.append("pork rib pizza")
                                        self.orderhistory.append("pork rib pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 13:
                                        print("BBQ pizza ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("BBQ pizza")
                                        self.orderhistory.append("BBQ pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 14:
                                        chemical = "milk"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("cheese pizza ordered sucessfully")
                                                self.amount =self.amount+180
                                                self.dish.append("cheese pizza")
                                                self.orderhistory.append("cheese pizza")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 15:
                                        print("garlic chicken pizza ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("garlic chicken pizza")
                                        self.orderhistory.append("garlic chicken pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 16:
                                        print("new york style pizza ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("new york style pizza")
                                        self.orderhistory.append("new york style pizza")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 17:
                                        chemical = "oil"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("french fries ordered sucessfully")
                                                self.amount =self.amount+150
                                                self.dish.append("french fries")
                                                self.orderhistory.append("french fries")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 18:
                                        print("chicken strips ordered sucessfully")
                                        self.amount =self.amount+180
                                        self.dish.append("chicken strips")
                                        self.orderhistory.append("chicken strips")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 19:
                                        print("garlic bread ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("garlic bread")
                                        self.orderhistory.append("garlic bread")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 20:
                                        print("cooldrinks ordered sucessfully")
                                        self.amount =self.amount+50
                                        self.dish.append("cooldrinks")
                                        self.orderhistory.append("cooldrinks")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 21:
                                        break
                            else:
                                print("--------enter valid option---------")

                                
                    case 4:
                        while True:
                            print("................................... BIB menu ..........................................................")
                            print("1.Naan........................................................................................ 30")
                            print("2.Butter Naan................................................................................. 50")
                            print("3.noodles.................................................................................... 100")
                            print("4.fried rice................................................................................. 120")
                            print("5.dumpling................................................................................... 200")
                            print("6.crispy fried chicken....................................................................... 150")
                            print("7.salt & pepper squid(not recommended to people who are allergic to seafood)................. 180")
                            print("8.yaung zhou fried rice...................................................................... 250")
                            print("9.scallion pancake........................................................................... 130")
                            print("10.beef chow fun............................................................................. 100")
                            print("11.momos...................................................................................... 80")
                            print("12.wonton.................................................................................... 120")
                            print("13.twice cooked pork(not recommended to people who hate pork)................................ 230")
                            print("14.braised pork belly(not recommended to people who hate pork)............................... 210")
                            print("15.cold skin noodles......................................................................... 130")
                            print("16.spring roll............................................................................... 120")
                            print("17.chinese omelette........................................................................... 60")
                            print("18.dragon chicken............................................................................ 200")
                            print("19.stir-fry shrips(not recommended to people who are allergic to seafood).................... 180")
                            print("20.ice cream................................................................................. 120")
                            print("21.century egg............................................................................... 110")
                            print("22.hot pot................................................................................... 120")
                            print("23.chinese cabbage salad..................................................................... 220")
                            print("24.dim sums.................................................................................. 150")
                            print("25.sweet & sour ribs(not recommended to people who hate pork)................................ 240")
                            print("26.exit")
                            choice5=int(input("enter choice: "))
                            if choice5 <=26:
                                match choice5:
                                    case 1:
                                        print("Naan ordered sucessfully")
                                        self.amount =self.amount+30
                                        self.dish.append("naan")
                                        self.orderhistory.append("naan")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 2:
                                        print("Butter Naan ordered sucessfully")
                                        self.amount =self.amount+50
                                        self.dish.append("butter naan")
                                        self.orderhistory.append("butter naan")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 3:
                                        print("noodles ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("noodles")
                                        self.orderhistory.append("noodles")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 4:
                                        print("fried rice ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("fried rice")
                                        self.orderhistory.append("fried rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 5:
                                        print("dumpling ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("dumbling")
                                        self.orderhistory.append("dumbling")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 6:
                                        print("crispy fried chicken ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("crispy fried chicken")
                                        self.orderhistory.append("crispy fried chicken")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 7:
                                        chemical = "seafood"
                                        if chemical == self.allergence:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("salt & pepper squid ordered sucessfully")
                                                self.amount =self.amount+180
                                                self.dish.append("salt & pepper squit")
                                                self.orderhistory.append("salt & pepper squit")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 8:
                                        print("yaung zhou fried rice ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("yaung zhou fried rice")
                                        self.orderhistory.append("yaung zhou rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 9:
                                        print("scallion pancake ordered sucessfully")
                                        self.amount =self.amount+130
                                        self.dish.append("scallion pancake")
                                        self.orderhistory.append("scallion pancake")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 10:
                                        print("beef chow fun ordered sucessfully")
                                        self.amount =self.amount+100
                                        self.dish.append("beef chow fun")
                                        self.orderhistory.append("beef chow fun")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 11:
                                        print("momos ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("momos")
                                        self.orderhistory.append("momos")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 12:
                                        print("wonton ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("wonton")
                                        self.orderhistory.append("wonton")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 13:
                                        print("twice cooked pork ordered sucessfully")
                                        self.amount =self.amount+230
                                        self.dish.append("twice cooked pork")
                                        self.orderhistory.append("twice cooked pork")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 14:
                                        print("braised pork belly ordered sucessfully")
                                        self.amount =self.amount+210
                                        self.dish.append("braised pork belly")
                                        self.orderhistory.append("braised pork belly")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 15:
                                        print("cold skin noodles ordered sucessfully")
                                        self.amount =self.amount+130
                                        self.dish.append("cold skin noodles")
                                        self.orderhistory.append("cold skin noodless")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 16:
                                        print("spring roll ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("spring roll")
                                        self.orderhistory.append("spring roll")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 17:
                                        print("chinese omelette ordered sucessfully")
                                        self.amount =self.amount+60
                                        self.dish.append("chinese omlette")
                                        self.orderhistory.append("chinese omlette")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 18:
                                        print("dragon chicken ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("dragon chicken")
                                        self.orderhistory.append("dragon chicken")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 19:
                                        chemical="seafood"
                                        if chemical == self.seafood:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("stir-fry shrips ordered sucessfully")
                                                self.amount =self.amount+180
                                                self.dish.append("stir-fry strips")
                                                self.orderhistory.append("stir-fry strips")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                    case 20:
                                        chemical="seafood"
                                        if chemical == self.seafood:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("ice cream ordered sucessfully")
                                                self.amount =self.amount+120
                                                self.dish.append("ice cream")
                                                self.orderhistory.append("ice cream")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 21:
                                        print("century egg ordered sucessfully")
                                        self.amount =self.amount+110
                                        self.dish.append("century egg")
                                        self.orderhistory.append("century egg")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 22:
                                        print("hot pot ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("hot pot")
                                        self.orderhistory.append("hot pot")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 23:
                                        print("chinese cabbage salad ordered sucessfully")
                                        self.amount =self.amount+220
                                        self.dish.append("chinese cabbage salad")
                                        self.orderhistory.append("chinese cabbage salad")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 24:
                                        print("dim sums ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("dim sums")
                                        self.orderhistory.append("dim sums")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 25:
                                        print("sweet & sour ribs ordered sucessfully")
                                        self.amount =self.amount+240
                                        self.dish.append("sweet & sour ribs")
                                        self.orderhistory.append("sweet & sour ribs")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 26:
                                        break
                            else:
                                print("-------enter valid option-----------")
                        
                    case 5:
                        while True:
                            print(".................................... THALAPPAKATI MENU ........................................")
                            print("1.Puttu............................................................................... 40")
                            print("2.Appam............................................................................... 30")
                            print("3.rasam rice.......................................................................... 80")
                            print("4.sambar rice......................................................................... 80")
                            print("5.idili sambar........................................................................ 60")
                            print("6.masala dosa......................................................................... 80")
                            print("7.egg dosa............................................................................ 60")
                            print("8.podi dosa........................................................................... 50")
                            print("9.tomato rice......................................................................... 90")
                            print("10.biriyani.......................................................................... 180")
                            print("11.coconut rice...................................................................... 120")
                            print("12.ghee rice......................................................................... 150")
                            print("13.parotta with beef(not recommended to people who hate beef)........................ 180")
                            print("14.bajji.............................................................................. 30")
                            print("15.payasam............................................................................ 60")
                            print("16.veg gravy......................................................................... 120")
                            print("17.chicken gravy..................................................................... 180")
                            print("18.mutton gravy...................................................................... 220")
                            print("19.beef gravy(not recommended to people who hate beef)............................... 200")
                            print("20.chicken pepper fry................................................................ 200")
                            print("21.mutton pepper fry................................................................. 250")
                            print("22.south indian thali................................................................ 500")
                            print("23.aapam paaya....................................................................... 150")
                            print("24.vada(not recommended to people who hate oil)....................................... 50")
                            print("25.milkshake(not recommended to people who hate milk)................................. 60")
                            print("26.exit")
                            choice6=int(input("enter choice: "))
                            if choice6 <= 26:
                                match choice6:
                                    case 1:
                                        print("Puttu ordered sucessfully")
                                        self.amount =self.amount+40
                                        self.dish.append("puttu")
                                        self.orderhistory.append("puttu")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 2:
                                        print("Appam ordered sucessfully")
                                        self.amount =self.amount+30
                                        self.dish.append("Appam")
                                        self.orderhistory.append("Appam")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 3:
                                        print("rasam rice ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("rasam rice")
                                        self.orderhistory.append("rasam rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 4:
                                        print("sambar rice ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("sambar rice")
                                        self.orderhistory.append("sambar rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 5:
                                        print("idili sambar ordered sucessfully")
                                        self.amount =self.amount+60
                                        self.dish.append("idilli sambar")
                                        self.orderhistory.append("idilli sambar")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 6:
                                        print("masala dosa ordered sucessfully")
                                        self.amount =self.amount+80
                                        self.dish.append("masala dosa")
                                        self.orderhistory.append("masala dosa")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 7:
                                        print("egg dosa ordered sucessfully")
                                        self.amount =self.amount+60
                                        self.dish.append("egg dosa")
                                        self.orderhistory.append("egg dosa")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 8:
                                        print("podi dosa ordered sucessfully")
                                        self.amount =self.amount+50
                                        self.dish.append("podi dosa")
                                        self.orderhistory.append("podi dosa")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 9:
                                        print("tomato rice ordered sucessfully")
                                        self.amount =self.amount+90
                                        self.dish.append("tomato rice")
                                        self.orderhistory.append("tomato rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 10:
                                        print("biriyani ordered sucessfully")
                                        self.amount =self.amount+180
                                        self.dish.append("biriyani")
                                        self.orderhistory.append("biriyani")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 11:
                                        print("coconut rice ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("coconut rice")
                                        self.orderhistory.append("coconut rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 12:
                                        print("ghee rice ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("ghee rice")
                                        self.orderhistory.append("ghee rice")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 13:
                                        print("parotta with beef ordered sucessfully")
                                        self.amount =self.amount+180
                                        self.dish.append("parotta with beef")
                                        self.orderhistory.append("parotta with beef")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 14:
                                        chemical="oil"
                                        if chemical == self.seafood:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("bajji ordered sucessfully")
                                                self.amount =self.amount+30
                                                self.dish.append("bajji")
                                                self.orderhistory.append("bajji")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 15:
                                        print("payasam ordered sucessfully")
                                        self.amount =self.amount+60
                                        self.dish.append("payasam")
                                        self.orderhistory.append("payasam")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 16:
                                        print("veg gravy ordered sucessfully")
                                        self.amount =self.amount+120
                                        self.dish.append("veg gravy")
                                        self.orderhistory.append("veg gravy")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 17:
                                        print("chicken gravy ordered sucessfully")
                                        self.amount =self.amount+180
                                        self.dish.append("chicken gravy")
                                        self.orderhistory.append("chicken gravy")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 18:
                                        print("mutton gravy ordered sucessfully")
                                        self.amount =self.amount+220
                                        self.dish.append("mutton gravy")
                                        self.orderhistory.append("mutton gravy")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 19:
                                        print("beef gravy ordered sucessfully")
                                        self.amount =self.amount+200
                                        self.dish.append("beef gravy")
                                        self.orderhistory.append("beef gravy")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 20:
                                        print("chicken pepper fry ordered sucessfully")
                                        self.amount =self.amount+ 200
                                        self.dish.append("chicken pepper fry")
                                        self.orderhistory.append("chicken pepper fry")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 21:
                                        print("mutton pepper fry ordered sucessfully")
                                        self.amount =self.amount+250
                                        self.dish.append("mutton pepper fry")
                                        self.orderhistory.append("mutton pepper fry")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 22:
                                        print("south indian thali ordered sucessfully")
                                        self.amount =self.amount+500
                                        self.dish.append("south india thali")
                                        self.orderhistory.append("south india thali")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 23:
                                        print("aapam paaya ordered sucessfully")
                                        self.amount =self.amount+150
                                        self.dish.append("aapam paaya")
                                        self.orderhistory.append("aapam paaya")
                                        print(f'dish: {self.dish}')
                                        print(f'total amount is: {self.amount}')
                                        self.isorderd=True
                                    case 24:
                                        chemical="oil"
                                        if chemical == self.seafood:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("vada ordered sucessfully")
                                                self.amount =self.amount+50
                                                self.dish.append("vada")
                                                self.orderhistory.append("vada")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 25:
                                        chemical="seafood"
                                        if chemical == self.seafood:
                                            print("this food may cause allergy to you")
                                            choice=input("enter y or n: ")
                                            if choice == "y":
                                                print("milkshake ordered sucessfully")
                                                self.amount =self.amount+60
                                                self.dish.append("milkshake")
                                                self.orderhistory.append("milkshake")
                                                print(f'dish: {self.dish}')
                                                print(f'total amount is: {self.amount}')
                                                self.isorderd=True
                                            else:
                                                break
                                    case 26:
                                        break
                            else:
                                print("-------enter valid option-----")


                    case 6:
                        break
            else:
                print("------enter valid option-----")
            



