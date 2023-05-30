import os
import asyncio
import redis.asyncio as redis
from dotenv import load_dotenv

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Inserts data into Redis'

    async def do_redis_insert(self):
        load_dotenv()

        redis_password = os.getenv("REDIS_PASSWORD")
        redis_host = os.getenv("REDIS_HOST")
        redis_port = os.getenv("REDIS_PORT")

        r = redis.Redis(
            host=redis_host, port=redis_port, password=redis_password)

        await r.set('my_key', 'my_value', ex=60)

        value = await r.get('my_key')

        await r.close()

        return value

    def handle(self, *args, **kwargs):
        inserted_value = asyncio.run(self.do_redis_insert())
        self.stdout.write(self.style.SUCCESS(
            f'Successfully inserted data into Redis! Value: {inserted_value}'))
