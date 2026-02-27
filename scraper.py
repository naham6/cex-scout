import random
import requests
import time

class MarketScraper:#handling web scraping and API requests for centralized exchanges
    
    def __init__(self):
        #this would let the bot look like a real human using a web browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept': 'application/json'
        }
        
        
        self.proxies = [
            'http://10.0.0.1:8080',
            'http://10.0.0.2:8080',
            'http://10.0.0.3:8080'
        ]#dummy IPs.not recommended in a real scenario.paid ones are better.

    def _get_random_proxy(self):
        proxy_ip = random.choice(self.proxies)
        return {"http": proxy_ip, "https": proxy_ip}

    def fetch_data(self, url):
        proxy = self._get_random_proxy()
        print(f"fetching data from {url}")
        print(f"proxy selected: {proxy['http']}")
        
        try:
            time.sleep(random.uniform(1.0, 3.0)) #sleep to avoid rate limits
            response = requests.get(url, headers=self.headers, timeout=10)#wait for 10 seconds max.
            response.raise_for_status() 
            
            print("Live data fetched successfully\n")
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None