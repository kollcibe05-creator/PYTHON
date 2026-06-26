# A walk-through before the world of SQLAlchemy

from __init__ import CONN, CURSOR 

# import sqlite3

# class Cat:
#     all = []

#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.add_cat_to_all(self)

#     @classmethod
#     def add_cat_to_all(cls, cat):
#         cls.append(cat)
    
#     def save(self, cursor):
#         cursor.execute(
#             'INSERT INTO cats (name, breed, age) VALUES (?, ?, ?)', 
#             (self.name, self.breed, self.age)
#         )

# db_connection = sqlite3.connect('db/my_database.db')
# db_cursor = db_connection.cursor()
# db_cursor.execute('CREATE TABLE IF NOT EXISTS cats (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER)')

# Cat("Mary", "Scottish", 4)
# Cat("Lucy", "German", 4)

# for cat in Cat.all:
#     cat.save(db.cursor)

class Department:
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name 
        self.location = location
    
    def __repr__(self):
        return f'<Department {self.id}: {self.name}, {self.location}>'

    @classmethod
    def create_table(cls):
        '''Create a new table to persist the attributes of Department instances'''
        sql = '''CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT, 
        location TEXT);
        '''
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        '''Drop table that persists the Department instances'''
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name and location values of the current Department instance and object id attribute using the primary key value of the new row""" 
        sql = """
        INSERT INTO departments (name, location)
        VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
    @classmethod
    def create(cls, name, location):
        """Initialize a new Department instance and save the object to the database"""
        department = cls(name, location)
        department.save()
        return department
    
    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
        UPDATE departments 
        SET name = ?, location = ? 
        WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit

    def delete(self):
        """Delete the table row corresponding to the current Department instance"""
        sql = """
        DELETE FROM departments
        WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,)) #The tuple comma, the gotcha!!!
        CONN.commit()