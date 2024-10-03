#!/usr/bin/env sh
pip install -q -r requirements.txt
pip install -q beautifulsoup4 pandas requests
pip install -q scrapy
pip freeze > requirements.txt