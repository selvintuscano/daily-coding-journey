Problem Description:

You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.



Input:

Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.



Output:

An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.


Python Function:

```python
def calculate_lift_rounds(n, capacity):
    full_rounds = n // capacity
    if n % capacity != 0:
        return full_rounds + 1 
    else:
        return full_rounds
```
