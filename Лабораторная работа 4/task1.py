import json

def calculate_product_sum(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    total_sum = sum(entry["score"] * entry["weight"] for entry in data)
    rounded_sum = round(total_sum, 3)
    return rounded_sum
json_file = "input.json"
result = calculate_product_sum(json_file)
print(result)