from sqlalchemy.orm import Session

from models import *

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, username: str):
    return db.query(User).all()


def create_user(db: Session, user: User):
    db_user = User(username=user.username, password=user.password, type=user.type, gender=user.gender, age=user.age, preferences=user.preferences)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_movie(db: Session, title: str):
    return db.query(Movie).filter(Movie.title == title).first()

def get_movies(db: Session):
    return db.query(Movie).all()

def create_movie(db: Session, movie: Movie):
    db_movie = Movie(title=movie.title, genre=movie.genre, start_time=movie.start_time, end_time=movie.end_time, total_seats=movie.total_seats, booked_seats=movie.booked_seats, price_1_adult=movie.price_1_adult, price_1_child=movie.price_1_child, rating=movie.rating)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie