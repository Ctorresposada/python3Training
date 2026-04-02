from employeeClass import employee

class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employees(self):
        print('Current Employees:\n')
        for i in self.employees:
            print(i.fname,i.lname,i.salary)
    def pay_employees(self):
        print('Paying employees')
        for i in self.employees:
            print('Paycheck for: ', i.fname,i.lname)
            print('Amount: ', i.calculate_paycheck())
            print('--------------')
        
def main():
    my_company = Company()
    employee1 = employee('Sarah','Hess',55000)
    my_company.add_employee(employee1)
    employee1 = employee('Bob','Brown',60000)
    my_company.add_employee(employee1)
    employee1 = employee('Cuto','Maco',25000)
    my_company.add_employee(employee1)
    my_company.display_employees()
    my_company.pay_employees()

main()

