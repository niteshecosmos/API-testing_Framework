import pytest
from utils.api_client import APIClient


def test_status():
    """Status"""
    response = APIClient.get_status()
    assert response.status_code == 200
    print("status Response:", response.json())
    
def test_get_products():
    """Test fectching all products"""
    response = APIClient.get_products()
    assert response.status_code == 200
    assert len(response.json()) > 0
    print("Add to Cart Response:", response.json())




def test_get_product():
    """Test fetching a single product by ID"""
    product_id = "4643"
    response = APIClient.get_product(product_id)
    assert response.status_code == 200
    assert response.json()["id"] == int(product_id)
    print("Add to Cart Response:", response.json())




def test_add_to_cart():
    """Test adding a product to the cart"""
    product_id ="4643"
    response = APIClient.add_to_cart(product_id)
    assert response.status_code == 201
    assert "cartId" in response.json()
    print("Add to Cart Response:", response.json())




def test_get_cart():
    """Test fetching cart details"""
    product_id = "4643"
    
    add_response = APIClient.add_to_cart(product_id)
    print("Add to Cart Response:", add_response.json())  # Debugging output

    cart_id = add_response.json().get("cartId")  # Correct key name
    
    assert cart_id is not None, f"Cart ID is missing in response: {add_response.json()}"
    
    response = APIClient.get_cart(cart_id)
    assert response.status_code == 200
