import random

print("Welcome to our grocery store!\n")

# Create your list with shopping items. Make sure to include ATLEAST 10 items
store_goods = ["milk", "eggs", "bread", "butter", "apples", "bananas", "soup", "tea", "crackers", "jelly", "soap"]

while True:
    clumsy_index = random.randint(0, len(store_goods) - 1)
    # Pop the item at this index
    dropped_item = store_goods.pop(clumsy_index)

    # Print a message that says 'oops, you dropped {item}'
    print(f"Opps, you dropped {dropped_item}.")

    # User Input: Ask for an index to add the dropped item
    index = int(input(f"Where would you like to add {dropped_item}? "))

    # Check Validity: Add the dropped item to the specified index if it's valid
    # HINT: The index is valid if the user's index is within the range of 0, length of your list - 1
    if 0 <= index < len(store_goods) + 1:
    # If the user's index is valid, insert the dropped item at the specified index
        store_goods.insert(index, dropped_item)
    # Otherwise, give the user a message that their inputted index is NOT valid
    else:
        print(f"{index} is invalid.")
    # Display the updated list of store goods
    print(store_goods)
    # Ask the user if they want to continue
    user_choice = input("Do you want to continue? (yes/no): ").lower()
    if user_choice != "yes":
        break  # Exit the loop if the user decides to stop

print("\nThanks for shopping! Hope you don't drop any more items!")


