from toon_format import encode, decode


input_json_1 = {
    "title": "Shopping List",
    "items": ["apple", "banana", "carrot"],
    "quantity": [5, 3, 4],
}

# Encode Python dict to toon format
toon_str = encode(input_json_1)
print("Encoded toon format:")
print(toon_str)

# Tabular array (uniform objects)
input_json_2 = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
]
toon_str_2 = encode(input_json_2)
print("\nEncoded toon format for tabular array:")
print(toon_str_2)


#### Toon to JSON Examples ####
toon_input_1 = """
title: Shopping List
items[3]: apple,banana,carrot
quantity[3]: 5,3,4
"""
decoded_json_1 = decode(toon_input_1)
print("\nDecoded JSON from toon format:")
print(decoded_json_1)


toon_input_2 = """[2]{name,age,city}:
  Alice,30,New York
  Bob,25,Los Angeles"""
decoded_json_2 = decode(toon_input_2)
print("\nDecoded JSON from toon format for tabular array:")
print(decoded_json_2)