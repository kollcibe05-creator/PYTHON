from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///company.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
# if __name__ == "__main__":
#     engine = create_engine("sql:///Scompany.db")
#     Base.metadata.create_all(engine)

#     Session = sessionmaker(bind=engine)

#     session = Session()

def recreate_db():
    """Drops all of the tables and recreates them based on the new Base Metadata"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)