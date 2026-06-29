#!/usr/bin/env python3

from __init__ import CONN, CURSOR

from orm_db import Department, Employee

import ipdb
Employee.drop_table()
Department.drop_table()
Department.create_table()
Employee.create_table()

payroll = Department.create("Payroll", "West Wing, 5th Floor")
# print(payroll)

quality_assurance = Department.create("Quality Assurance", "East Wing, 4th Floor")
# print(quality_assurance)

hr = Department.create("Human Resources", "West Egg, Building C")
# print(hr)

hr.name = "HR"
hr.location = "East Egg, Building 4"
hr.update()
# print(hr)

cleric = Department.create("Clerics", "West Egg, 4th Floor")
# print(cleric)

# print("Deleting Clerics")
cleric.delete()
# print(cleric)

###################################################################

Employee.create("Amir", "Accountant", payroll.id)
Employee.create("Bola", "Manager", payroll.id)
Employee.create("Charlie", "Manager", hr.id)
Employee.create("Dani", "Benefits Coordinator", hr.id)
Employee.create("Hao", "New Hires Coordinator", hr.id)
Employee.create("Slayer", "New Hires Coordinator", quality_assurance.id)
Employee.create("FullEight", "Clerical Work", quality_assurance.id)
Employee.create("Boogeyman", "Accoutant", quality_assurance.id)
Employee.create("Slim Shady", "Events Manager", quality_assurance.id)
Employee.create("Kendrick Lamar", "Head", quality_assurance.id)



ipdb.set_trace()

