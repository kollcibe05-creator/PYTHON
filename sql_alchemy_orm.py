
from sqlalchemy import (declarative_base, desc, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint, Index, DateTime, Integer, String)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    __table_args__ = (
        PrimaryKeyConstraint(
            "id", 
            name="id_pk"
        ),
        UniqueConstraint("email", 
            "email",
            "unique_email"
        ), 
        CheckConstraint(
            "grade BETWEEN 1 AND 12", 
            "grade_between_1_and_12"
        )
    ),

    Index("index_name", "name")

    id = Column(Integer())
    name = Column(String())
    email = Column(String())
    grade = Column(Integer())
    birthday = Column(DateTime())




if __name__ == "__main__":
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)