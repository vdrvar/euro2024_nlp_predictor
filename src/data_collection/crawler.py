import requests
import re
import urllib.request
from urllib.parse import urlparse, urljoin  # Ensure urljoin is also imported
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
import os

# Regex pattern to match a URL
HTTP_URL_PATTERN = r'^http[s]*://.+'

# Create a class to parse the HTML and get the hyperlinks
class HyperlinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hyperlinks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])

def get_hyperlinks(url):
    """Fetch and parse hyperlinks from the given URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {str(e)}")
        return []

def get_domain_hyperlinks(base_url, url, filter_path=None):
    """Filter and clean links to ensure they belong only to the specified domain and optional path segment."""
    hyperlinks = get_hyperlinks(url)
    domain_links = []
    for link in hyperlinks:
        if link.startswith('/'):
            link = urljoin(base_url, link)
        elif not link.startswith('http'):
            continue
        parsed_link = urlparse(link)
        parsed_base = urlparse(base_url)
        if parsed_link.netloc == parsed_base.netloc:
            if filter_path is None or filter_path in parsed_link.path:
                domain_links.append(link)
    return list(set(domain_links))

def crawl(start_url, local_domain, max_depth, filter_path=None):
    queue = deque([(start_url, 0)])  # Initialize queue with (url, depth)
    seen = set([start_url])
    data_dir = "../../data/raw/" + local_domain.replace('.', '_') + "/"  # Adjusted directory path

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    while queue:
        url, depth = queue.popleft()
        if depth > max_depth:
            continue  # Skip processing if depth exceeds the max_depth
        print(f"Crawling: {url} at depth {depth}")

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()

            file_path = os.path.join(data_dir, f"{urlparse(url).path.strip('/').replace('/', '_').replace(':', '_')}.txt")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)

            if depth < max_depth:
                for link in get_domain_hyperlinks(start_url, url, filter_path):
                    if link not in seen:
                        queue.append((link, depth + 1))
                        seen.add(link)

        except requests.RequestException as e:
            print(f"Error accessing {url}: {str(e)}")