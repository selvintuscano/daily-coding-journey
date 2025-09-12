```python
def check_unique(lst):
    seen = set()
    
    for num in lst:
        if num in seen:
            return False
        seen.add(num)
        
    return True
```
