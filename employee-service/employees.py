class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

employees = [
    Employee(1, "John Doe", "Manager", 50000),
    Employee(2, "Jane Smith", "Cashier", 20000)
]

def get_all_employees():
    return [vars(emp) for emp in employees]

def add_employee(id, name, position, salary):
    new_employee = Employee(id, name, position, salary)
    employees.append(new_employee)
    return vars(new_employee)
