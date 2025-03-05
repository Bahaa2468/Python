print("Object Oriented Programming")
class job:
    name=None
    salary=None
    hours=None

    def __init__(self,name,salary,hours):
        self.name=name
        self.salary=salary
        self.hours=hours
    
    def print(self):
        print("-- Jobs Listing: Powered by Linkedin --")
        print(f"Name:{self.name}{"|":>5}Salary {self.salary}{"|":>5} Hours: {self.hours}")

class doctor(job):
    experience=None
    speciality=None

    def __init__(self, name, salary, hours,experience,speciality):
        self.name=name
        self.salary=salary
        self.hours=hours
        self.experience=experience
        self.speciality=speciality

    def print(self):
        print()
        print(f"Name:{self.name}{"|":>5}Salary {self.salary}{"|":>5} Hours: {self.hours}Experience: {self.experience} Years{"|":>5}Speciality: {self.speciality}")

class teacher(job):
    subject=None
    position=None

    def __init__(self, name, salary, hours,subject,position):
        self.name=name
        self.salary=salary
        self.hours=hours
        self.subject=subject
        self.position=position
    def print(self):
        print()
        print(f"Name:{self.name}{"|":>5}Salary {self.salary}{"|":>5}Hours: {self.hours}{"|":>5}Subject: {self.subject}{"|":>5}Position: {self.position}")


laywer=job("Laywer","85,000","60+")
doc=doctor("Doctor","120,000","80+","5+","Pediactric Counsultant")
teach=teacher("Teacher","60,000","60+","Computer Science","High School Teacher")

laywer.print()
doc.print()
teach.print()