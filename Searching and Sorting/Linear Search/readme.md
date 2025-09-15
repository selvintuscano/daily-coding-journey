### 📝 Problem Description:

Implement a function `linear_search` that performs a **linear search** on a list to find a given value.  
The function should return the **index of the first occurrence** of the value in the list, or `-1` if the value is not found.

---

### 🔢 Parameters:

- `arr`: A list of elements (can be empty).
- `target`: The value to search for in the list.

---

### 📤 Return:

- An integer representing the **index (0-based)** of the first occurrence of `target` in `arr`, or `-1` if not found.

---

### ✅ Examples:

```python
linear_search([3, 7, 2, 5], 2)      # ➞ 2
linear_search([1, 1, 2, 1], 1)      # ➞ 0
linear_search([], 5)               # ➞ -1
linear_search([4, 2, 8], 6)        # ➞ -1
```

---

### 💻 Python Function:

```python
def linear_search(arr, target):
    # TODO: Implement this function
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1
```
