# global variables
is_valid = False
email_valid = False
pass_valid = False
phone_valid = False
login_valid = False
project_input_valid = False
projectData_valid = False

# start program function
class Main:
    
    def __init__(self):
        Main.startPage(self)
        
    def startPage(self):
        global is_valid
        print("\n--------Welcome To Crownd-Funding Application-------")
        # import classes
        from user import Users
        while True:
            try:
                print("1- Sign Up\n2- Login\n3-Exit\n")
                account = int(input("Enter Your Choice: "))
                if (account == 1):
                    is_valid = True
                    f_name = input("Enter Your First Name: ")
                    l_name = input("Enter Your Last Name: ")
                    email = Users.emailValidation()
                    password, confirm_password = Users.passValidation()
                    phone = Users.phoneValidation()
                    newUser = Users(f_name, l_name, phone, email, password, confirm_password )
                    Users.addUserToFile(newUser)
                    # registerUser()
                elif (account == 2):
                    is_valid = True
                    Users.loginValidation()
                    # loginUser()
                elif account == 3:
                    exit()
                elif is_valid != True:
                    print("\nInvalid Choice, Please Enter 1 or 2 or 3\n")
            except ValueError:
                print("\nInvalid Choice, Please Enter 1 or 2 or 3\n")

# -----------------------------------------------------------------------
# run the program
main = Main()