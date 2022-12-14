class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print('Employee Payroll')
            print('================')
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print('')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ask_name(self):
        try:
            self.name = str(input('Please enter employee name:'))
        except:
            self.name = ''


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.salary = "M"
        self.monthly_salary = int(monthly_salary)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input('Please enter monthly salary:'))
        except:
            self.monthly_salary = 0

    def calculate_salary(self):
        return self.monthly_salary


# Create class HourlyEmployee here
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.salary = "H"
        self.hour_rate = hour_rate

    def ask_salary(self):
        try:
            self.hours_worked = int(input('Please enter hours worked:'))
            self.hour_rate = int(input('Please enter hour rate:'))
        except:
            self.hours_worked = 0
            self.hour_rate = 0

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked


# Create class CommissionEmployee here
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.salary = "C"
        self.monthly_salary = int(monthly_salary)
        self.commission = int(commission)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input('Please enter monthly salary:'))
            self.commission = int(input('Please enter commission:'))
        except:
            self.monthly_salary = 0
            self.commission = 0

    def calculate_salary(self):
        return self.monthly_salary + self.commission


employees = []
id = 1


def salary():
    global id
    while True:
        salarytype = int(input('Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n'))
        if salarytype == 1:
            employee = SalaryEmployee(id, '', 0)
            SalaryEmployee.ask_name(employee)
            SalaryEmployee.ask_salary(employee)
            employees.append(employee)
            id += 1
        elif salarytype == 2:
            employee = HourlyEmployee(id, '', 0, 0)
            HourlyEmployee.ask_name(employee)
            HourlyEmployee.ask_salary(employee)
            employees.append(employee)
            id += 1
        elif salarytype == 3:
            employee = CommissionEmployee(id, '', 0, 0)
            CommissionEmployee.ask_name(employee)
            CommissionEmployee.ask_salary(employee)
            employees.append(employee)
            id += 1
        elif salarytype == 0:
            break
        else:
            print('Invalid input')


def read():  # Read from file
    list = ''
    try:
        with open("employee.csv", "r") as f:
            read_list = f.read()
            list += read_list
    except:
        print('error to read')

    count = 0
    y = ''
    if list != "":
        for x in list:
            y += x
            #print(y)
            if x == '\n':
                if y != '':
                    #print(y)
                    y = ''
                    count += 1
        print(str(count) + '  employee(s) read from employee.csv')
    '''
    try add data in list but task in 'metropolia' don't need it, so i comment it
    # clear data
    read_list = read_list.replace('[', '')
    read_list = read_list.replace(']', '')
    read_list = read_list.replace("'", '')
    read_list = read_list.split(', ')  # Split data
    #output number of employees
    count = 0
    for i in range(len(read_list)):
        count += 1
    print(read_list[count-1][0] + "  employee(s) read from employee.csv")

'''
def write(employees):
    count_of_employee = 0
    write_list = ''  # Create list for write to file
    for employee in employees:  # Loop for employees
        if employee.salary == "M":
            x = str(employee.id) + ',' + str(employee.name) + ',' + str(employee.salary) + ',' + str(employee.calculate_salary())
            write_list += x + '\n'
            count_of_employee += 1
        elif employee.salary == "H":
            x = str(employee.id) + ',' + str(employee.name) + ',' + str(employee.salary) + ',' + str(employee.hours_worked) + ',' + str(employee.hour_rate)
            write_list += x + '\n'
            count_of_employee += 1
        elif employee.salary == "C":
            x = str(employee.id) + ',' + str(employee.name) + ',' + str(employee.salary) + ',' + str(employee.monthly_salary) + ',' + str(employee.commission)
            write_list += x + '\n'
            count_of_employee += 1
        # Convert to string for write to file

    try:
        print(str(count_of_employee) + '  employee(s) added to employee.csv')  # Print number of employees added
        with open("employee.csv", "w+") as f:  # Open file and write to file
            f.write(str(write_list))  # Write to file
    except:  # If error
        print('error to write')  # Print error


while True:  # Loop for menu
    user_input = int(input(
        '(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print payroll\n(0) Quit\n\nPlease select one: '))
    if user_input == 1:
        salary()
    elif user_input == 2:
        write(employees)
    elif user_input == 3:
        read()
    elif user_input == 4:
        payroll_system = PayrollSystem()
        payroll_system.calculate_payroll(employees)
    elif user_input == 0:
        print('Service shutting down, thank you.')
        break
