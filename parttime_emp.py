from employee import Employee
class parttime(Employee):
    def __init__(self):
        self.hourlywage=0
        self.biweekly_hours= 0
        self.pay=0

    def CalculatePay(self):
        self.pay= self.biweekly_hours* self.hourlywage
        return self.pay


    def tostring(self):
        return("Bi-weekly houyrspay: " + str(self.CalculatePay()))
        