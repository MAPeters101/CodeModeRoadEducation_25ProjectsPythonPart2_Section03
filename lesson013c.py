
def linear_search(my_list, target):
    for index, element in enumerate(my_list):
        if element == target:
            return index
    return -1

my_list = [1, 2, 3, 4, 5]
print(linear_search(my_list,3))
print(linear_search(my_list,6))
