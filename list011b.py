list2 = ["hello", "my", "name", "is", "hello", "hello", "name", "my", "is"]

list2.pop(0)
list2.pop(-1)
print(list2)

"""The authors code doesn't work because the indexing changes
for i in range(len(list2)):
    if list2[i] == "hello":
        list2.pop(i)
"""
""" This doesn't work either because the indexing changes
for i in range(len(list2)):
    if list2[i] == "hello":
        list2.remove("hello")
"""
while "hello" in list2:
    list2.remove("hello")

print(list2)