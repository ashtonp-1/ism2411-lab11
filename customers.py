
from os import name


print("Reflection:")

#1.

#2.

print("Exercise 1:")
dict('name', )

print("Exercise 4:")

for key, value in customer.items():
    for something in customer:
        print(something, customer[something])

print("Exercise 5:")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

purchase = 200 
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}, Discount Rate: {discount_rate}, Final Price: {final_price}")

print("Exercise 6:")
customer = [
    {"name": "bob", "tier": "gold", "ytd_spent": 3200},
    {"name": "alice", "tier": "silver", "ytd_spent": 1500},
    {"name": "charlie", "tier": "bronze", "ytd_spent": 800},
]


print("Exercise 7:")
catalog = [
    "widget A": {"price": 9.99, "stock": 150},
    "gadget C": {"price": 49.99, "stock": 8}
]
for product_name, product_details in catalog.items():
    if product_details["stock"] < 10:
        print(f"LOW STOCK: {product_name} - Only {product_details['stock']} left in stock!")