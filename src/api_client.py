import requests
import time
import logging
from typing import List, Dict
from .models import Customer

# Configure logging format and level
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomerAPIClient:
    """
    A client to interact with the Customer API.
    
    Attributes:
        base_url (str): The base URL of the API.
        api_key (str, optional): API key for authentication (if required).
    """
    
    def __init__(self, base_url: str, api_key: str = None):
        """
        Initialize the CustomerAPIClient with a base URL and optional API key.
        
        Args:
            base_url (str): The base URL of the API.
            api_key (str, optional): API key for authentication. Defaults to None.
        """
        self.base_url = base_url
        self.api_key = api_key

    def fetch_all_customers(self) -> List[Dict]:
        """
        Fetch all customers from the API, handling pagination automatically.
        
        Returns:
            List[Dict]: A list of customer records returned by the API.
        """
        all_customers = []  # List to store all fetched customer data
        page = 1  # Start fetching from page 1
        
        while True:
            try:
                response = self._fetch_page(page)  # Fetch data for the current page
                data = response.get("data", [])
                
                if not data:  # No more data returned; exit the loop
                    break
                
                all_customers.extend(data)  # Add the fetched data to the list
                
                # Stop if current page is the last page
                if page >= response.get("total_pages", page):
                    break
                
                page += 1  # Move to the next page
                
            except Exception as e:
                logging.error(f"Failed to fetch page {page}: {e}")
                break
        
        return all_customers

    def _fetch_page(self, page: int) -> Dict:
        """
        Fetch a single page of customers from the API with retry logic.
        
        Args:
            page (int): Page number to fetch.
        
        Returns:
            Dict: JSON response from the API containing customer data.
        
        Raises:
            Exception: If the page cannot be fetched after retries.
        """
        url = f"{self.base_url}/users?page={page}"
        retries = 3  # Number of retries in case of failure
        delay = 1  # Initial delay between retries in seconds
        
        for attempt in range(retries):
            try:
                resp = requests.get(url)
                
                if resp.status_code == 200:
                    logging.info(f"Fetched page {page} successfully")
                    return resp.json()
                
                elif resp.status_code == 429:  # Rate limited
                    logging.warning("Rate limited. Retrying...")
                    time.sleep(delay)
                
                else:
                    logging.error(f"Request failed: {resp.status_code}. Retrying...")
                    time.sleep(delay)
            
            except requests.RequestException as e:
                logging.error(f"Request error: {e}. Retrying...")
                time.sleep(delay)
            
            delay *= 2  # Exponential backoff for next retry
        
        raise Exception(f"Failed to fetch page {page} after {retries} retries")
