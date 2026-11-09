
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
