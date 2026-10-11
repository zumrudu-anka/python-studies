# 🐍 Selenium Studies

## Prerequisites

- Install required web driver you want:

|Type|Link|
|:--|:--|
|Chrome|[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)|
|Edge|[https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)|
|Firefox|[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)|
|Safari|[https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)|

**Note:** Firefox web driver have been used for this repository

## Installation

- run `git clone https://github.com/zumrudu-anka/python-selenium-studies.git` to download this repository
- run `python -m venv venv` to create virtual environment
- run `venv\Scripts\active` to activate it
- run `pip install -r requirements.txt` to install all dependencies

## Usage

- Create `.env` file and set your twitter username and password as environment variables **OR** set `TWITTER_USERNAME` and `TWITTER_PASSWORD` variables in `join_twitter.py`
- run `python join_twitter.py` to login your twitter account.
