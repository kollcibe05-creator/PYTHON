from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye✌️")
    exit()

def list_departments():
    departments = Department.list_departments()
    for department in departments:
        print(department)
        

def find_department_by_name():
    name = input("Enter the department's name: ")
    dept = Department.find_department_by_name(name)
    print(dept) if dept else print(
        f"Department {name} not found"
    )

def find_department_by_id():
    id = input("Enter the department's id: ")
    dept = Department.find_department_by_id(id)
    print(dept) if dept else print(
        f"Department with id {id} not found"
    )

def create_department():
    name = input("Enter the name: ")
    location = input("Enter the location: ")
    try:
        department = Department.create_department(name, location)
        print(f"Success: {department}")
    except Exception as exc:
        print(f"ErrOR: {exc}")

def update_department():
    id = input("Enter the department's id: ")
    dept = Department.find_department_by_id(id)
    if dept:
        try:
            name = input("Enter the department's name: ")
            location = input("Enter the department's location: ")
            Department.update_department(name=name, location=location)
            department = Department.find_by_id(id)
            print(f"Department updated successfully! {department}")

        except Exception as exc:
            print(f"Err: {exc}")    

def delete_department():
    id = input("Enter the department's id: ")
    dept = Department.find_department_by_id(id)
    if department:
        Department.delete_department(id)
        print("Department deleted successfully")
    else:
        print(f"Department with id {id} not found")


def list_employees():
    employees = Employee.list_employees()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the Employee's name: ")
    emp = Employee.find_employee_by_name(name)
    print(emp) if emp else print(
        f"Employee {name} not found"
    )

def find_employee_by_id():  
    id = input("Enter the Employee's id: ")
    emp = Employee.find_employee_by_id(id)
    print(emp) if emp else print(
        f"Employee {id} not found"
    )

def create_employee():
    name = input("Enter the name: ")
    job_title = input("Enter the job title: ")
    department_id = input("Enter the department id: ")

    try:
        employee = Employee.create_employee(name,job_title, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"ErrOR: {exc}")


def update_employee(): 
    id = input("Enter the Employee's id: ")
    emp = Employee.find_employee_by_id(id)
    if emp:
        try:
            name = input("Enter the employee's name: ")
            job_title = input("Enter the employee's job title: ")
            department_id = input("Enter the employee's department id: ")

            Employee.update_employee(name=name, job_title=job_title, department_id=department_id)
            employee = employee.find_by_id(id)
            print(f"employee updated successfully! {employee}")

        except Exception as exc:
            print(f"Err: {exc}")    

def delete_employee():
    id = input("Enter the employee's id: ")
    emp = Employee.find_employee_by_id(id)
    if emp:
        Employee.delete_employee(id)
        print("Employee deleted successfully")
    else:
        print(f"Employee with id {id} not found")


def list_department_employees():
    id = input("Enter the department's id: ")
    dept = Department.find_department_by_id(id)
    if dept:
        for employee in dept.list_employees():
            print(employee)
    else:
        print(f"Department with id {id} not found.")

