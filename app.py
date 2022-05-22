import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Booking(BaseModel):
    booking_id: int
    room_id: int
    user_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class User(BaseModel):
    user_id: int
    username: str = Field(max_length=12)

class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)

app = FastAPI()

@app.get('/')
async def index():
    return 'Success!'

@app.post('/users')
async def users(users: User):
    return f'users: {users}'

@app.post('/rooms')
async def rooms(rooms: Room):
    return f'rooms: {rooms}'

@app.post('/bookings')
async def bookings(bookings: Booking):
    return f'bookings: {bookings}'