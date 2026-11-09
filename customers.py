
# ISM2411 Lab 11
# Name: Harsh Patel

# Reflection 1:
# I would use .get() when a key might not exist because it prevents the program from crashing. I would use brackets when I know the key exists and need its value.

# Reflection 2: This reminds me of using a PivotTable in Excel to total sales by region. Python can be more useful for large datasets because it can automatically summarize lots of information.


# Exercise 1
customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2

customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")



# Exercise 4

for key, value in customer.items():
    print(f"{key}: {value}")


for key in customer:
    print(key)


# Exercise 5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount)

print("Tier:", tier)
print("Discount:", f"{discount:.0%}")
print("Final price:", f"${final_price:.2f}")


# Exercise 6

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount
    print(f"{person['name']}: {tier}, discount ${discount_amount:.2f}")
