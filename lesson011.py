list = []
for i in range(5):
    string = input("Enter a string: ")
    list.append(string)

print(list)

string2 = input("Enter a string: ")
ind = int(input("What index do you want to add this to: "))
list.insert(ind, string2)
print(list)

ind = int(input("What index do you want to change: "))
el = input("Enter the new element: ")
list[ind] = el
print(list)


