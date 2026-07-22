from datetime import datetime
from sqlalchemy import (create_engine, desc, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint, Index, DateTime, Integer, String, Column, func)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, relationship 


Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id", 
            name="id_pk"
        ),
        UniqueConstraint(
            "email",
           name="unique_email"
        ), 
        CheckConstraint(
            "grade BETWEEN 1 AND 12", 
            "grade_between_1_and_12"
        )
    )

    Index("index_name", "name")

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())
    def __repr__(self):
        return f"Student {self.id}: "\
            + f"{self.name}, "\
            + f"Grade {self.grade}"
    def create_table(Base, engine):
        Base.metadata.create_all(engine)

    def save(session, student):
        session.add(student)
        session.commit()

    def get_all(session):
        return [student for student in session.query(Student)]
    def find_by_name(session, name):
        return [student for student in session.query(Student).filter(Student.name == name)]
    def find_by_name_and_id(session, name, id):
        return [student for student in session.query(Student).filter(Student.name == name, Student.id == id)]
    def update_grade(session, student, grade):
        student.grade = grade
        session.commit()
    
    



if __name__ == "__main__":
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    # albert_einstein = Student(
    #     name="Albert Einstein",
    #     email = "albert2.com",
    #     grade=6,
    #     birthday=datetime(
    #         year=1879,
    #         month=3,
    #         day=14
    #     ),
    # )

    # alan_turing = Student(
    #     name="Alan Turing",
    #     email="alan.turing@sherborne.edu",
    #     grade=11,
    #     birthday=datetime(
    #         year=1912,
    #         month=6,
    #         day=23
    #     ),
    # )


    # session.bulk_save_objects([albert_einstein, alan_turing])
    # session.commit()

    # print(albert_einstein.id)
    # print(alan_turing.id)

    students = session.query(Student).all()
    # print([student for student in students])
    student_count = session.query(func.count(Student.id)).first()
    # print([student for student in session.query(Student.name, Student.grade).order_by(desc(Student.grade)).first()])
    print(student_count)
    query = session.query(Student).filter(Student.name.like('%Alan%'), Student.grade == 11)

    for record in query:
        print(record.name)