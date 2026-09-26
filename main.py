import json
from abc import ABC ,abstractmethod
from pathlib import Path


database="School_data.json"
data={"students":[],"teachers":[]}
if Path.exists(database):
    with open(database,'r') as f:
        content=f.read()
    if content:
        data=json.loads(content)   
def save():
    with open(database,'w') as f:
        json.dump(data,f,indent=4)        

class Persons(ABC):
    @abstractmethod
    def get_role(self):
       pass
    @abstractmethod
    def register(self):
        pass
    @abstractmethod
    def show(self):
        pass
    @staticmethod
    def email_valid(email):
        if '@' in email and '.' in email:
            return True
        else:
            False
    

class Student(Persons):
    def get_role(self):
        return "Student"
    def show(self):
        roll_no=input("Enter roll no to view detail:-")
        for i in data['students']:
             if i['roll_no']==roll_no:
                grade=i['grade']
                avg=sum(grade.values())/len(grade) if grade else 0
                print(f"Name:{i['name']}")
                print(f"Age:{i['age']}")
                print(f"Roll_no:{i['roll_no']}")
                print(f"Email:{i['email']}")
                print(f"Garde:{i['grade']}")
                print(f"Average:{avg}")
                return
             else:
                  print("Student not found") 
                  return
            
    def register(self):

        name=input("Enter your name:-")             
        age=int(input("Enter your age:-"))   
        roll_no=input("Enter your roll number:-")
        for i in data['students']:
                           if  i['roll_no'] ==roll_no:
                               print("Studnet Already exists")
                               return
                  
        email=input("Enter your email:-")             

       
        if not Persons.email_valid(email):
            print("...Invalid email...")
            return 
        
        
        data['students'].append(
            {
                "name":name,
                "age":age,
                "email":email,
                "roll_no":roll_no,
                "grade":{}
                
            }
        )
        save() 
        print(f"{name}  Registerd Succesfully") 
    def add_grade(self):
        roll_no=input("Enter your roll no to add grade:-")
        subject=input("Enter your subject:-")
        marks=float(input("Enter your marks:-"))
        
       
        for i in data['students']:
              if i['roll_no']==roll_no:
                                     
                                     i['grade'][subject]=marks
                                     
                                     print("Grade added succesfullt")
                                     save()
                                     
                                     return 
        print("Student not found")
            




class Teacher(Persons):
    def get_role(self):
        return "Teacher"
    def show(self):
        emp_id=int(input("Enter emp_id to view detail:-"))
        for i in data['teachers']:
             if i['emp_id']==emp_id:
                     
                print(f"Name:{i['name']}")
                print(f"Age:{i['age']}")
                print(f"emp_id:{i['emp_id']}")
                print(f"Email:{i['email']}")
                print(f"Subject:{i['Subject']}")
                return 
             else:
                  print("Invalid emp_id")
                  return 
    def register(self):

        name=input("Enter your name:-")             
        age=int(input("Enter your age:-"))             
        email=input("Enter your email:-") 
        subject=input("Enter your Subject:-")            
        emp_id=int(input("Enter your emp_id number:-"))

        if not Persons.email_valid(email):
            print("...Invalid email...")
            return 
        

        
        for i in data['teachers']:
           if  i['emp_id'] ==emp_id:
               print("Id Already exists")
               return
        data['teachers'].append(
            {
                "name":name,
                "age":age,
                "email":email,
                "Subject":subject,
                "emp_id":emp_id,
                
            }
        )
        save() 
        print(f"{name} Sir/Madam Registerd Succesfully")
                         


print("Press 1 to Register Student:-")
print("Press 2 to Register Teacher:-")
print("Press 3 to add grades:-")
print("Press 4 to Show Student's detail:-")
print("Press 5 to Show Teacher's detail:-")


     
choise=int(input("Enter your choise:-"))
std=Student()
tech=Teacher()
if choise==1:
    std.register()
    
elif choise==2:
    tech.register()
elif choise==3:
    std.add_grade()
elif choise==4:
    std.show()
elif choise==5:
    tech.show()
            