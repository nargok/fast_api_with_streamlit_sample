from fastapi import FastAPI, Depends
from sqlalchemy import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

# Databaseの作成
models.Base.metadata.create_all(bind=engine)

from sql_app.models import Booking, Room, User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get('/')
# async def index():
#     return 'Success!'

@app.get('/users', response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get('/rooms', response_model=List[schemas.Room])
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get('/bookings', response_model=List[schemas.Booking])
async def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

@app.post('/users')
async def users(users: User):
    return users

@app.post('/rooms')
async def rooms(rooms: Room):
    return rooms

@app.post('/bookings')
async def bookings(bookings: Booking):
    return bookings
