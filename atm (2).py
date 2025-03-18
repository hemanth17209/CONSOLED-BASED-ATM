print("**********************")
print("Welcome to ATM")
print("**********************")
print()
accounts = {
    1001 : ["Hemanthsai","17-11-2000",10000,7777],
    1002 : ["yaswanth","21-04-2003",20000,9999],
    1003 : ["chintu","11-11-2011",50000,None]    
    }
dobm = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation/Reset pin")
    print("4. Mini statement")
    print("5. Exit")
    option = int(input("Enter Your Option: "))
    print()
    if option == 1:
        print("**********************")
        accno =  int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exist !")
        else:
            pin = int(input("Enter Pin: "))
            if accounts[accno][-1] == None:
                print("Generate Pin")
            else:
                if accounts[accno][-1] != pin:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficent Funds ")
                    else:
                        print("Withdraw Sucessfull !")
                        accounts[accno][-2] -= amt
        print("**********************")
    elif option == 2:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account does not Exist")
        else:
            amt = int(input("Enter Amount to Deposit: "))
            accounts[accno][-2] += amt
            print("Deposit Sucessfull")
        print("**********************")
    elif option == 3:
        print("Dear Customer !! Welcome to Pin Generation: ")
        print()
        ano=int(input("enter account no:"))
        print("your acc no: ",ano)
        if accounts[ano][-1]==None:
            pin =int(input(f"Enter Your New pin {accounts[ano][0]} :"))
            accounts[ano][-1]=pin
            print()
            print("Pin is generated successfully")
            print("...Exiting from the Pin generation window......")
        else:
            decide=input("Pin is avaliable Do you want to change your password/reset password [y/n]: ")
            if decide.lower()=="y":
                old_pin =int(input("Enter your old pin:"))
                if accounts[ano][-1]==old_pin:
                    print("\"Confirmed Old Pin\"")
                    pin=int(input("Enter New Pin Now: "))
                    accounts[ano][-1]=pin
                    print()
                    print("Pin is generated successfully")
                    print(".. Exiting from the pin generation ...")
                    
                else:
                    
                    print("\n..you entered wrong old pin so Exiting from the pin generation ...")
            else:
                
                print("\nYou disagreee to change the pin so back to main window ......")
                
        print("⭐"*40)
        '''
print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            if accounts[accno][-1] == None:
                pin = int(input("Enter Pin: "))
                cpin = int(input("Confirm Pin: "))
                if pin != cpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = pin
                    print("Pin Generated Sucessfully")
            else:
                print("Pin Already Exist")
                '''
        print("**********************")
    elif option == 4:
        print("**********************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Name: {accounts[accno][0]}")
                print(f"Account Number: {accno}")
                dob = accounts[accno][1].split("-")
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dob[2]
                dob = date + "-" + month + "-" + year
                print(f"Date of Birth: {dob}")
                print(f"Account Balance: {accounts[accno][-2]}")
        print("**********************")
    else:
        break
        
