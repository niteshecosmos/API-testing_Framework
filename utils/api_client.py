import requests
from config import BASE_URL

class APIClient:
    @staticmethod

    def get_status():
        """Status the Endpoint"""
        url = f"{BASE_URL}/status"
        response = requests.get(url)
        return response

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
        payload = {
            "productId": product_id, 
            "quantity": 1
        }
        response = requests.post(url,json = payload)
        if response.status_code == 201:
            return response.json().get("cartId")
        return None
    
    @staticmethod
    def add_to_item_the_cart(cart_id, product_id, quantity=1):
        """Add the item in the cart"""
        url = f"{BASE_URL}/carts/{cart_id}/items"
        payload = {
            "productId": int(product_id), 
            "quantity": quantity
        }
        print("🔍 Sending Payload:", payload)   
        response = requests.post(url, json=payload)
        return response


    @staticmethod
    def created_cart(cartId):
        """Created Cart item id"""
        url = f"{BASE_URL}/carts/{cartId}"
        response = requests.get(url)
        return response

    @staticmethod
    def get_cart(cart_id):
        """Fetch Cart detials"""
        url = f"{BASE_URL}/carts/{cart_id}"
        response = requests.get(url)
        return response
    
    @staticmethod
    def update_item(cartId,itemId,product_id,quantity):
        """Update the item"""
        url =f"{BASE_URL}/carts/{cartId}/items/{itemId}"
        payload = {
            "productID": product_id,
            "quantity" : quantity
        }
        print("PATCH URL:",url)
        print("Payload sent to update item:", payload)
        response = requests.patch(url, json=payload)
        return response

    @staticmethod
    def delete_item(cart_id, item_id):
        """Delete item from cart"""
        url = f"{BASE_URL}/carts/{cart_id}/items/{item_id}"
        print("🗑️ Sending DELETE request to:", url)
        response = requests.delete(url)
        return response
