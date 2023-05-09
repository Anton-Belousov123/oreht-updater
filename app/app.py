import asyncio
import time
from app import db, scraper


async def cycle():
    print('yes')
    item_list = await db.get_item_list()
    print('yes2')
    print(item_list)
    exit(0)
    for item in item_list:
        response = await scraper.get_card_info(item)


def start_app():
    while True:
        try:
            asyncio.run(cycle())
        except Exception as ex:
            time.sleep(15)
            print(f"Running again after {ex}!")
