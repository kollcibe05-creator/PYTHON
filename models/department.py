from sqlalchemy import (Column, Integer, String, DateTime, func)

from models.config import Base, session

from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())

    employees = relationship("Employee", back_populates="department")

    def __repr__(self):
        return f"<Department {self.id}, Name: {self.name}, Location: {self.location}>"
    @classmethod
    def list_departments(cls):
        return session.query(cls).all()
    def list_employees(self):
        return self.employees
    @classmethod
    def create_department(cls, name, location):
        department = cls(name=name, location=location)
        session.add(department)
        session.commit()
        return department
    @classmethod
    def find_department_by_name(cls, name):
        dep = session.query(cls).filter(cls.name == name).first()
        return dep
    @classmethod
    def find_department_by_id(cls, id):
        dep = session.query(cls).filter(cls.id == id).first()
        return dep
    @classmethod
    def update_department(cls, id, name=None, location=None):
        dept = cls.find_by_id(id)
        if name is not None:
            dept.name = name
        if location is not None:
            dept.location = location
        
        session.commit()
        return dept
    @classmethod
    def delete_department(cls, id):
        dept = dept.find_by_id(id)
        session.delete(dept)
        session.commit()
        return None
   



