# EDITED-Application-task
The project is done by using [Pyppeteer.](https://github.com/pyppeteer/pyppeteer)

Python version = 3.10.5

## Task
- request to load the page located at [this address](https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99)

- parse of the html

- collect the data (name, price, selected default color and size)

- output the data as json file, for example:

		{

		"name": String

		"price": Double,

		"color": String,

		"size": Array

		}

## requirements.txt
Run `pip install -r requirements.txt` to install the required packages.

## EDITED-Application-task.py
- Open terminal window in the project's directory. 
- Run `python EDITED-Application-task.py`
- After completition 'data.json' file will appear in project's directory.


## Flow chart

```mermaid
graph TD
A(launch browser) --> B(create a new page) --> C(request to load the page) --> D(wait for the last element in our search query to load) --> E(collect data) --> F(export data.json file)
