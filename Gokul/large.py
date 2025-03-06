def find_largest_number(lst):
    if not lst:
        return None 
    largest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
    return largest
numbers = [3, 7, 2, 9, 5,59]
print(find_largest_number(numbers))
