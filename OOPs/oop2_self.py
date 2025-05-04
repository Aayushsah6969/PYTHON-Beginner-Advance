class Employee:
    name="Aayush"
    salary=1000000
    language="Python"
    def getInfo(self):
        print(f"the salary is {self.salary} and language used is: {self.language}")

a=Employee()
print(a.name, a.salary)
a.location="Kathmandu"
print(a.location)
a.getInfo() #--> this will get convert to: Employee.getInfo(a)