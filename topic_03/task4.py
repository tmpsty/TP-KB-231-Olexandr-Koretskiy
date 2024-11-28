def find_insert_position(lst, x):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

# Приклад використання
print(find_insert_position([1, 3, 5, 7, 9], 6))  # Виведе 3