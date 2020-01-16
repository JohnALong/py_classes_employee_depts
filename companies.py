class Company:
    def __init__(self, name, industry):
        self.name = name
        self.address = ""
        self.industry = industry
        self.employees = list()

    def set_address(self, address):
        self.address = address

    def set_industry(self, industry):
        self.industry = industry

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def about_company(self):
        print(f"{self.name} is in the {self.industry} industry and has the following employees:")
        for employee in self.employees:
            print(employee.name)

    