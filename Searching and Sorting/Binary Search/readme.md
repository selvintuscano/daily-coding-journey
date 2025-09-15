## 🔎 Binary Search in a Sorted List

### 📝 Problem Description:

Implement a binary search algorithm to find the **index** of a target value in a sorted list.  
Return the index if the target is found, otherwise return `-1`.

---

### 💻 Python Function:

```python
def binary_search(arr, target):
    size = len(arr)
    start = 0 
    end = size - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid  # found the target
        elif arr[mid] > target:
            end = mid - 1 
        else:
            start = mid + 1
        
    return -1
```

---

### 🧪 Example Usage:

```python
arr = [10, 23, 35, 45, 50, 70, 85]
target = 85

result = binary_search(arr, target)
print(result)
```

---

### ✅ Output:

```
6
```

> The target value `85` is found at index `6` in the sorted list.

