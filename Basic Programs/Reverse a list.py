## You are given a list of integers. 
# Write a Python program that reverses the list without using slicing (lst[::-1]). The program should return the reversed list.


def reverse(lst):
    lst.reverse()
    return lst


numbers = [4,5,6,7,8]
print('reversed list:', reverse(numbers))


# solution 2

def reverse_list(lst):
    return lst[::-1]

numbers = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(numbers))


