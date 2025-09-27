def max_ele(arr):
    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num 
    return maximum 

numbers = [5, 10, 3, 8, 25, 2]
print("Maximum element:", max_ele(numbers))