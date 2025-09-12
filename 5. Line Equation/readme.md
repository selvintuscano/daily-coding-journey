## 📈 Calculate Y using the Slope-Intercept Form

### 📝 Problem Description:

You are given:
- The slope `m` of a line,
- The y-intercept `b`,
- A value `x`.

Your task is to calculate and return the value of `y` using the **slope-intercept form** of a linear equation:

```
y = mx + b
```

---

### 🔢 Input:
Three floating-point numbers:
- `slope` (float): The slope of the line.
- `intercept` (float): The y-intercept of the line.
- `x` (float): The x-value at which to calculate `y`.

---

### 📤 Output:
- A floating-point number representing the value of `y` corresponding to the given `x`.


### 💻 Python Function:

```python
def calculate_y(slope, intercept, x):
    return slope * x + intercept
```

