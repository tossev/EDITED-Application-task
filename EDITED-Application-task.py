import asyncio
from pyppeteer import launch
import json

async def collect_data():
    # launch browser
    browser = await launch()
    
    # create a new page
    page = await browser.newPage()
    
    # request to load the page
    await page.goto('https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99')
    
    # wait for the last element in our search query to load
    await page.waitFor('.selector-list')    
    
    # collect data
    name = await page.Jeval('.product-name','node => node.textContent')
    price = await page.Jeval('.product-prices', 'node => node.children[1].getAttribute("content")')
    color = await page.Jeval('.colors-info-name', 'node => node.textContent')
    size = await page.Jeval('.selector-list', 'node => [...node.children].map(n => n.dataset.size)')
    
    # export data.json file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump({
            'name': name,
            'price': float(price),
            'color': color,
            'size': size
        }, f, indent=4)
    
asyncio.new_event_loop().run_until_complete(collect_data())
