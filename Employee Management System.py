#Employee Management System

"""
1. Add Employee
2. Update Employee
3. Search Employee
4. Delete Employee
5. Display All Employee
"""

import json,os

class Employee:
    def __init__(self,employee_id,emp_email_id,name,age,address,department,experience,salary):
        self.employee_id = employee_id
        self.emp_email_id = emp_email_id
        self.name = name
        self.age = age
        self.department = department
        self.experience = experience
        self.salary = salary

    data_file = "Employee_data.json"
        
    def emp_details(self):
        print("Enter the Employee details.")
        name = (input("Enter The Name of the Employee : ")).capitalize()    
        age = int(input("Enter The Age Employee : "))
        address = (input("Enter Employee Address : "))
        emp_id = (int)(input("Enter Employee ID : "))
        emp_email_id = (input("Enter Employee Email ID : "))
        department = (input("Enter Employee Department Name : ")).capitalize()
        salary = (float)(input("Enter Employee Salary : "))
        if salary == 0:
            return "Salary Amount can't be zero"
        experience = int(input("Enter Employee Experience(yrs): "))

        return {"Name": name,"Age":age,"Employee ID":emp_id,"Employee Email ID":emp_email_id,"Address":address,"Department":department,"Experience":experience,"Salary":salary}

    def update_employee(self,employee_id):
        emp_id = employee_id
        if os.path.exists(self.data_file):
            with open(self.data_file,'r') as file:
                data = json.load(file)
            for emp in data.get("Employees",[]):
                if emp["Employee ID"] == emp_id:
                    print("Enter the updated Employee Details.")
                    updated_data_file = self.emp_details()
                    emp.update(updated_data_file)
                    with open(self.data_file,'w') as updating_file:
                        json.dump(data,updating_file,indent=4)
                    return "Employee data is Updated Successfully."
            return "Employee Not Found."
        else:
            return "File Not Found."
                    

    def add_employee(self):
        emp_data = self.emp_details()
        if os.path.exists(self.data_file):
            with open(self.data_file,'r') as file:
                data = json.load(file)
        else:
            data = {"Employees":[]}

        data["Employees"].append(emp_data)
        with open(self.data_file,'w') as file:
            json.dump(data,file,indent=4)

        print("DONE.")

    def display_all_emp(self):
        print("All Employees Details.")
        if os.path.exists(self.data_file):
            with open(self.data_file,'r') as file:
                data = json.load(file)

            for emps in data.get("Employees",[]):
                print(emps)
        else:
            print("Data file Doesnt exists.")

    def search_emp(self,employee_id):
        emp_id = employee_id
        if os.path.exists(self.data_file):
            with open(self.data_file,'r') as file:
                data = json.load(file)

            found = False

            for emp in data.get("Employees",[]):
                if emp["Employee ID"] == emp_id:
                    print(emp)
                    found = True
            if not found:
                print("Employee ID Doesnt exist in Database.")

        else:
            print("File Doesnt Exists.")

    def delete_emp(self,employee_id):
        emp_id = employee_id
        if os.path.exists(self.data_file):
            with open(self.data_file,'r') as file:
                data = json.load(file)

            emps_data = data.get("Employees",[])

            found = False

            for emp in emps_data:
                if emp["Employee ID"] == emp_id:
                    removed_emp = emp
                    emps_data.remove(emp)
                    with open(self.data_file,'w') as updating_file:
                        json.dump(data,updating_file,indent=4)
                    print(f"Successfully Deleted Employee {removed_emp}.")
                    found = True
                    
            if not found:
                print("Employee Not Found.")
        else:
            print("File Not Found.")
            

emp_obj = Employee(0,"","",0,"","",0,0)
#emp_obj.add_employee()
print("Employee Management System\n 1. Add Employee (type:- add)\n 2. Update Employee (type:- update)\n 3. Delete Employee (type:- delete)\n 4. Display All Employees (type:- display)\n 5. Search An Employee (type:- search)\n 6. End program (type:- end)")
while True:
    user_enter = (input("Enter the operation you want to perform : ")).lower()
    if user_enter == "add":
        emp_obj.add_employee()
    elif user_enter.isdigit():
        print("Only Alphabetic values are allowed.")
    elif user_enter == "display":
        emp_obj.display_all_emp()
    elif user_enter == "search":
        enter_id = (int)(input("Enter the Employee ID of the Employee : "))
        emp_obj.search_emp(enter_id)
    elif user_enter == "update":
        enter_num = (int)(input("Enter the Employee ID : "))
        print(emp_obj.update_employee(enter_num))
    elif user_enter == "delete":
        enter_num = (int)(input("Enter the Employee ID : "))
        emp_obj.delete_emp(enter_num)
    elif user_enter == "end":
        exit()
    else:
        print("Input other then operation is not supported.")
  
