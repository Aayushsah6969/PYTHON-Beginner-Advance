# Create a class “Programmer” for storing information of few programmers
# working at Microsoft

class Programmer:
     def __init__(self, name, lang, dept):
          print("Setting all default")
          self.name=name
          self.lang=lang
          self.dept=dept 
     def details(self):
          print(f"At Microsoft: Programmer: {self.name}, language using: {self.lang}, department: {self.dept}")

emp=Programmer("Aayush","Python","Software")
emp.details()

     