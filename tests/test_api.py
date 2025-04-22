
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


def test_add_to_cart():
    """Test adding a product to the cart"""
    product_Id = 4646
    cartId = APIClient.add_to_cart(product_Id)
    assert cartId is not None
    print("Cart ID generated:",cartId)



def test_created_cart():
    product_Id = 4646
    """Test the created cart with item id"""
    cart_id = APIClient.add_to_cart(product_Id)
    assert cart_id is not None,"Cart ID should not be None"

    add_response = APIClient.add_to_item_the_cart(cart_id, product_Id)
    
    print("STATUS CODE:", add_response.status_code)
    print("RESPONSE BODY:", add_response.text)
    assert add_response.status_code == 201, "Failed to add item to cart"


    response = APIClient.created_cart(cart_id)
    assert response.status_code == 200,"Failed to fetch cart detials"
    print("Add the created cart id:",response.json())

    cart_data = response.json()
    print("cart content:", cart_data)

    assert any(item["productId"] == product_Id for item in cart_data.get("items", [])), "Product ID not found in cart items"




def test_add_item_to_cart():
    product_id = 4646
    """Test adding an item to an existing cart"""
    cart_id = APIClient.add_to_cart(product_id)
    assert cart_id is not None,"Cart ID should not be done"

    response = APIClient.add_to_item_the_cart(cart_id,product_id,quantity=1)
    assert response.status_code == 201, f"Failed to add item to cart: {response.status_code}, Response: {response.text}"
    print("Add the created item id:",response.json())




def test_get_product():
    """Test fetching a single product by ID"""
    product_id = "4643"
    response = APIClient.get_product(product_id)
    assert response.status_code == 200
    assert response.json()["id"] == int(product_id)
    print("Add to Cart Response:", response.json())


def test_update_item():
    """Test fecthing update the item"""
    product_Id =  4646
    
    #Step 1: Add product to cart 
    cart_id = APIClient.add_to_cart(product_Id)
    assert cart_id is not None,"Cart ID should not be None"
    print("Cart ID created:", cart_id)

    #Step 2: Add item to the cart
    add_response = APIClient.add_to_item_the_cart(cart_id, product_Id)
    assert add_response.status_code == 201
    response_data = add_response.json()
    print("Item added to cart response:",response_data)

    #Step 3:Extract item ID
    item_id = response_data.get("itemId")   
    assert item_id is not None,"Item ID should not be None"
    print("Extracted Item ID:", item_id)

    #Step 4: Update the item in cart
    updated_quantity = 3
    update_response = APIClient.update_item(cart_id, item_id,product_Id,updated_quantity)
    assert update_response.status_code in [200, 204], f"Unexpected status: {update_response.status_code}"
    print("Status Code:", update_response.status_code)

    #Step 5 Get the update Item
    response = APIClient.created_cart(cart_id)
    assert response.status_code == 200,"Failed to fetch cart detials"
    print("Add the created cart id:",response.json())

def test_delete_item():
    """Test fetching delete item""" 
    product_id = "1225"

    #Step 1 Add product to cart
    cart_id = APIClient.add_to_cart(product_id)
    assert cart_id is not None,"Cart ID should not be None"
    print("Cart ID created:",cart_id)

    #Step 2 Add item to the cart
    add_response = APIClient.add_to_item_the_cart(cart_id,product_id)
    assert add_response.status_code == 201
    response_data = add_response.json()
    print("Item added to cart response:",response_data)

    #Step3 :Extract item ID
    item_id =response_data.get("itemId")
    assert item_id is not None,"Item ID should not be None"
    print("Extracted Item ID:", item_id)

    #Step4 : Update the item in cart 
    updated_quantity = 4
    update_response = APIClient.update_item(cart_id,item_id,product_id,updated_quantity)
    assert update_response.status_code in [200,204], f"Unexcepted status:{update_response.status_code}"
    print("Status Code:", update_response.status_code)

    # Step 5: Delete the item from the cart
    delete_response = APIClient.delete_item(cart_id, item_id)
    assert delete_response.status_code in [200, 204], f"Unexpected delete status: {delete_response.status_code}"
    print("✅ Item deleted successfully. Status:", delete_response.status_code)
