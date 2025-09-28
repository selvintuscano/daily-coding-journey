def reversee(arr):

    reversed_array = []

    for num in arr:
        reversed_array= arr[::-1]
    return reversed_array 

arr = [2,3,4,5]
print(reversee(arr))