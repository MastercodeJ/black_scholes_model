from model import Todo

# MongoDB driver
import motor.motor_asyncio

Client =  motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = Client.TodoList
collection = database.todo # Create a table 

async def fetch_one_todo(title):
    document = collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    docuement = todo
    result = await collection.insert_one(docuement)
    return docuement

async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set":{"description": desc}})
    document = await collection.find_one({"title": title})



