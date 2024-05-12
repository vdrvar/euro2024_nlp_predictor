import requests
import re
import urllib.request
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from collections import deque
import os
import shutil
import time

from crawler import crawl

configs = [
    {"domain": "fourfourtwo.com", "url": "https://www.fourfourtwo.com/euro-2024", "max_depth": 1, "filter_path": None},
    {"domain": "marca.com", "url": "https://www.marca.com/futbol/eurocopa.html?intcmp=MENUMIGA&s_kw=euro-2024", "max_depth": 1, "filter_path": "eurocopa"},
    {"domain": "kicker.de", "url": "https://www.kicker.de/em/startseite", "max_depth": 1, "filter_path": "em"},
    {"domain": "gazzetta.it", "url": "https://www.gazzetta.it/Calcio/Europei/?refresh_ce", "max_depth": 1, "filter_path": "Calcio"},
    {"domain": "lequipe.fr", "url": "https://www.lequipe.fr/Football/Euro/", "max_depth": 1, "filter_path": "/Football/"}  # Added configuration for L'Équipe
]

def clear_directory(path):
    """ Clear all files and folders in the specified directory """
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

def start_crawling(configs):
    # Clear the raw data directory before starting the crawl
    raw_data_path = "../../data/raw"
    clear_directory(raw_data_path)
    print(f"Contents of {raw_data_path} have been cleared.")

    print("Crawling the predefined football magazines...")
    start_time = time.time()  # Start timing the crawling process

    for config in configs:
        site_start_time = time.time()  # Start time for this particular site
        print(f"Starting crawl for {config['domain']} at {config['url']}")

        crawl(config['url'], config['domain'], config['max_depth'], config['filter_path'])

        site_elapsed_time = time.time() - site_start_time
        print(f"Finished crawling {config['domain']} in {site_elapsed_time:.2f} seconds.")

    total_elapsed_time = time.time() - start_time  # Total time for all crawls
    print(f"Total crawling completed in {total_elapsed_time:.2f} seconds.")

# Call the function to start crawling all configured magazines
start_crawling(configs)
