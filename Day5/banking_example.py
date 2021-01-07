#=============IMPLEMENTATION===============
#sample data
customer_data = {
    "uid-1" : {
        "Account-no" : "123",
        "Full-Name" : "Adam",
        "Account-type" : "Savings account",
        "Balance" : 1000,
    },
     "uid-2" : {
        "Account-no" : "456",
        "Full-Name" : "Sam",
        "Account-type" : "Savings account",
        "Balance" : 1000,
    },
     "uid-3" : {
        "Account-no" : "789",
        "Full-Name" : "David",
        "Account-type" : "Savings account",
        "Balance" : 345,
    }
}

customer_creds = {
    "uid-1" : "passw1",
    "uid-2" : "passw2",
    "uid-3" : "passw3"
}


#global variable
uid = ""

def login():
    uid = input("Enter your User-Id: ")
    pwd = input("Enter your pin: ")
    if uid in customer_creds: #checking user id
        if customer_creds[uid] == pwd:  #checking password
            print("Logged in successfully")
            home()
        else:
            print("Password is incorrect!")
    else:
        print("Print User doest not exists!")



def process(option):
    uid = "uid-1"
    if option == "1":
        print("Your current balance is: ", customer_data[uid]["Balance"])
    elif option == "2":
        amout = int(input("PLease enter the amount you want to withdraw: "))
        if amout <= customer_data[uid]["Balance"]:
            customer_data[uid]["Balance"] = customer_data[uid]["Balance"] - amout
            print("Withdrowal succussful")
            return "Thank you"
        else:
            return "Insufficient funds in you account!"
        
    elif option == "3":
        current_pin = input("Please enter you pin")
        if customer_creds[uid] == current_pin:
            new_pin = input("Please enter the new pin")
            confirm = input("Please enter the new pin again")

            customer_creds[uid] = confirm
            print("YOUR PIN HAS BEEN UPDAYED SUCCESSFULLY.")
            return "Thank you"

    elif option == "4":
        return "Thank you."
    else:
        print("Please provide a valid input!")
        home()


def home():
    print("=================WELCOME TO OUR BANK================")
    print("please select any options below :")
    print("1. view balance")
    print("2. withdraw money")
    print("3. change PIN")
    print("4. exit")
    user_input = input("Please between 1 or 2 or 3 or 4")
    process(user_input)

    

login()
