
# global variabled
email_valid = False
pass_valid = False
phone_valid = False
login_valid = False
project_input_valid = False
login_email_input = ""


def getLoginValid():
    global login_valid
    return login_valid


class Users:
    def __init__(self, f_name, l_name, phone, email, password, confirm_password):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    @staticmethod
    def emailValidation():
        global email_valid
        email_valid = False
        while email_valid == False:
            email = input("Enter Your Email: ")
            found = False
            email = email.strip().lower()
            if not "@" in email:
                email_valid = False
                print(
                    "Invalid email format. Email must contain '@'!\n")
            elif not email[-4:] in ".com.org.edu.gov.net":
                email_valid = False
                print(
                    "Invalid email format. Email must contain 'dot'!\n")
            else:
                with open("data", "r") as output:
                    lines = output.readlines()
                    for field in lines[0:]:
                        if email in field:
                            found = True
                            break
                        else:
                            found = False
                    if found == True:
                        print("\nThis email already exists!\n")
                        email_valid = False
                    else:
                        email_valid = True
                        return email
     # -----------------------------------------------------------------------

    @staticmethod
    def passValidation():
        global pass_valid
        pass_valid = False
        while pass_valid == False:
            password = input("Enter Your Password: ")
            confirm_password = input("Enter Your Confirm Password: ")
            if password == confirm_password:
                pass_valid = True
                return password, confirm_password
            elif password != confirm_password:
                pass_valid = False
                print("Password and confirm password does not match!\n")
     # -----------------------------------------------------------------------

    @staticmethod
    def phoneValidation():
        global phone_valid
        phone_valid = False
        while phone_valid == False:
            phone = input("Enter your phone number: ")
            if not(phone.isdigit()):
                print("Mobile only contains numbers!\n")
                phone_valid = False
            elif len(phone) < 11 or len(phone) > 11:
                print("Mobile must contain only 11 digits!\n")
                phone_valid = False
            elif (phone.startswith("010") or phone.startswith("011") or phone.startswith("012") or phone.startswith("015")) == False:
                print("Mobile must begin with '010' or '011' or '012' or '015'!\n")
                phone_valid = False
            else:
                phone_valid = True
                return phone
     # -----------------------------------------------------------------------

    @staticmethod
    def addUserToFile(new):
        global email_valid, pass_valid, phone_valid
        if (email_valid and pass_valid and phone_valid == True):
            with open('data', 'a') as dataFile:
                input_data = [new.f_name, " ", new.l_name, " ",
                              new.email, " ", new.phone, " ", new.password, "\n"]
                dataFile.writelines(input_data)
        else:
            print("Something went wrong, please try again!\n")
     # -----------------------------------------------------------------------

    @staticmethod
    def loginValidation():
        global login_email_input, project_input_valid, login_valid
        login_valid = False
        while login_valid == False:
            login_email_input = input("Enter your email: ")
            login_pass_input = input("Enter your password: ")
            found = False
            with open("data", "r") as output:
                lines = output.readlines()
                for field in lines[1:]:
                    if (login_email_input == field.split()[2]) and (login_pass_input == field.split()[4]):
                        found = True
                        break
                    else:
                        found = False
            if found == True:
                print("Valid Email And Password :D\nLogin Successfully\n")
                login_valid = True
            else:
                print("Something Wrong In Your Email or Password, Try Again!\n")
                login_valid = False

        from project import Projects
        if login_valid == True:
            while True:
                project_input_str = input(
                    "1- Create a new project\n2- Show All Projects\n3- Search Project\n4- Delete Project\n5- Back to Main Menu\nEnter You Choice: ")
                project_input = int(project_input_str)
                if project_input == 1:
                    project_input_valid = True
                    title = input("Enter Project Title: ")
                    details = input("Enter Project Details: ")
                    total_budget = Projects.targetValidation()
                    start_date, end_date = Projects.dateValidation()
                    newProject = Projects(
                        title, details, total_budget, start_date, end_date)
                    Projects.addProjectToFile(newProject,login_email_input)
                    # createNewProject(login_email_input)
                elif project_input == 2:
                    project_input_valid = True
                    Projects.viewAllProjects()
                    # viewAllProjects()
                elif project_input == 3:
                    project_input_valid = True
                    Projects.searchForProject(Projects)
                    # searchForProject()
                elif project_input == 4:
                    project_input_valid = True
                    Projects.deleteProject(login_email_input)
                    # deleteProject(login_email_input)
                elif project_input == 5:
                    from main import Main
                    project_input_valid = True
                    Main()
                elif project_input_valid != True:
                    print("\nInvalid Choice, Please Enter 1 or 2 or 3\n")
    # -----------------------------------------------------------------------
