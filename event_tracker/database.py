from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
client = None
db = None
async def init_db():
    global client, db
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client['event_db']
async def create_event(event_data):
    pass  # TODO
async def read_event(event_id):
    pass  # TODO
async def update_event(event_id, update_data):
    pass  # TODO
async def delete_event(event_id):
    pass  # TODO
