from crawler import crawl

# Configuration for the Football section of L'Équipe
domain_to_crawl = "lequipe.fr"
start_url = "https://www.lequipe.fr/Football/"
segment_keyword = "/Football/"

crawl(start_url, domain_to_crawl, segment_keyword)