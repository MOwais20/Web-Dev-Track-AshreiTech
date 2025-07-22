
products = [
    {
        "id": "b7e23ec2-8c4a-4e2a-9f3e-1a2b3c4d5e6f",
        "name": "Laptop",
        "price": 999.99,
        "quantity": 50,
        "category": "Electronics",
        "onSale": True
    },
    {
        "id": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6",
        "name": "Smartphone",
        "price": 699.99,
        "quantity": 150,
        "category": "Electronics",
        "onSale": False
    },
    {
        "id": "f6e5d4c3-b2a1-0g9h-8i7j-k6l5m4n3o2p1",
        "name": "Desk Chair",
        "price": 89.99,
        "quantity": 200,
        "category": "Furniture",
        "onSale": True
    },
    {
        "id": "c3b2a1d0-e9f8-7g6h-5i4j-k3l2m1n0o9p8",
        "name": "Coffee Maker",
        "price": 49.99,
        "quantity": 75,
        "category": "Appliances",
        "onSale": False
    },
    {
        "id": "d4c3b2a1-e0f9-8g7h-6i5j-k4l3m2n1o0p9",
        "name": "Wireless Headphones",
        "price": 129.99,
        "quantity": 120,
        "category": "Electronics",
        "onSale": True
    }
]


# total_products = products.count()
# print(f"Total products in inventory: {total_products}")


def get_product_stock(product_id):
    for product in products:
        if product["id"] == product_id:
            return product["quantity"]
    return None


class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        self._account_type = "Savings"  # Protected attribute (convention)
        self.__balance = initial_balance  # Private attribute
    
    # Private method
    def __calculate_interest(self):
        return self.__balance * 0.03
    
    # Public methods to access/modify private data
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} rupees deposit ho gaye hain")
            return True
        else:
            print("Deposit amount positive hona chahiye")
            return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} rupees withdraw ho gaye hain")
            return True
        else:
            print("Invalid withdrawal amount ya insufficient balance")
            return False
    
    def get_balance(self):
        interest = self.__calculate_interest()
        print(f"Aapke account mein {self.__balance} rupees hain")
        print(f"Annual interest: {interest} rupees")
        return self.__balance

# # BankAccount object create karna
# account = BankAccount("Imran Khan", 5000)


# # Public method ke through private data access karna
# account.deposit(10000)# account.withdraw(1000)
# account.get_balance()

# # Direct access try karna
# print(f"Account holder (public): {account.account_holder}")
# print(f"Account type (protected): {account._account_type}")

# # Private attribute ko direct access karne ki koshish
# try:
#     print(account.__balance)  # Ye error dega
# except AttributeError as e:
#     print(f"Error: {e}")

# Name mangling ke baad private attribute access karna
# (Ye technical knowledge hai, generally avoid karna chahiye)
# print(f"Private balance (not recommended): {account._BankAccount__balance}")


# print("******\n*****")

# second_account = BankAccount("Ali", 100)

# second_account.get_balance()



