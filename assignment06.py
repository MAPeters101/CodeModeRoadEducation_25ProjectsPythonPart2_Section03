import random

print("Welcome to our grocery store!\n")

store_goods = ["milk", "eggs", "bread", "butter", "apples", "bananas", "soup", "tea", "crackers", "jelly", "soap"]

while True:
    clumsy_index = random.randint(0, len(store_goods) - 1)
    dropped_item = store_goods.pop(clumsy_index)

    print(f"Opps, you dropped {dropped_item}.")

    index = int(input(f"Where would you like to add {dropped_item}? "))

    if 0 <= index <= len(store_goods):
        store_goods.insert(index, dropped_item)
    else:
        print(f"{index} is invalid.")
    print(store_goods)
    user_choice = input("Do you want to continue? (yes/no): ").lower()
    if user_choice != "yes":
        break  # Exit the loop if the user decides to stop

print("\nThanks for shopping! Hope you don't drop any more items!")


