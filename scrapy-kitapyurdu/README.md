# 🐍 Scrapy - Kitap Yurdu

## Prerequisites

- run `Users\<Username>\anaconda3\Scripts\activate` to activate anaconda environment
- Select the interpreter
- run `scrapy startproject`
- add `FEED_EXPORT_ENCODING = "utf-8"` to settings.py (Optional)

## Usage

- run `scrapy crawl books -o books.json`

## Commands

- run `scrapy crawl books -O books.json` to export json file (overwrite)
- run `scrapy crawl books -o books.json` to export json file (append)
