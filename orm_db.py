# A walk-through before the world of SQLAlchemy

from __init__ import CONN, CURSOR 

class Department:
    all = {}
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
        """Insert a new row with the name and location values of the current Department instance and object id attribute
        using the primary key value of the new row""" 
        sql = """
        INSERT INTO departments (name, location)
        VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid

        # Added to evaluate to the department class
        type(self).all[self.id] = self # type(self) resolves to the Class. it is safer to use than Class as it makes the code extensible and safe to inherit especially with the complexities along subclasess (result:Department.all = {1: <Department object at 0x1023>, 2: <Department object at 0x1054>}) Fetching: Department.all[1]. The data is later fetched from memory without need of a slow query
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
        """Delete the table row corresponding to the current Department instance, delete the dictionary entry, and reassign id attribute"""
        sql = """
        DELETE FROM departments
        WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,)) #The tuple comma, gotcha!!!
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
    @classmethod
    def instance_from_db(cls, row):
        """Return a Department object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary id
        department = cls.all.get(row[0])
        if department:
            # ensure attributes match the row values in case local objects was modified
            department.name = row[1]
            department.location = row[2]
        else:
            # not in the dictionary, create new instance and add to dictionary
            department = cls(row[1], row[2])
            department.id = row[0]
            cls.all[department.id] = department
            
        return department
    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table."""
        sql = '''
            SELECT * 
            FROM departments
        '''
        rows = CURSOR.execute(sql).fetchall() # we iterate over each to retrieve them as Python objects.
        return [cls.instance_from_db(row) for row in rows]
        # or return CURSOR.execute(sql).fetchall() if we are not interested in having them as Python Objects

    @classmethod
    def find_by_id(cls, id):
        '''Return a Department object corresponding to the table row matching the 
        specified primary key'''
        sql = """
            SELECT * FROM departments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_name(cls, name):
        """Return a Department object corresponding to first table row matching 
        specified name"""
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None







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

