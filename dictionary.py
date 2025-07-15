employees = {"chef": "Amy", "ceo": "Jason"}
print(employees["ceo"])

# ADDING NEW ITEM
employees["Waiter"] = "Mike" # ALSO employees.update({"Waiter":"Mike"})
print(employees)

# UPDATING ITEM
print(employees)
print(employees["chef"])
employees["chef"] = "Jose"
print(employees)
print(employees["chef"].upper())


stock_prices = {"GOOGL": [100, 200, 300, 400], "GME": [20, 100, 90, 50]}
history = stock_prices["GOOGL"]
print(history)

# print(f"First day GOOGL Price : {history[0]} Second day GOOGL Price : {history[1]} Third day GOOGL Price : {history[2]} Fourth day GOOGL Price : {history[3]}")

# print(f"First day GOOGL Price : {history[0]}")
# print(f"Second day GOOGL Price : {history[1]}")
# print(f"Third day GOOGL Price : {history[2]}")
print(
    f"First day GOOGL Price : {history[0]}, Second day GOOGL Price : {history[1]}, Third day GOOGL Price : {history[2]}, Fourth day GOOGL Price : {history[3]}"
)

# NESTED DICTIONARY
nested_dictionary = {"GOOGL": {"first": 100, "second": 200, "third": 300, "fourth": 400}, "GME": {"first": 20, "second": 100, "third": 90, "fourth": 50}}
print(nested_dictionary)
print(nested_dictionary.keys())
print(nested_dictionary.values())
print(nested_dictionary.items())

# ACCESSING NESTED DICTIONARY
print(nested_dictionary["GOOGL"]["first"])
print(nested_dictionary["GME"]["first"])


