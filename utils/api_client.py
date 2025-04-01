import requests
from config import BASE_URL

class APIClient:
    @staticmethod
    def get_products():
        """Fetch all available products"""
        url =f"{BASE_URL}/products"
        response = requests.get(url)
        return response
    
    @staticmethod
    def get_product(product_id):
        """Fetch details of a specific product """
        url =f"{BASE_URL}/products/{product_id}"
        response = requests.get(url)
        return response
    
    @staticmethod
    def add_to_cart(product_id):
        """Add a product to the cart"""
        url = f"{BASE_URL}/carts"
        payload = {"productID": product_id, "qaunity": 1}
        response = requests.post(url,json = payload)
        return response

    @staticmethod
    def get_cart(cart_id):
        """Fetch Cart detials"""
        url = f"{BASE_URL}/carts/{cart_id}"
        response = requests.get(url)
        return response