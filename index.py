class User:
    def __init__(self, name):
        print("User__init__ name called")
        self.name = name
    def log_in(self):
        self.logged_in = True

class Student(User):
    def __init__(self, name, grade):
        print("super().__init__(name) called")
        super().__init__(name)
        self.grade = grade
    def log_in(self):
        super().log_in()
        self.in_class = True

oneil = Student()
print(oneil)