## 🃏 Insertion Sort Algorithm

### 📝 Problem Description:

You are given a list of integers. Write a Python function to sort the list in **ascending order** using the **Insertion Sort** algorithm.

**Insertion Sort** works by building a sorted section of the list one element at a time, inserting each new element into its **proper position** within the already sorted section.

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
lst = [12, 11, 13, 5, 6]
```

**Output:**
```
[5, 6, 11, 12, 13]
```

**Input:**
```python
lst = [31, 41, 59, 26, 41, 58]
```

**Output:**
```
[26, 31, 41, 41, 58, 59]
```

---

### 💻 Python Function:

```python
def insertion_sort(arr):
    n = len(arr)

    for current in range(1, n):
        currentCard = arr[current]
        correctPosition = current - 1  # It will go from i-1 to 0

        while correctPosition >= 0 and arr[correctPosition] > currentCard:
            arr[correctPosition + 1] = arr[correctPosition]
            correctPosition -= 1

        arr[correctPosition + 1] = currentCard  # Insert at correct position

    return arr
```

