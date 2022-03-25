from parttime_emp import parttime
from fulltime_emp import fulltime

class application:
    def run():
        ptemp= parttime()
        ptemp._name= "Rajjev Liu"
        ptemp._address= "Toronto"
        ptemp.empID= "F101"
        ptemp.hourlywage= 50
        ptemp.biweekly_hours=30





app= application()
app.run()
