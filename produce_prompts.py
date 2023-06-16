import csv
import json

dataset = []

with open('products_new.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_name = row['product_name']
        aisle_id = row['aisle_id']
        department_id = row['department_id']
        inventory = row['inventory']

        prompts = [
            f"What deparment is {product_name} located?"
            f"What aisle is {product_name} located?"
            f"What other products can I find that are similar to {product_name} and in the same aisle?"
            f"How much more do you have of {product_name}?"
        ]

        completions = [
            f"{product_name} is located in deparment {department_id}.",
            f"{product_name} can be found in aisle {aisle_id}.",
            f"You can find similar products to {product_name} in the same aisle, such as [product_name_1], [product_name_2], and [product_name_3].",
            f"We currently have {inventory} units of {product_name} in stock."
        ]

        for prompt, completion in zip(prompts, completions):
            dataset.append({
                "prompt": prompt,
                "completion": completion
            })

with open('dataset.json', 'w') as file:
    json.dump(dataset, file, indent=2)

print("Dataset written to 'dataset.json' file.")