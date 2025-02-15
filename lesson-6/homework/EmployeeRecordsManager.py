f = open("employees.txt", mode='w+')

while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    choice = int(input())

    if choice == 1:

        id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        pos = input("Enter employee position: ")
        salary = input("Enter employee salary: ")
        f.write(id + ", " + name + ", " + pos + ", " + salary + "\n")
    
    elif choice == 2:
        f.seek(0)
        print(f.read())

    elif choice == 3:
        id = input("Enter employee ID: ")
        f.seek(0)
        found = False
        for line in f.readlines():
            txt = line.split(", ")
            if id in txt:
                print(line)
                found = True
                break
        if found == False:
            print("Employe with this id does not exist!")
    
    elif choice == 4:
        id = input("Enter employee ID: ")
        f.seek(0)
        found = False
        lines = f.readlines()

        for i in range(len(lines)):
            if  lines[i].split(", ")[0] == id:
                name = input("Name: ")
                pos = input("position: ")
                salary = input("Salary: ")
                lines[i] = id + ", " + name + ", " + pos + ", " + salary + "\n"
                found = True
                break
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)
        if found == False:
            print("Employe with this id does not exist!")
        
    elif choice == 5:
        id = input("Enter employee ID: ")
        f.seek(0)
        found = False
        lines = f.readlines()

        for i in range(len(lines)):
            if  lines[i].split(", ")[0] == id:
                lines.pop(i)
                found = True
                break
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)
        if found == False:
            print("Employe with this id does not exist!")
    
    elif choice == 6:
        break
    else:
        print("choose between 1 and 6 (inclusive)")

f.close()
        
        

    

        

