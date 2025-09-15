
### 📝 Problem Description:

You are given a list of integers. Write a Python program that **reverses the list without using slicing (`lst[::-1]`)**. The program should return the reversed list.



### 💻 Python Function:

```python
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

```
