def min_ele(arr):
    minimum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num 
    return minimum 

numbers = [5, 10, 3, 8, 25, 2]
print("minimum element:", min_ele(numbers))