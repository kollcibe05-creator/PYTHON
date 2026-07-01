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