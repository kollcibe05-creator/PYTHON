from sqlalchemy import (create_engine, Column, Integer, String, DateTime, func, ForeignKey)
from sqlalchemy.orm import relationship
from models.config import Base, session

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    job_title = Column(String())
    department_id = Column(Integer(), ForeignKey("departments.id"))

    department = relationship("Department", back_populates="employees")

    def __repr__(self):
        return f"Employee {self.id}, {self.name}, {self.job_title}, Dep Id: {self.id}"
    @classmethod
    def list_employees(cls):
        return session.query(cls).all()
    @classmethod
    def find_employee_by_name(cls, name):
        return session.query(cls).filter(cls.name == name).first()
    @classmethod
    def find_employee_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    @classmethod
    def create_employee(cls, name, job_title, department_id):
        employee = cls(name=name, job_title=job_title, department_id=department_id)
        session.add(employee)
        session.commit()
        return employee
    @classmethod
    def update_employee(cls, id, name=None, job_title=None, department_id=None):
        employee = cls.find_employee_by_id(id)

        if name is not None:
            employee.name = name
        if job_title is not None:
            employee.job_title = job_title
        if department_id is not None:
            employee.department_id = department_id
        session.commit()
        return employee
    @classmethod
    def delete_employee(cls, id):
        employee = cls.find_by_id(id)

        session.delete(employee)
        session.commit()