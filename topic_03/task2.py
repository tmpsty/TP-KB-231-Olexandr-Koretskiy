lst = [5, 2, 9]

# extend()
lst.extend([1, 6])
print("extend:", lst)

# append()
lst.append(10)
print("append:", lst)

# insert()
lst.insert(2, 7)
print("insert:", lst)

# remove()
lst.remove(2)
print("remove:", lst)

# clear()
lst_copy = lst.copy()  # зберігаємо копію
lst.clear()
print("clear:", lst)

# sort()
lst_copy.sort()
print("sort:", lst_copy)

# reverse()
lst_copy.reverse()
print("reverse:", lst_copy)

# copy()
new_lst = lst_copy.copy()
print("copy:", new_lst)