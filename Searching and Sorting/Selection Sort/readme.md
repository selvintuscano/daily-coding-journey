## 📊 Selection Sort Algorithm

### 📝 Problem Description:

You are given a list of integers. Write a Python function to sort the list in **ascending order** using the **Selection Sort** algorithm.

**Selection Sort** works by repeatedly finding the **minimum element** from the **unsorted part** of the list and swapping it with the **first element** of the unsorted part.

---

### 🔢 Parameters:

- `lst` (List of integers): The list to be sorted.

---

### 📤 Returns:

- A list of integers sorted in ascending order.

---

### ✅ Examples:

**Input:**
```python
lst = [64, 25, 12, 22, 11]
```

**Output:**
```
[11, 12, 22, 25, 64]
```

**Input:**
```python
lst = [29, 10, 14, 37, 13]
```

**Output:**
```
[10, 13, 14, 29, 37]
```

---

### 💻 Python Function:

```python
def selection_sort(arr):
    # Your code goes here
    n = len(arr)

    for i in range(n - 1):   # Outer loop
        min_index = i        # Assume current index is the smallest
        for j in range(i + 1, n):  # Inner loop to find the true minimum
            if arr[j] < arr[min_index]: 
                min_index = j  # Update index of minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap

    return arr
```

