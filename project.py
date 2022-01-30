import time
from user import getLoginValid

# global variables
login_valid = getLoginValid()
total_valid = False
projectData_valid = False
search_input_project = False

class Projects:
    def __init__(self, title, details, total_budget, start_date, end_date):
        self.title = title
        self.details = details
        self.total_budget = total_budget
        self.start_date = start_date
        self.end_date = end_date
    # --------------------------------------------------

    @staticmethod
    def targetValidation():
        global total_valid
        total_valid = False
        while total_valid == False:
            total_budget = input(
                "Enter your total budget: ")
            if total_budget.isdigit():
                total_valid = True
                return total_budget
            else:
                print("Total budget must be integer!\n")
                total_valid = False

    # --------------------------------------------------
    @staticmethod
    def dateValidation():
        slash = "/"
        global projectData_valid
        projectData_valid = False
        while projectData_valid == False:
            print(
                "Enter Project Start Date and End Date in Day/Month/Year Format\n")
            start_date = input(
                "Enter start date of the project: ")
            end_date = input(
                "Enter end date of the project: ")
            if (start_date.count(slash) < 2) or (end_date.count(slash) < 2) or (start_date.count(slash) > 2) or (end_date.count(slash) > 2):
                print(
                    "Invalid Start Date or End Date Format!\n")
                projectData_valid = False
            else:
                # projectDateValidation(start_date, end_date)
                startDate = time.mktime(time.strptime(start_date, "%d/%m/%Y"))
                endDate = time.mktime(time.strptime(end_date, "%d/%m/%Y"))
                if startDate > endDate:
                    print("Start Date Must be less than end date!\n")
                    projectData_valid = False
                else:
                    print("Valid date format :D\n")
                    projectData_valid = True
                    return start_date, end_date
    # --------------------------------------------------

    @staticmethod
    def addProjectToFile(new,login_email_input):
        global total_valid, projectData_valid, login_valid
        if (total_valid and projectData_valid and login_valid == True):
            with open('projectData', 'a') as projectFile:
                input_project_data = [login_email_input, " ", new.title,
                                      " ", new.details, " ", new.total_budget, " ", new.start_date, " ", new.end_date, "\n"]
                projectFile.writelines(input_project_data)
    # --------------------------------------------------

    @staticmethod
    def viewAllProjects():
        with open("projectData", "r") as projects:
            lines = projects.readlines()
            print("\nTitle , FirstName , LastName , Budget , Start Date , End Date")
            print("================================================================")
            for field in lines[1:]:
                print(field.split()[1:])
                print("\n")

    # --------------------------------------------------
    @staticmethod
    def searchProjectByName(name):
        found = False
        with open("projectData", "r") as projects:
            lines = projects.readlines()
            print("\nTitle , FirstName , LastName , Budget , Start Date , End Date")
            print("================================================================")
            for field in lines[1:]:
                if name == field.split()[1]:
                    print(field[0:])
                    found = True
            if found == False:
                print("Didn't find any projects with this name!\n")

    # ---------------------------------------------------
    @staticmethod
    def searchProjectByStartDate(start_date):
        found = False
        with open("projectData", "r") as projects:
            lines = projects.readlines()
            print("\nTitle , FirstName , LastName , Budget , Start Date , End Date")
            print("================================================================")
            for field in lines[1:]:
                if start_date == field.split()[5]:
                    print(field[0:])
                    found = True
            if found == False:
                print("Didn't find any projects with this start date!\n")
    # --------------------------------------------------

    @staticmethod
    def deleteProject(login_email_input):
        found = False
        del_lines = []
        with open("projectData", "r") as projects:
            lines = projects.readlines()
            for i, field in enumerate(lines):
                if login_email_input == field.split()[0]:
                    # del lines[i]
                    del_lines.append(i)
                    found = True
            for i in sorted(del_lines, reverse=True):
                del lines[i]
        if found == False:
            print("Didn't find any projects created with this user email!\n")
        else:
            with open("projectData", "w+") as newProjects:
                for line in lines:
                    newProjects.write(line)

            print("Projects Deleted Successfully :D\n")
    # --------------------------------------------------
    
    def searchForProject(self):
        global search_input_project
        search_input_project = False
        while search_input_project == False:
            search_input_str = input(
                "1- Search Project By Name\n2- Search Project By Start Date\nEnter Your choice: ")
            search_input = int(search_input_str)
            if search_input == 1:
                search_input_project = True
                pname = input("Enter Project Name: ")
                self.searchProjectByName(pname)
            elif search_input == 2:
                search_input_project = True
                pstart_date = input(
                    "Enter Project Start Date: ")
                self.searchProjectByStartDate(pstart_date)
            elif search_input_project != True:
                print(
                    "\nInvalid Choice, Please Enter 1 or 2\n")

    # --------------------------------------------------
