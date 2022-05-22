from fastapi import FastAPI
import json

from sql_app.models import Booking, Room, User

app = FastAPI()

@app.get('/')
async def index():
    return 'Success!'

@app.post('/users')
async def users(users: User):
    return users

@app.post('/rooms')
async def rooms(rooms: Room):
    return rooms

@app.post('/bookings')
async def bookings(bookings: Booking):
    return bookings
