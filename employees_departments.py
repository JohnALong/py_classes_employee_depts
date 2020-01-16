from employees import Employee
from companies import Company

John = Employee("John Long", "Front End Developer")
Bishop = Employee("Ryan Bishop", "Full Stack Developer")
Jeremiah = Employee("Jeremiah Bell", "Dilletante")
Trey = Employee("Trey Suiter", "Motivational Speaker")
Brenda = Employee("Brenda Long", "UI/UX specialist")

Eventbrite = Company("Eventbrite", "Tech")
NSS = Company("Nashville Software School", "Creating Developers")

NSS.add_employee(John)
NSS.add_employee(Trey)
Eventbrite.add_employee(Brenda)
Eventbrite.add_employee(Jeremiah)
Eventbrite.add_employee(Bishop)

NSS.about_company()
Eventbrite.about_company()



        
    