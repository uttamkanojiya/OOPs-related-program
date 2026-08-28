#Student Management systems

# **Features
  #1. add student
  #2. view student
  #3. search student
  #4. update student
  #5. delete student
  #6. save data in json

import json
import os
import re

class Student:
    def __init__(self,name,age,roll_no,address,course,marks,fees,is_fees_paid):        
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.address = address
        self.course = course
        self.marks = marks
        self.fees = fees
        self.is_fees_paid = is_fees_paid

    filename = "student_data.json"

    def add_student(self):
        print("Enter the student details.")
        name = (input("Enter The Name of the Student : ")).capitalize()    
        age = int(input("Enter The Age Student : "))
        roll_no = (int)(input("Enter Rollno : "))
        address = (input("Enter Student Address : "))
        course = (input("Enter Student Course Name : ")).capitalize()
        marks = (int)(input("Enter Student Total Marks Scored out of 500."))
        if marks >= 500:
            print("Maximum marks are 500.")
                
        percentage = (marks/500 * 100)
        fees = (float)(input("Enter Student Fees Amount : "))
        if fees == 0:
            print("Fees Amount can't be zero")
        is_fees_paid = (input("Is fees of the Student is Paid(y/n) ? : ")).lower()
        if is_fees_paid != 'y' or is_fees_paid != 'n':
            pass
        else:
            print(is_fees_paid)
            print("Either enter y or n.")
            
        return {"Name": name,"Age":age,"Roll No.":roll_no,"Address":address,"Course":course,"Marks":marks,"Percentage":percentage,"Fees":fees,"Fees_paid":is_fees_paid}
    
    def adding_student(self):
        new_student_data = self.add_student()
        print("Adding Student Data.")
        if os.path.exists(self.filename):
            with open(self.filename,"r") as json_file:
                file_data = json.load(json_file)
        else:
            file_data = {'Students':[]}

        file_data["Students"].append(new_student_data)

        with open(self.filename,'w') as json_file:
            json.dump(file_data,json_file,indent=4)

        print("done")

    def view_student(self,roll_no):
        rollno = roll_no
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                file_data = json.load(file)

            for student in file_data.get('Students',[]):
                if student.get("Roll No.") == rollno:
                    return student
            return "No Student found."
        return ("No File found.")

    def search_student(self,student_name):
        name = student_name.capitalize()
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                file_data = json.load(file)

            for student in file_data.get('Students',[]):
                if student.get("Name") == name:
                    return f"Student With The Name {name} Exists."
            return "No Student found."
        return ("No File found.")

    def update_student(self,roll_no):
        rollno = roll_no
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                file_data = json.load(file)
            for student in file_data.get("Students",[]):
                if student.get("Roll No.") == rollno:
                    print("Enter the updated information for the existing student.")
                    updated_student_data = self.add_student()
                    student.update(updated_student_data)
                    with open(self.filename,'w') as file:
                         json.dump(file_data,file,indent=4)
                    return("Successfully updated student data.")
            return("Student not found.")
        return ("File Not Found.")
        
    def delete_student(self,roll_no):
        rollno = roll_no
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                file_data = json.load(file)
            students = file_data.get("Students",[])
            for student in students:
                if student.get("Roll No.") == roll_no:
                    removed_student = students.remove(student)
                    with open(self.filename,'w') as file:
                        json.dump(file_data,file,indent=4)
                    return f"Successfully deleted student data {removed_student}."
            return ("Students not found.")
        return ("File Not Found.")

student_object = Student("",0,0,"","",0,0,"")
print("Student Management System.\n 1. Add Student Data(type - add).\n 2. View Student (type - view). \n 3. Search Student (type - search). \n 4. Update Student (type - update). \n 5. Delete Student data (type - delete). \n 6. To Exit from program (type - end).")
while True:
    user_enter = (input("Enter the operation you want to perform : ")).lower()
    if user_enter.isdigit():
        print("Only Alphabetic values are allowed.")
    else:
        if user_enter == "add":
            student_object.adding_student()
        elif user_enter == "view":
            enter_num = (int)(input("Enter the Roll no of the student."))
            student_object.view_student(enter_num)
        elif user_enter == "search":
            enter_name = (input("Enter the Roll no of the student."))
            if enter_name.isdigit():
                print("Name cant contain numbers")
            else:
                student_object.search_studnet(enter_name)
        elif user_enter == "update":
            enter_num = (int)(input("Enter the Roll no of the student."))
            student_object.update_student(enter_num)
        elif user_enter == "delete":
            enter_num = (int)(input("Enter the Roll no of the student."))
            student_object.delete_student(enter_num)
        elif user_enter == "end":
            exit()
        else:
            print("Input other then operation is not supported.")
#student_object.adding_student()
#print(student_object.view_student(123456))       
#print(student_object.search_student("uttam"))        
#print(student_object.update_student(123456))
#print(student_object.delete_student(1234))
