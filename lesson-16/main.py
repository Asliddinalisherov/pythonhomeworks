import csv
with open('employee.csv', 'r') as file:
    reader = csv.reader(file)
    header = (next(reader))
    print(header)
    data = list(reader)
    print(data)