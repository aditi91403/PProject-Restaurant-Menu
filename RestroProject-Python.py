print("            Welcome to My Classic Resturant          ");
Name=input("Enter your Name please:- ")
pwd=input("Enter your Passward please:- ")
ze=[]
z3=[]
z1=[]
z2=[]
z4=[]
z5=[]
z6=[]
z7=[]
z8=[]
z9=[]
z10=[]
z11=[]
z12=[]
z13=[]
z14=[]
z15=[]
z16=[]
z17=[]
z18=[]
z19=[]
z20=[]
z21=[]
z22=[]
z23=[]
z24=[]
z25=[]
z26=[]

if(Name=="a" and pwd=="a" or Name=="aditi" and pwd=="agrawal"):
    print("Hello")
    print("Welcome", Name)

else:
    print("    Sorry, Wrong Pwd   ")
    
RW='1'
while(RW=='1'):
    print("**********************RESTURANT - MENU**************************")
    print("1. Breakfast  2. Dinner  3. Lunch 4. Exit")
    a=int(input("What do you want to take"))
    if(a==1):
        print("***********************Breakfast - Items********************")
        print("1. Veg Breakfast   2. Non-Veg Breakfast")
        b=int(input("What you want"))
        if(b==1):
            VBI='1'
            while(VBI=='1'):
                print("***********************Veg- Breakfast- Items********************")
                print("1. Upma \n2. Patties  \n3. Idli  \n4. Chilla \n5. Bread \n6. Exit")
                Bft=int(input("Which type of Breakfast? :"))
                if(Bft==1):
                    UP='1'
                    while(UP=='1'):
                        print("1. Semiya Upma :Rs30 \n 2. Rava Upma :Rs40 \n 3. Tomato Upma :Rs50 \n 4. Bread Upma :Rs60 \n 5. Exit")
                        u1=input("Which type of Upma? :")
                        if(u1=='1'):
                            SU='1'
                            while(SU=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Semiya Upma has been added to your order")
                                b=int(30*quantity)
                                ze.append(b)
                                SU=input("Want to add semiya Upma again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(ze))
                            CT='1'
                            while(CT=='1'):
                                add2=input("1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. Exit")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z3))
                                    break
                            CT=input("Wanna Add Some Chutney nd Ketch-up Again? (1.yes / 2. no) ")
                        if(u1=='2'):
                            SU='1'
                            while(SU=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Rava Upma has been added to your order")
                                rate=40
                                b=int(rate*quantity)
                                ze.append(b)
                                SU=input("Want to add Rava Upma again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(ze))
                            CT='1'
                            while(CT=='1'):
                                add2=input("1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='4'):
                                    print("No Added Anything.")
                                    print("Your Addons Bill is ", sum(z3))
                                    break
                            CT=input("wanna add some chutney and Ketch-up? (1.yes / 2. no) ")

                        if(u1=='3'):
                            SU='1'
                            while(SU=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Tomato Upma has been added to your order")
                                b=int(50*quantity)
                                ze.append(b)
                                SU=input("Want to add Tomato Upma again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(ze))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z3))
                                    break
                            KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")

                        if(u1=='4'):
                            SU='1'
                            while(SU=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Bread Upma has been added to your order")
                                b=int(60*quantity)
                                ze.append(b)
                                SU=input("Want to add Bread Upma again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(ze))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z3.append(b1)
                                    print("Your Addons Bill is ", sum(z3))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z3))
                                    break
                            KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")
                            
                        if(u1=='5'):
                            break
                    print("Your Over All Upma Bill is ", (sum(ze)+ sum(z3)))
                   
                if(Bft==2):
                    PT='1'
                    while(PT=='1'):
                        print("1. Masala Patties :Rs40 \n 2. Cheese Patties :Rs50 \n 3. Paneer Patties :Rs60 \n 4. Tandoori Patties :Rs70 \n 5. Exit")
                        p1=input("Which type of Patties? :")
                        if(p1=='1'):
                            MP='1'
                            while(MP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Masala Patties has been added to your order")
                                b=int(40*quantity)
                                z4.append(b)
                                MP=input("Want to add Masala Patties again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z4))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z5))
                                    break
                                KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")
                        if(p1=='2'):
                            CP='1'
                            while(CP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Cheese Patties has been added to your order")
                                b=int(50*quantity)
                                z4.append(b)
                                CP=input("Want to add Cheese Patties again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z4))
                            KU='1'
                            while(KU=='1'):
                                add2=input("1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z5))
                                    break
                                KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")

                        if(p1=='3'):
                            PP='1'
                            while(PP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Paneer Patties has been added to your order")
                                b=int(60*quantity)
                                z4.append(b)
                                PP=input("Want to add Paneer Patties again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z4))
                            KU='1'
                            while(KU=='1'):
                                add2=input("1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z5))
                                    break
                                KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")

                        if(p1=='4'):
                            TP='1'
                            while(TP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Tandoori Patties has been added to your order")
                                rate=70
                                b=int(rate*quantity)
                                z4.append(b)
                                TP=input("Want to add Tandoori Patties again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z4))
                            KU='1'
                            while(KU=='1'):
                                add2=input("1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z5.append(b1)
                                    print("Your Addons Bill is ", sum(z5))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z5))
                                    break
                            KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")
                        if(p1=='5'):
                            print("Your Total Bill is ", sum(z4))
                            break
                    print("Your Over All Patties Bill is ", sum(z4)+ sum(z5))
                if(Bft==3):
                    ID='1'
                    while(ID=='1'):
                        print("1. Vegetable Idli :Rs50 \n 2. Rava Idli :Rs60 \n 3. Moong Dall Idli :Rs70 \n 4. Stuffed Idli :Rs80 \n 5. Exit")
                        i1=input("Which type of Idli? :")
                        if(i1=='1'):
                            VI='1'
                            while(VI=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Vegetable Idli has been added to your order")
                                b=int(50*quantity)
                                z6.append(b)
                                VI=input("Want to add Vegetable Idli again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z6))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Sambhar :Rs 30\n 4. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Sambhar added")
                                    b1=int(30*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z7))
                                    break
                            KU=input("wanna add some chutney nd Sambhar? (1.yes / 2. no) ")
                        if(i1=='2'):
                            RI='1'
                            while(RI=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Rava Idli has been added to your order")
                                b=int(60*quantity)
                                z6.append(b)
                                RI=input("Want to add Rava Idli again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z6))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Sambhar :Rs 30 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Sambhar added")
                                    b1=int(30*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z7))
                                    break
                            KU=input("wanna add some chutney nd Sambhar? (1.yes / 2. no) ")

                        if(i1=='3'):
                            MDI='1'
                            while(MDI=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Moong Dal Idli has been added to your order")
                                b=int(70*quantity)
                                z6.append(b)
                                MDI=input("Want to add Moong Dal Idli again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z6))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Sambhar :Rs 30 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Sambhar added")
                                    b1=int(30*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z7))
                                    break
                            KU=input("wanna add some chutney nd Sambhar? (1.yes / 2. no) ")

                        if(i1=='4'):
                            SI='1'
                            while(SI=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Stuffed Idli has been added to your order")
                                b=int(80*quantity)
                                z6.append(b)
                                SI=input("Want to add Stuffed Idli again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z6))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Sambhar :Rs 30 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Sambhar added")
                                    b1=int(30*quantity1)
                                    z7.append(b1)
                                    print("Your Addons Bill is ", sum(z7))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z7))
                                    break
                            KU=input("wanna add some chutney nd Sambhar? (1.yes / 2. no) ")
                        if(i1=='5'):
                            break
                    print("Your Over All Idli Bill is ", (sum(z6)+ sum(z7)) )    
                if(Bft==4):
                    CH='1'
                    while(CH=='1'):
                        print("1. Besan Chilla :Rs30 \n 2. Oats Chilla :Rs50 \n 3. Moong Dal Chilla :Rs60 \n 4. Paneer Chilla :Rs80 \n 5. Exit")
                        c1=input("Which type of Chilla? :")
                        if(c1=='1'):
                            BC='1'
                            while(BC=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Besan Chilla has been added to your order")
                                b=int(30*quantity)
                                z8.append(b)
                                BC=input("Want to add Besan Chilla again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z8))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5\n 4. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z9))
                                    break
                            KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")
                        if(c1=='2'):
                            OC='1'
                            while(OC=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Oats Chilla has been added to your order")
                                b=int(50*quantity)
                                z8.append(b)
                                OC=input("Want to add Oats Chilla again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z8))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z9))
                                    break
                            KU=input("wanna add some chutney nd Ketch-up? (1.yes / 2. no) ")

                        if(c1=='3'):
                            MDC='1'
                            while(MDC=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Moong Dal Chilla has been added to your order")
                                b=int(60*quantity)
                                z8.append(b)
                                MDC=input("Want to add Moong Dal Chilla again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z8))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "ketch-up added")
                                    b1=int(5*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z9))
                                    break
                            KU=input("wanna add some chutney nd ketch-up? (1.yes / 2. no) ")

                        if(c1=='4'):
                            PC='1'
                            while(PC=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Paneer Chilla has been added to your order")
                                b=int(80*quantity)
                                z8.append(b)
                                PC=input("Want to add Paneer Chilla again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z8))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Red Chutney :Rs 10 \n 2. Green Chutney :Rs 20 \n 3. Ketch-up :Rs 5 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Red Chutney added")
                                    b1=int(10*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill is ", sum(z9))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Green Chutney added")
                                    b1=int(20*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill  is ", sum(z9))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Ketch-up added")
                                    b1=int(5*quantity1)
                                    z9.append(b1)
                                    print("Your Addons Bill  is ", sum(z9))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z9))
                                    break
                            KU=input("wanna add some chutney and Ketch-up? (1.yes / 2. no) ")
                        if(c1=='5'):
                            break
                    print("Your Over All Chilla Bill is ", sum(z8)+ sum(z9))
                    
                if(Bft==5):
                    BD='1'
                    while(BD=='1'):
                        print("1. White Bread :Rs20 \n 2. Bread Roll :Rs30 \n 3. Potato Bread :Rs40 \n 4. Garlic Bread :Rs50 \n 5. Exit")
                        b1=input("Which type of Bread? :")
                        if(b1=='1'):
                            WB='1'
                            while(WB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"White Bread has been added to your order")
                                b=int(20*quantity)
                                z10.append(b)
                                WB=input("Want to add White Bread again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z10))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Jam :Rs 10 \n 2. Butter :Rs 15 \n 3. Cheese :Rs 20 \n 4. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Jam added")
                                    b1=int(10*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Butter added")
                                    b1=int(15*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Cheese added")
                                    b1=int(20*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z11))
                                    break
                            KU=input("wanna add some Jam, Cheese and Butter? (1.yes / 2. no) ")
                        if(b1=='2'):
                            BR='1'
                            while(BR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Bread Roll has been added to your order")
                                b=int(30*quantity)
                                z10.append(b)
                                BR=input("Want to add Bread Roll again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z10))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Jam :Rs 10 \n 2. Butter :Rs 15 \n 3. Cheese :Rs 20 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Jam added")
                                    b1=int(10*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Butter added")
                                    b1=int(15*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill Butter is ", sum(z11))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Cheese added")
                                    b1=int(20*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill Cheese is ", sum(z11))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z11))
                                    break
                            KU=input("wanna add some Jam, Cheese and Butter? (1.yes / 2. no) ")

                        if(b1=='3'):
                            PB='1'
                            while(PB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Potato Bread has been added to your order")
                                b=int(40*quantity)
                                z10.append(b)
                                PB=input("Want to add Potato Bread again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z10))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Jam :Rs 10 \n 2. Butter :Rs 15 \n 3. Cheese :Rs 20 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Jam added")
                                    b1=int(10*quantity1)
                                    z10.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Butter added")
                                    b1=int(15*quantity1)
                                    z10.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Cheese added")
                                    b1=int(20*quantity1)
                                    z10.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z11))
                                    break
                            KU=input("wanna add some Jam, Butter and Cheese? (1.yes / 2. no) ")

                        if(b1=='4'):
                            GB='1'
                            while(GB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Garlic Bread has been added to your order")
                                b=int(50*quantity)
                                z10.append(b)
                                GB=input("Want to add Garlic Bread again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z10))
                            KU='1'
                            while(KU=='1'):
                                add2=input(" 1. Jam :Rs 10 \n 2. Butter :Rs 15 \n 3. Cheese :Rs 20 \n 4. OK TATA")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Jam added")
                                    b1=int(10*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='2'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Butter added")
                                    b1=int(15*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='3'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Cheese added")
                                    b1=int(20*quantity1)
                                    z11.append(b1)
                                    print("Your Addons Bill is ", sum(z11))
                                if(add2=='4'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z11))
                                    break
                            KU=input("wanna add some Jam, Cheese and Butter? (1.yes / 2. no) ")
                        if(b1=='5'):
                            break
                    print("Your Over All Bread Bill is ", (sum(z10)+ sum(z11)) )
                    
                if(Bft==6):
                    break
                    print("Exit")
            print("Your Over All Breakfast Bill is ", (sum(ze)+sum(z3)+sum(z4)+sum(z5)+sum(z6)+sum(z7)+sum(z8)+sum(z9)+sum(z10)+sum(z11)) )

    if(a==2):
        print("***********************Dinner - Items********************")
        print("1. Veg Dinner   2. Non-Veg Dinner")
        b=int(input("What you want"))
        if(b==1):
            VDI='1'
            while(VDI=='1'):
                print("***********************Veg- Dinner- Items********************")
                print("")
                print("1. Vegetables \n2. Rice  \n3. Chapati  \n4. Raita \n5. Salad \n6. Papad \n7. Sweets \n8. Exit ")
                print("")
                DI=int(input("Which type of Dinner-Items? :"))
                if(DI==1):
                    VG='1'
                    while(VG=='1'):
                        print("1. Dal-Fry :Rs120 \n 2. Dal-Makhni :Rs150 \n 3. Methi-Aloo :Rs100 \n 4. Paneer-Bhujiya :Rs210 \n 5. Chole :Rs130 \n 6. Paneer-Kadahi :Rs200 \n 7. Mix-Veg :Rs160 \n 8. Shahi-Paneer :Rs220 \n 9. Palak-Paneer :Rs180 \n 10. Exit")
                        v1=input("Which type of Vegetables? :")
                        if(v1=='1'):
                            DF='1'
                            while(DF=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Dal-Fry has been added to your order")
                                b=int(120*quantity)
                                z1.append(b)
                                DF=input("Want to add Dal-Fry again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                           
                        if(v1=='2'):
                            DM='1'
                            while(DM=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Dal Makhni has been added to your order")
                                b=int(150*quantity)
                                z1.append(b)
                                DM=input("Want to add Dal Makhni again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                            
                        if(v1=='3'):
                            MA='1'
                            while(MA=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Methi Aloo has been added to your order")
                                b=int(100*quantity)
                                z1.append(b)
                                MA=input("Want to add Methi Aloo again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                            
                        if(v1=='4'):
                            PB='1'
                            while(PB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Paneer-Bhujiya has been added to your order")
                                b=int(210*quantity)
                                z1.append(b)
                                PB=input("Want to add Paneer-Bhujiya again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                            
                        if(v1=='5'):
                            CH='1'
                            while(CH=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Chole has been added to your order")
                                b=int(130*quantity)
                                z1.append(b)
                                CH=input("Want to add Chole again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                           
                        if(v1=='6'):
                            PK='1'
                            while(PK=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Paneer-Kadahi has been added to your order")
                                b=int(200*quantity)
                                z1.append(b)
                                PK=input("Want to add Paneer-Kadahi again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                            
                        if(v1=='7'):
                            MV='1'
                            while(MV=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Mix-Veg has been added to your order")
                                b=int(160*quantity)
                                z1.append(b)
                                MV=input("Want to add Mix-Veg again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                            
                        if(v1=='8'):
                            SP='1'
                            while(SP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Shahi-Paneer has been added to your order")
                                b=int(220*quantity)
                                z1.append(b)
                                SP=input("Want to add Shahi-Paneer again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))

                        if(v1=='9'):
                            PP='1'
                            while(PP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Palak Paneer has been added to your order")
                                b=int(180*quantity)
                                z1.append(b)
                                PP=input("Want to add Palak Paneer again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z1))
                            
                        if(v1=='10'):
                            break
                    print("Your Over All Vegetables Bill is ", sum(z1))
                   
                if(DI==2):
                    RI='1'
                    while(RI=='1'):
                        print("1. Plain Rice :Rs60 \n 2. Zeera Rice :Rs70 \n 3. Veg Pulab :Rs80 \n 4. Mater Pulab :Rs100 \n 5. Paneer Pulab :Rs110 \n 6. Veg Briyani :Rs120 \n 7. Exit")
                        r1=input("Which type of Rice? :")
                        if(r1=='1'):
                            PR='1'
                            while(PR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Plain Rice has been added to your order")
                                b=int(60*quantity)
                                z12.append(b)
                                PR=input("Want to add Plain Rice again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z12))
                            
                        if(r1=='2'):
                            ZR='1'
                            while(ZR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Zeera Rice has been added to your order")
                                b=int(70*quantity)
                                z12.append(b)
                                ZR=input("Want to add Zeera Rice again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z12))

                        if(r1=='3'):
                            VP='1'
                            while(VP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Veg Pulab has been added to your order")
                                b=int(80*quantity)
                                z12.append(b)
                                VP=input("Want to add Veg Pulab again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z12))

                        if(r1=='4'):
                            MP='1'
                            while(MP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Mater Pulab has been added to your order")
                                b=int(100*quantity)
                                z12.append(b)
                                MP=input("Want to add Mater Pulab again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z12))

                        if(r1=='5'):
                            PP='1'
                            while(PP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Paneer Pulab has been added to your order")
                                b=int(110*quantity)
                                z12.append(b)
                                PP=input("Want to add Paneer Pulab again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z12))

                        if(r1=='6'):
                            VB='1'
                            while(VB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Veg Briyani has been added to your order")
                                b=int(120*quantity)
                                z12.append(b)
                                VB=input("Want to add Veg Briyani again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z12))
                            
                        if(r1=='7'):
                            print("Your Total Bill is ", sum(z12))
                            break
                    print("Your Over All Rice Bill is ", sum(z12))
                    
                if(DI==3):
                    CI='1'
                    while(CI=='1'):
                        print("1. Tava Roti/Butter Roti :Rs10 \n 2. Plain Naan/Butter Naan :Rs20 \n 3. Tandoori Roti :Rs30 \n 4. Exit")
                        c1=input("Which type of Roti? :")
                        if(c1=='1'):
                            TR='1'
                            while(TR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Tava Roti/Butter Roti has been added to your order")
                                b=int(10*quantity)
                                z13.append(b)
                                TR=input("Want to add Tava Roti/Butter Roti again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z13))
                            EB='1'
                            while(EB=='1'):
                                add2=input(" 1. Extra Butter :Rs 10 \n 2. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Extra Butter added")
                                    b1=int(10*quantity1)
                                    z14.append(b1)
                                    print("Your Addons Bill is ", sum(z14))
                                    
                                if(add2=='2'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z14))
                                    break
                                EB=input("Wanna Add Extra Butter ? (1.yes / 2. no) ")
                                
                        if(c1=='2'):
                            PN='1'
                            while(PN=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Plain Naan has been added to your order")
                                b=int(20*quantity)
                                z13.append(b)
                                PN=input("Want to add Plain Naan again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z13))
                            EB='1'
                            while(EB=='1'):
                                add2=input(" 1. Extra Butter :Rs 10 \n 2. Exit")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Extra Butter added")
                                    b1=int(10*quantity1)
                                    z14.append(b1)
                                    print("Your Addons Bill is ", sum(z14))
                        
                                if(add2=='2'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z14))
                                    break
                                KU=input("Wanna Add Extra Butter? (1.yes / 2. no) ")

                        if(c1=='3'):
                            TR='1'
                            while(TR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Tandoori Roti has been added to your order")
                                b=int(30*quantity)
                                z13.append(b)
                                TR=input("Want to add Tandoori Roti again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z13))
                            EB='1'
                            while(EB=='1'):
                                add2=input(" 1. Extra Butter :Rs 10 \n 2. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Extra Butter added")
                                    b1=int(10*quantity1)
                                    z14.append(b1)
                                    print("Your Addons Bill is ", sum(z14))
                            
                                if(add2=='2'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z14))
                                    break
                                KU=input("Wanna Add Extra Butter? (1.yes / 2. no) ")

                        if(c1=='4'):
                            break
                    print("Your Over All Chapati Bill is ", sum(z13)+ sum(z14))
                    
                if(DI==4):
                    RI='1'
                    while(RI=='1'):
                        print("1. Plain Raita :Rs40 \n 2. Bundi Raita :Rs50 \n 3. Veg Raita :Rs60 \n 4. Cucumber Raita :Rs80 \n 5. Fruit Raita :Rs100 \n 6. Exit")
                        r1=input("Which type of Raita? :")
                        if(r1=='1'):
                            PR='1'
                            while(PR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Plain Raita has been added to your order")
                                b=int(40*quantity)
                                z15.append(b)
                                PR=input("Want to add Plain Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z15))
                          
                        if(r1=='2'):
                            BR='1'
                            while(BR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Bundi Raita has been added to your order")
                                b=int(50*quantity)
                                z15.append(b)
                                BR=input("Want to add Bundi Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z15))

                        if(r1=='3'):
                            VR='1'
                            while(VR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Veg Raita has been added to your order")
                                b=int(60*quantity)
                                z15.append(b)
                                VR=input("Want to add Veg Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z15))

                        if(r1=='4'):
                            CR='1'
                            while(CR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Cucumber Raita has been added to your order")
                                b=int(80*quantity)
                                z15.append(b)
                                CR=input("Want to add Cucumber Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z15))

                        if(r1=='5'):
                            FR='1'
                            while(FR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Fruit Raita has been added to your order")
                                b=int(100*quantity)
                                z15.append(b)
                                FR=input("Want to add Fruit Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z15))
                            
                        if(r1=='6'):
                            break
                    print("Your Over All Raita Bill is ", sum(z15))
                    
                if(DI==5):
                    SA='1'
                    while(SA=='1'):
                        print("1. Onion Salad :Rs40 \n 2. Green Salad :Rs50 \n 3. Cucumber Salad :Rs60 \n 4. Exit")
                        s1=input("Which type of Salad? :")
                        if(s1=='1'):
                            OS='1'
                            while(OS=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Onion Salad has been added to your order")
                                b=int(40*quantity)
                                z16.append(b)
                                OS=input("Want to add Onion Salad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z16))
                            
                        if(s1=='2'):
                            GS='1'
                            while(GS=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Green Salad has been added to your order")
                                b=int(50*quantity)
                                z16.append(b)
                                GS=input("Want to add Green Salad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z16))

                        if(s1=='3'):
                            CB='1'
                            while(CB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Cucumber Salad has been added to your order")
                                b=int(60*quantity)
                                z16.append(b)
                                CB=input("Want to add Cucumber Salad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z16))

                        if(s1=='4'):
                            break
                    print("Your Over All Salad Bill is ", sum(z16) )

                if(DI==6):
                    PP='1'
                    while(PP=='1'):
                        print("1. Roasted Papad :Rs10 \n 2. Masala Papad :Rs20 \n 3. Fried Papad :Rs30 \n 4. Exit")
                        p1=input("Which type of Papad? :")
                        if(p1=='1'):
                            RP='1'
                            while(RP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Roasted Papad has been added to your order")
                                b=int(10*quantity)
                                z17.append(b)
                                RP=input("Want to add Roasted Papad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z17))
                            
                        if(p1=='2'):
                            MP='1'
                            while(MP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Masala Papad has been added to your order")
                                b=int(20*quantity)
                                z17.append(b)
                                MP=input("Want to add Masala Papad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z17))

                        if(p1=='3'):
                            FP='1'
                            while(FP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Fried Papad has been added to your order")
                                b=int(30*quantity)
                                z17.append(b)
                                FP=input("Want to add Fried Papad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z17))

                        if(p1=='4'):
                            break
                    print("Your Over All papad Bill is ", sum(z17))

                if(DI==7):
                    SW='1'
                    while(SW=='1'):
                        print("1. Gulab Jamun :Rs40 \n 2. Ras Malai :Rs70 \n 3. Gajar Halwa :Rs100 \n 4. Rasgulla :Rs50 \n 5. Exit")
                        s1=input("Which type of Sweets? :")
                        if(s1=='1'):
                            GJ='1'
                            while(GJ=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Gulab Jamun has been added to your order")
                                b=int(40*quantity)
                                z18.append(b)
                                GJ=input("Want to add Gulab Jamun again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z18))
                            
                        if(s1=='2'):
                            RM='1'
                            while(RM=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Ras Malai has been added to your order")
                                b=int(70*quantity)
                                z18.append(b)
                                RM=input("Want to add Ras Malai again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z18))

                        if(s1=='3'):
                            GH='1'
                            while(GH=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Gajar Halwa has been added to your order")
                                b=int(100*quantity)
                                z18.append(b)
                                GH=input("Want to add Gajar Halwa again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z18))
                            
                        if(s1=='4'):
                            RS='1'
                            while(RS=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Rasgulla has been added to your order")
                                b=int(50*quantity)
                                z18.append(b)
                                RS=input("Want to add Rasgulla again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z18))
                            
                        if(s1=='5'):
                            break
                    print("Your Over All Sweets Bill is ", sum(z18))
                    
                if(DI==8):
                    break
                    print("Exit")
            print("Your Over All Dinner Bill is ", (sum(z1)+sum(z2)+sum(z12)+sum(z13)+sum(z14)+sum(z15)+sum(z16)+sum(z17)+sum(z18)) )

    if(a==3):
        print("***********************Lunch - Items********************")
        print("1. Veg Lunch   2. Non-Veg Lunch")
        l=int(input("What you want"))
        if(l==1):
            VLI='1'
            while(VLI=='1'):
                print("***********************Veg- Dinner- Items********************")
                print("")
                print("1. Vegetables \n2. Rice  \n3. Chapati  \n4. Raita \n5. Salad \n6. Fruits \n7. Ice-Cream \n8. Exit ")
                print("")
                LI=int(input("Which type of Lunch-Items? :"))
                if(LI==1):
                    VG='1'
                    while(VG=='1'):
                        print("1. Masala Paneer :Rs70 \n 2. Besan Shimla Mirch :Rs80 \n 3. Jeera-Aloo :Rs90 \n 4. Crispy Bhindi Fry :Rs100 \n 5. Aloo Gobi Matar :Rs120 \n 6. Methi Moong :Rs130 \n 7. Aloo Palak :Rs140 \n 8. Turai :Rs150 \n 9. Soya :Rs160 \n 10. Exit")
                        v1=input("Which type of Vegetables? :")
                        if(v1=='1'):
                            MP='1'
                            while(DF=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Masala Paneer has been added to your order")
                                b=int(70*quantity)
                                z19.append(b)
                                MP=input("Want to add Masala Paneer again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                           
                        if(v1=='2'):
                            BSM='1'
                            while(BSM=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Besan Shimla Mirch has been added to your order")
                                b=int(80*quantity)
                                z19.append(b)
                                BSM=input("Want to add Besan Shimla Mirch again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                            
                        if(v1=='3'):
                            JA='1'
                            while(JA=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Jeera Aloo has been added to your order")
                                b=int(90*quantity)
                                z19.append(b)
                                JA=input("Want to add Jeera Aloo again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                            
                        if(v1=='4'):
                            CBF='1'
                            while(CBF=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Crispy Bhindi Fry has been added to your order")
                                b=int(100*quantity)
                                z19.append(b)
                                CBF=input("Want to add Crispy Bhindi Fry again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                            
                        if(v1=='5'):
                            AGM='1'
                            while(AGM=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Aloo Gobi Matar has been added to your order")
                                b=int(120*quantity)
                                z19.append(b)
                                AGM=input("Want to add Aloo Gobi Matar again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                           
                        if(v1=='6'):
                            MM='1'
                            while(MM=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Methi Moong has been added to your order")
                                b=int(130*quantity)
                                z19.append(b)
                                MM=input("Want to add Methi Moong again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                            
                        if(v1=='7'):
                            AP='1'
                            while(AP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Aloo Palak has been added to your order")
                                b=int(140*quantity)
                                z19.append(b)
                                AP=input("Want to add Aloo Palak again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                            
                        if(v1=='8'):
                            TR='1'
                            while(TR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Turai has been added to your order")
                                b=int(150*quantity)
                                z19.append(b)
                                TR=input("Want to add Turai again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))

                        if(v1=='9'):
                            SO='1'
                            while(SO=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Soya has been added to your order")
                                b=int(160*quantity)
                                z19.append(b)
                                SO=input("Want to add Soya again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z19))
                            
                        if(v1=='10'):
                            break
                    print("Your Over All Vegetables Bill is ", sum(z19))
                   
                if(LI==2):
                    RI='1'
                    while(RI=='1'):
                        print("1. Plain Rice :Rs60 \n 2. Zeera Rice :Rs70 \n 3. Veg Pulab :Rs80 \n 4. Mater Pulab :Rs100 \n 5. Paneer Pulab :Rs110 \n 6. Veg Briyani :Rs120 \n 7. Exit")
                        r1=input("Which type of Rice? :")
                        if(r1=='1'):
                            PR='1'
                            while(PR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Plain Rice has been added to your order")
                                b=int(60*quantity)
                                z20.append(b)
                                PR=input("Want to add Plain Rice again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z20))
                            
                        if(r1=='2'):
                            ZR='1'
                            while(ZR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Zeera Rice has been added to your order")
                                b=int(70*quantity)
                                z20.append(b)
                                ZR=input("Want to add Zeera Rice again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z20))

                        if(r1=='3'):
                            VP='1'
                            while(VP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Veg Pulab has been added to your order")
                                b=int(80*quantity)
                                z20.append(b)
                                VP=input("Want to add Veg Pulab again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z20))

                        if(r1=='4'):
                            MP='1'
                            while(MP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Mater Pulab has been added to your order")
                                b=int(100*quantity)
                                z20.append(b)
                                MP=input("Want to add Mater Pulab again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z20))

                        if(r1=='5'):
                            PP='1'
                            while(PP=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Paneer Pulab has been added to your order")
                                b=int(110*quantity)
                                z20.append(b)
                                PP=input("Want to add Paneer Pulab again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z20))

                        if(r1=='6'):
                            VB='1'
                            while(VB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Veg Briyani has been added to your order")
                                b=int(120*quantity)
                                z20.append(b)
                                VB=input("Want to add Veg Briyani again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z20))
                            
                        if(r1=='7'):
                            print("Your Total Bill is ", sum(z20))
                            break
                    print("Your Over All Rice Bill is ", sum(z20))
                    
                if(LI==3):
                    CI='1'
                    while(CI=='1'):
                        print("1. Tava Roti/Butter Roti :Rs10 \n 2. Plain Naan/Butter Naan :Rs20 \n 3. Tandoori Roti :Rs30 \n 4. Exit")
                        c1=input("Which type of Roti? :")
                        if(c1=='1'):
                            TR='1'
                            while(TR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Tava Roti/Butter Roti has been added to your order")
                                b=int(10*quantity)
                                z21.append(b)
                                TR=input("Want to add Tava Roti/Butter Roti again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z21))
                            EB='1'
                            while(EB=='1'):
                                add2=input(" 1. Extra Butter :Rs 10 \n 2. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Extra Butter added")
                                    b1=int(10*quantity1)
                                    z22.append(b1)
                                    print("Your Addons Bill is ", sum(z22))
                                    
                                if(add2=='2'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z22))
                                    break
                                EB=input("Wanna Add Extra Butter ? (1.yes / 2. no) ")
                                
                        if(c1=='2'):
                            PN='1'
                            while(PN=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Plain Naan has been added to your order")
                                b=int(20*quantity)
                                z21.append(b)
                                PN=input("Want to add Plain Naan again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z21))
                            EB='1'
                            while(EB=='1'):
                                add2=input(" 1. Extra Butter :Rs 10 \n 2. Exit")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Extra Butter added")
                                    b1=int(10*quantity1)
                                    z22.append(b1)
                                    print("Your Addons Bill is ", sum(z22))
                        
                                if(add2=='2'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z14))
                                    break
                                KU=input("Wanna Add Extra Butter? (1.yes / 2. no) ")

                        if(c1=='3'):
                            TR='1'
                            while(TR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Tandoori Roti has been added to your order")
                                b=int(30*quantity)
                                z21.append(b)
                                TR=input("Want to add Tandoori Roti again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z21))
                            EB='1'
                            while(EB=='1'):
                                add2=input(" 1. Extra Butter :Rs 10 \n 2. Exit ")
                                if(add2=='1'):
                                    quantity1=int(input("quantity? : "))
                                    print(quantity1, "Extra Butter added")
                                    b1=int(10*quantity1)
                                    z22.append(b1)
                                    print("Your Addons Bill is ", sum(z22))
                            
                                if(add2=='2'):
                                    print("No Added Anything")
                                    print("Your Addons Bill is ", sum(z22))
                                    break
                                KU=input("Wanna Add Extra Butter? (1.yes / 2. no) ")

                        if(c1=='4'):
                            break
                    print("Your Over All Chapati Bill is ", sum(z21)+ sum(z22))
                    
                if(LI==4):
                    RI='1'
                    while(RI=='1'):
                        print("1. Plain Raita :Rs40 \n 2. Bundi Raita :Rs50 \n 3. Veg Raita :Rs60 \n 4. Cucumber Raita :Rs80 \n 5. Fruit Raita :Rs100 \n 6. Exit")
                        r1=input("Which type of Raita? :")
                        if(r1=='1'):
                            PR='1'
                            while(PR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Plain Raita has been added to your order")
                                b=int(40*quantity)
                                z23.append(b)
                                PR=input("Want to add Plain Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z23))
                          
                        if(r1=='2'):
                            BR='1'
                            while(BR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Bundi Raita has been added to your order")
                                b=int(50*quantity)
                                z23.append(b)
                                BR=input("Want to add Bundi Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z23))

                        if(r1=='3'):
                            VR='1'
                            while(VR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Veg Raita has been added to your order")
                                b=int(60*quantity)
                                z23.append(b)
                                VR=input("Want to add Veg Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z23))

                        if(r1=='4'):
                            CR='1'
                            while(CR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Cucumber Raita has been added to your order")
                                b=int(80*quantity)
                                z23.append(b)
                                CR=input("Want to add Cucumber Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z23))

                        if(r1=='5'):
                            FR='1'
                            while(FR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Fruit Raita has been added to your order")
                                b=int(100*quantity)
                                z23.append(b)
                                FR=input("Want to add Fruit Raita again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z23))
                            
                        if(r1=='6'):
                            break
                    print("Your Over All Raita Bill is ", sum(z23))
                    
                if(LI==5):
                    SA='1'
                    while(SA=='1'):
                        print("1. Onion Salad :Rs40 \n 2. Green Salad :Rs50 \n 3. Cucumber Salad :Rs60 \n 4. Exit")
                        s1=input("Which type of Salad? :")
                        if(s1=='1'):
                            OS='1'
                            while(OS=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Onion Salad has been added to your order")
                                b=int(40*quantity)
                                z24.append(b)
                                OS=input("Want to add Onion Salad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z24))
                            
                        if(s1=='2'):
                            GS='1'
                            while(GS=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Green Salad has been added to your order")
                                b=int(50*quantity)
                                z24.append(b)
                                GS=input("Want to add Green Salad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z24))

                        if(s1=='3'):
                            CB='1'
                            while(CB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Cucumber Salad has been added to your order")
                                b=int(60*quantity)
                                z24.append(b)
                                CB=input("Want to add Cucumber Salad again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z24))

                        if(s1=='4'):
                            break
                    print("Your Over All Salad Bill is ", sum(z24) )

                if(LI==6):
                    SF='1'
                    while(SF=='1'):
                        print("1. Mango :Rs50 \n 2. Guava :Rs40 \n 3. Watermelon :Rs60 \n 4. Orange :Rs20 \n 5. Grapes :Rs70 \n 6. Exit")
                        f1=input("Which type of Fruits? :")
                        if(f1=='1'):
                            MA='1'
                            while(MA=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Mango has been added to your order")
                                b=int(50*quantity)
                                z25.append(b)
                                MA=input("Want to add Mango again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z25))
                            
                        if(f1=='2'):
                            GA='1'
                            while(GA=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Guava has been added to your order")
                                b=int(40*quantity)
                                z25.append(b)
                                GA=input("Want to add Guava again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z25))

                        if(f1=='3'):
                            WM='1'
                            while(WM=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Watermelon has been added to your order")
                                b=int(60*quantity)
                                z25.append(b)
                                WM=input("Want to add Watermelon again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z25))

                        if(f1=='4'):
                            OR='1'
                            while(OR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Orange has been added to your order")
                                b=int(20*quantity)
                                z25.append(b)
                                OR=input("Want to add Orange again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z25))

                        if(f1=='5'):
                            GR='1'
                            while(GR=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Grapes has been added to your order")
                                b=int(70*quantity)
                                z25.append(b)
                                GR=input("Want to add Grapes again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z25))

                        if(f1=='6'):
                            break
                    print("Your Over All Seasonable Fruits Bill is ", sum(z25))

                if(LI==7):
                    IC='1'
                    while(IC=='1'):
                        print("1. Butterscotch :Rs40 \n 2. Chocolate :Rs50 \n 3. Vanilla :Rs30 \n 4. Strawberry :Rs60 \n 5. Exit")
                        ic1=input("Which type of Ice-Cream? :")
                        if(ic1=='1'):
                            BS='1'
                            while(BS=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Butterscotch has been added to your order")
                                b=int(40*quantity)
                                z26.append(b)
                                BS=input("Want to add Butterscotch again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z26))
                            
                        if(ic1=='2'):
                            CL='1'
                            while(CL=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Chocolate has been added to your order")
                                b=int(50*quantity)
                                z26.append(b)
                                CL=input("Want to add Chocolate again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z26))

                        if(ic1=='3'):
                            VA='1'
                            while(VA=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Vanilla has been added to your order")
                                b=int(30*quantity)
                                z26.append(b)
                                VA=input("Want to add Vanilla again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z26))
                            
                        if(ic1=='4'):
                            SB='1'
                            while(SB=='1'):
                                quantity=int(input("quantity? : "))
                                print(quantity,"Strawberry has been added to your order")
                                b=int(60*quantity)
                                z26.append(b)
                                SB=input("Want to add Strawberry again (1. yes/2. No)")
                            print("Your Total Bill is ", sum(z26))
                            
                        if(ic1=='5'):
                            break
                    print("Your Over All Ice-Cream Bill is ", sum(z26))
                    
                if(LI==8):
                    break
                    print("Exit")
            print("Your Over All Lunch Bill is ", (sum(z19)+sum(z20)+sum(z21)+sum(z22)+sum(z23)+sum(z24)+sum(z25)+sum(z26)) )
        
    if(a==4):
        break
print("Your Over All Resturant Bill is", (sum(ze)+sum(z3)+sum(z1)+sum(z2)+sum(z3)+sum(z4)+sum(z5)+sum(z6)+sum(z7)+sum(z8)+sum(z9)+sum(z10)+sum(z11)+sum(z12)+sum(z13)+sum(z14)+sum(z15)+sum(z16)+sum(z17)+sum(z18)+sum(z19)+sum(z20)+sum(z21)+sum(z22)+sum(z23)+sum(z24)+sum(z25)+sum(z26)) )

