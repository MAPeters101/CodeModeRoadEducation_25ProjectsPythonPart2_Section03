import random

print("Welcome to our grocery store!\n")

# Create your list with shopping items. Make sure to include ATLEAST 10 items
store_goods = []

while True:
    clumsy_index = random.randint(0, len(store_goods) - 1)
    # Pop the item at this index

    # Print a message that says 'oops, you dropped {item}'

    # User Input: Ask for an index to add the dropped item

    # Check Validity: Add the dropped item to the specified index if it's         valid
    # HINT: The index is valid if the user's index is within the range of 0,     length of your list - 1

    # If the user's index is valid, insert the dropped item at the specified     index

    # Otherwise, give the user a message that their inputted index is NOT         valid

    # Display the updated list of store goods

    # Ask the user if they want to continue
    user_choice = input("Do you want to continue? (yes/no): ").lower()
    if user_choice != "yes":
        break  # Exit the loop if the user decides to stop

print("\nThanks for shopping! Hope you don't drop any more items!")


