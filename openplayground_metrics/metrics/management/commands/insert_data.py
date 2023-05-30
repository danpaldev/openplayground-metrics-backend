import os
import asyncio
import motor.motor_asyncio
from dotenv import load_dotenv
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Inserts data into MongoDB'

    async def do_db_insert(self):
        load_dotenv()

        mongo_user = os.getenv("MONGO_USER")
        mongo_password = os.getenv("MONGO_PASSWORD")
        mongo_host = os.getenv("MONGO_HOST")
        mongo_port = os.getenv("MONGO_PORT")
        mongo_db = os.getenv("MONGO_DB")

        client = motor.motor_asyncio.AsyncIOMotorClient(
            f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/')
        db = client[mongo_db]
        collection = db.open_ai

        document = {"name": "Example",
                    "description": "Example Description"}
        result = await collection.insert_one(document)
        return result.inserted_id

    def handle(self, *args, **kwargs):
        new_doc_id = asyncio.run(self.do_db_insert())
        self.stdout.write(self.style.SUCCESS(
            f'Successfully inserted data into MongoDB! Document ID: {new_doc_id}'))
