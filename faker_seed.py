import random
from faker import Faker

from models import Game
session.query(Game).delete()
session.commit()

fake = Faker()

print("Seeding games...")

games = [Game(
    title=fake.name(), 
    genre=fake.word(),
    platform=fake.word(),
    price=random.randint(0, 60)
)
for i in range(50)]

session.bulk_save_objects(games)
session.commit()


# Hot tip on selecting random elements 
# Define your list of departments
departments = [
    "Human Resources",
    "Engineering",
    "Marketing",
    "Sales",
    "Finance",
    "Customer Support",
    "Research & Development"
]

# Generate employee data with a random department
employee = {
    "name": fake.name(),
    "job_title": fake.job(),
    "department": fake.random_element(elements=departments)
}
