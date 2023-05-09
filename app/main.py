import asyncio
import time
from app import db, scraper


def main():
    item_list = db.get_all_articles()
    for item in item_list:
        response = await scraper.get_card_info(item)


if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except Exception as ex:
            time.sleep(15)
            print(f"Running again after {ex}!")
