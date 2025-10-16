
# dictionary
# key-value pairs in curly braces {}
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
print(type(my_dict))
print(len(my_dict))
print(my_dict["name"])  # Access value by key
print(my_dict.get("age"))  # Access value by key using get method
print(my_dict.get("country", "USA"))  # Access with default value if key not found
my_dict["age"] = 31  # Update value
print(my_dict)
my_dict["country"] = "USA"  # Add new key-value pair
print(my_dict)
