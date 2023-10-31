import random

# Linear Search
def linear_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1

# Bubble Sort
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]      

# Insertion Sort
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

# Selection Sort
def selection_sort(list):
    n = len(list)
    for i in range(n):
        index_min = i
        for j in range(i + 1, n):
            if list[j] < list[index_min]:
                index_min = j
        list[i], list[index_min] = list[index_min], list[i]

# Merge Sort
def merge_sort(list):
    if len(list) <= 1:
        return list
    
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

#--------------------------------------------------------------
# Linear Searh
print ("\n Example: Linear Search") 
list_1 = [random.randint(1,100) for _ in range(20)]
print(f'Unordered list: {list_1}')
item_to_search = 90
index = linear_search(list_1, item_to_search)
if index != -1:
    print(f"Item {item_to_search} has been found in the list. Index {index}")
else:
    print(f"Item {item_to_search} not found in list")

# Bubble Sort
print ("\n Example: Bubble Sort") 
list_1 = [random.randint(1,100) for _ in range(20)]
print(f'Unordered list: {list_1}')
bubble_sort(list_1)
print(f'Ordered list: {list_1}')

# Insertion Sort
print ("\n Example: Insertion Sort") 
list_1 = [random.randint(1,100) for _ in range(20)]
print(f'Unordered list: {list_1}')
insertion_sort(list_1)
print(f'Ordered list: {list_1}')

# Selection Sort
print ("\n Example: Selection Sort") 
list_1 = [random.randint(1,100) for _ in range(20)]
print(f'Unordered list: {list_1}')
selection_sort(list_1)
print(f'Ordered list: {list_1}')

# Merge Sort
print ("\n Example: Merge Sort") 
list_1 = [random.randint(1,100) for _ in range(20)]
print(f'Unordered list: {list_1}')
ordered_list_1 = merge_sort(list_1)
print(f'Ordered list: {ordered_list_1}')

# Quick Sort
print ("\n Example: Quick Sort") 
list_1 = [random.randint(1,100) for _ in range(20)]
print(f'Unordered list: {list_1}')
ordered_list_1 = quick_sort(list_1)
print(f'Ordered list: {ordered_list_1}')
