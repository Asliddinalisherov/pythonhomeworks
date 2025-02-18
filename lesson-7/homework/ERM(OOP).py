class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'


class EmployeeManager:
    def __init__(self):
        self.employee_ids = []
        print("""Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")

    def add_employee(self):
        eid = int(input("Enter ID: "))
        if eid in self.employee_ids:
            print("Employee with this ID already exists!")
        else:
            self.employee_ids.append(eid)
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = int(input("Enter salary: "))
            new_employee = Employee(eid, name, position, salary)
            with open('employee.txt', 'a') as f:
                f.write(new_employee.get_info() + '\n')
                print('Employee added successfully!')

    def view_employee(self):
        try:
            with open('employee.txt', 'r') as f:
                lines = f.readlines()
                if not lines:
                    print("No employee records found.")
                else:
                    for line in lines:
                        print(line, end='')
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self):
        employee_id = input("Enter ID: ")
        try:
            with open('employee.txt', 'r') as f:
                lines = f.readlines()
                found = False
                for line in lines:
                    if line.split(", ")[0] == employee_id:
                        print(line, end="")
                        found = True
                        break
                if not found:
                    print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID: ")
        try:
            with open('employee.txt', 'r') as f:
                lines = f.readlines()
            found = False
            updated_lines = []
            for line in lines:
                if line.split(", ")[0] == employee_id:
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    salary = input("Enter new salary: ")
                    updated_line = f"{employee_id}, {name}, {position}, {salary}\n"
                    updated_lines.append(updated_line)
                    found = True
                    print("Employee updated successfully!")
                else:
                    updated_lines.append(line)
            if not found:
                print("Employee not found.")
            with open('employee.txt', 'w') as f:
                f.writelines(updated_lines)
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self):
        employee_id = input("Enter ID: ")
        try:
            with open('employee.txt', 'r') as f:
                lines = f.readlines()
            found = False
            updated_lines = []
            for line in lines:
                if line.split(", ")[0] != employee_id:
                    updated_lines.append(line)
                else:
                    found = True
            if not found:
                print("Employee not found.")
            else:
                with open('employee.txt', 'w') as f:
                    f.writelines(updated_lines)
                print("Employee deleted successfully!")
        except FileNotFoundError:
            print("No employee records found.")



manager = EmployeeManager()
while True:
    choice = input('Enter your choice (1-6): ')
    if choice == '1':
        manager.add_employee()
    elif choice == '2':
        manager.view_employee()
    elif choice == '3':
        manager.search_employee()
    elif choice == '4':
        manager.update_employee()
    elif choice == '5':
        manager.delete_employee()
    elif choice == '6':
        print("Good bye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")