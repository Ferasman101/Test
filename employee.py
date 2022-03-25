from person import Person
class Employee(Person):
    def __init__(self):
        self.empID= "None"
        self._dept= "None"

    def toString(self):
        return "Employee ID: " + str(self.empID) + "Department" + str(self._dept)