from datetime import datetime

class Employee:
    employees = []
    counter = 1

    def __init__(self, emp_id, name, joining_date, salary):
        self.id = Employee.counter
        Employee.counter += 1

        self.emp_id = emp_id
        self.name = name
        self.joining_date = datetime.strptime(joining_date, "%Y-%m-%d")
        self.salary = salary

    @classmethod
    def create(cls, data):
        emp = Employee(
            data["emp_id"],
            data["name"],
            data["joining_date"],
            data["salary"]
        )
        cls.employees.append(emp)
        print("Employee added\n")

    @classmethod
    def update(cls, emp_id, data):
        for emp in cls.employees:
            if emp.emp_id == emp_id:

                if "name" in data:
                    emp.name = data["name"]

                if "joining_date" in data:
                    emp.joining_date = datetime.strptime(data["joining_date"], "%Y-%m-%d")

                if "salary" in data:
                    emp.salary = data["salary"]

                print("Employee updated\n")
                return

        print("Employee not found\n")

    @classmethod
    def delete(cls, emp_id):
        for emp in cls.employees:
            if emp.emp_id == emp_id:
                cls.employees.remove(emp)
                print("Employee deleted\n")
                return

        print("Employee not found\n")

    @classmethod
    def list_employees(cls):

        if len(cls.employees) == 0:
            print("No employees\n")
            return

        result = cls.employees

        choice = input("Search? (y/n): ")
        if choice == "y":
            term = input("Enter emp_id or name: ")
            temp = []
            for emp in result:
                if emp.emp_id == term or emp.name == term:
                    temp.append(emp)
            result = temp

        choice = input("Sort? (y/n): ")
        if choice == "y":
            key = input("Sort by (emp_id, name, joining_date, salary): ")

            if key == "emp_id":
                result.sort(key=lambda x: x.emp_id)
            elif key == "name":
                result.sort(key=lambda x: x.name)
            elif key == "joining_date":
                result.sort(key=lambda x: x.joining_date)
            elif key == "salary":
                result.sort(key=lambda x: x.salary)

        for emp in result:
            print("-----")
            print("ID:", emp.id)
            print("Emp ID:", emp.emp_id)
            print("Name:", emp.name)
            print("Date:", emp.joining_date.date())
            print("Salary:", emp.salary)

        print()



while True:
    print("1. Create")
    print("2. Update")
    print("3. Delete")
    print("4. List")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        emp_id = input("Emp ID: ")
        name = input("Name: ")
        date = input("Joining Date (YYYY-MM-DD): ")
        salary = float(input("Salary: "))

        Employee.create({
            "emp_id": emp_id,
            "name": name,
            "joining_date": date,
            "salary": salary
        })

    elif choice == "2":
        emp_id = input("Enter emp_id: ")

        data = {}

        name = input("New name (leave empty): ")
        if name != "":
            data["name"] = name

        date = input("New date (leave empty): ")
        if date != "":
            data["joining_date"] = date

        salary = input("New salary (leave empty): ")
        if salary != "":
            data["salary"] = float(salary)

        Employee.update(emp_id, data)

    elif choice == "3":
        emp_id = input("Enter emp_id: ")
        Employee.delete(emp_id)

    elif choice == "4":
        Employee.list_employees()

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice\n")