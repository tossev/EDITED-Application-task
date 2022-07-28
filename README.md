# EDITED-Application-task
The project is done by using [Pyppeteer.](https://github.com/pyppeteer/pyppeteer)

Python version = 3.10.5

## Task
- Request to load the page located at [this address.](https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99)

- Parse of the html.

- Collect the data (name, price, selected default color and size).

- Output the data as json file, for example:

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


## Flow chart of the programm

```mermaid
graph TD
A(launch browser) --> B(create a new page) --> C(request to load the page) --> D(wait for the last element in our search query to load) --> E(collect data) --> F(export data.json file)
