#!/usr/bin/env python3

from __init__ import CONN, CURSOR

from orm_db import Department

import ipdb
Department.drop_table()

Department.create_table()

payroll = Department.create("Payroll", "West Wing, 5th Floor")
print(payroll)

quality_assurance = Department.create("Quality Assurance", "East Wing, 4th Floor")
print(quality_assurance)

hr = Department.create("Human Resources", "West Egg, Building C")
print(hr)

hr.name = "HR"
hr.location = "East Egg, Building 4"
hr.update()
print(hr)

cleric = Department.create("Clerics", "West Egg, 4th Floor")
print(cleric)

print("Deleting Clerics")
cleric.delete()
# print(cleric)

ipdb.set_trace()

