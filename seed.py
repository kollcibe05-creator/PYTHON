from faker import Faker
import random

from models.department import Department
from models.employee import Employee
from models.config import session

fake = Faker()


def seed_database():
    Department.create_department(name="Human Resources", location="West Wing")
    Department.create_department(name="Information Technology", location="East Wing")
    Department.create_department(name="Quality Assurance", location="South Wing")
    Department.create_department(name="Accounts", location="North Wing")
    Department.create_department(name="Clerics", location="East Egg")

    employees = [
        Employee(
            name=fake.name(), job_title=fake.job(), department_id=random.randint(1, 5)
        ) 
        for _5 in range (1, 25)
    ] 
    session.bulk_save_objects(employees)
    session.commit()

