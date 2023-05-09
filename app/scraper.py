from bs4 import BeautifulSoup
import requests
import aiohttp
from datetime import datetime


async def get_card_info(item_art):
    try:
        url = f'https://www.oreht.ru/modules.php?name=orehtPriceLS&op=ShowInfo&code={item_art}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'referer': url
        }
        data = {'inn': '583413946400', 'pass': 'Alcatel199'}
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, headers=headers, data=data) as resp:
                src = await resp.text()
        soup = BeautifulSoup(src, 'lxml')
        stock_balance = soup.find(class_='mg-is-k').text
        try:
            price = soup.find(class_='mg-price').text.replace(',', '.').replace('\n', '')
            price = float(price)
        except:
            price = None
        return stock_balance, price
    except:
        return False


