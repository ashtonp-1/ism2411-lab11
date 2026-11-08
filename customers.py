
import email
from os import name


print("Reflection:")

#1.

#2.

print("Exercise 1:")

#Customer dictionary

customer = {
    "name:": "bob",
    "email:": "bob@gmail.com",
    "tier:": "gold",
    "ytd_spent:": 3200,
}

#Print induvidual results

print(customer["name:"])
print(customer["email:"])
print(customer["tier:"])
print(customer["ytd_spent:"])

print(customer)

print("Exercise 2:")

customer["phone:"] = "555-555-5555"
print(customer)

customer["tier:"] = "platinum"
print(customer)

del customer["email:"]
print(customer)

print("Exercise 3:")

print(customer.get("email:", "no email on file"))

try:
    print(customer["email:"])
except KeyError:
    print("KeyError: email does not exist")



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
discount_rate = tier_discounts.get(customer['tier:'], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier:']}, Discount Rate: {discount_rate}, Final Price: {final_price}")

print("Exercise 6:")
customer = [
    {"name": "bob", "tier": "gold", "ytd_spent": 3200},
    {"name": "alice", "tier": "silver", "ytd_spent": 1500},
    {"name": "charlie", "tier": "bronze", "ytd_spent": 800},
]


print("Exercise 7:")
catalog = {
    "widget A": {"price": 9.99, "stock": 150},
    "gadget C": {"price": 49.99, "stock": 8}
}
for product_name, product_details in catalog.items():
    if product_details["stock"] < 10:
        print(f"LOW STOCK: {product_name} - Only {product_details['stock']} left in stock!")

print("Exercise 8:")
transactions = [
    {"region": "south", "amount": 300},
    {"region": "north", "amount": 150},
    {"region": "south", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region.keys()):
    print(f"{region}: ${sales_by_region[region]:.2f}")