from inventory import products, get_product_stock
from inventory import BankAccount

from fastapi import FastAPI


second_account = BankAccount("Saad", 100)
second_account.get_balance()




# def display_products():
#     for product in products:
#         print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}, "
#               f"Quantity: {product['quantity']}, Category: {product['category']}, On Sale: {product['onSale']}")


# print("Welcome to Imtiaz Inventoy")
# display_products()








