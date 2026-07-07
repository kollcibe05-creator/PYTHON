from sqlalchemy import (create_engine, desc, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint, Index, DateTime, Integer, String, Column, func)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Many to many with table objects
game_user = Table(
    "game_users", 
    Base.metadata,
    Column("game_id", ForeignKey("games.id", primary_key=True)),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    extend_existing=True  # Overwrites the table object instead of throwing errors. That is also for the case of overlapping relationships
)


class Game(Base):
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    # With table objects
    users = relationship("User", secondary=game_user, back_populates="games")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f"User(id={self.id}, " + \
        f"name={self.name}"

    reviews = relationship("Review", backref=backref("user"))

    # With table objects
    games = relationship("Game", secondary=game_user, back_populates="users")
    

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey("games.id"))
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())
    user_id = Column(Integer(), ForeignKey("users.id"))

class GameUser(Base):
    __tablename__ = "game_users"

    id = Column(Integer(), primary_key=True)
    game_id = Column(Integer(), ForeignKey('games.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))

    game = relationship("Game", backref=backref("game_users"))
    user = relationship("User", back_populates="game_users")

    def __repr__(self):
        return f'GameUser(game_id={self.game_id}, ' + \
            f'user_id={self.user_id})'

