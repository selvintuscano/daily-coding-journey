### Problem Description:

Write a Python function that finds and returns the **largest element** in a given list of integers.

---

### 💻 Python Function:

```python
def find_largest(numbers):
    largest = numbers[0]
    
    for num in numbers[1:]:
        if num > largest:
            largest = num
            
    return largest
```
