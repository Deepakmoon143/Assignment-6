import json


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state


employee_data = []
with open('employee.json', 'r') as file:
    data = json.load(file)
    for item in data:
        employee = Employee(item['Name'], item['DOB'], item['Height'], item['City'], item['State'])
        employee_data.append(employee)


for employee in employee_data:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
