import requests
import re
import urllib.request
from urllib.parse import urlparse, urljoin  # Ensure urljoin is also imported
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
import os

from crawler import crawl

configs = [
    {"domain": "fourfourtwo.com", "url": "https://www.fourfourtwo.com/euro-2024", "max_depth": 1, "filter_path": None},
    {"domain": "marca.com", "url": "https://www.marca.com/futbol/eurocopa.html?intcmp=MENUMIGA&s_kw=euro-2024", "max_depth": 1, "filter_path": None},
    {"domain": "kicker.de", "url": "https://www.kicker.de/em/startseite", "max_depth": 1, "filter_path": None},
    {"domain": "gazzetta.it", "url": "https://www.gazzetta.it/Calcio/Europei/?refresh_ce", "max_depth": 1, "filter_path": "Calcio/Europei"},
    {"domain": "lequipe.fr", "url": "https://www.lequipe.fr/Football/Euro/", "max_depth": 1, "filter_path": "/Football/"}  # Added configuration for L'Équipe
]

def start_crawling(configs):
    for config in configs:
        print(f"Starting crawl for {config['domain']} at {config['url']}")
        crawl(config['url'], config['domain'], config['max_depth'], config['filter_path'])

# Call the function to start crawling all configured magazines
start_crawling(configs)