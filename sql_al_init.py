
from sqlalchemy import create_engine


if __name__ = "__main__":
    engine = create_engine('sqlite:///students.db') # /// ~ Conection URL/URI
    Base.metadata.create_all(engine)