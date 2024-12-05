#!/usr/bin/env sh
pip install -q -r requirements.txt
pip install -q beautifulsoup4 pandas requests
pip install -q scrapy
pip install -q openai openai-whisper
pip install -q python-dotenv
pip install -q python-docx
pip freeze > requirements.txt
