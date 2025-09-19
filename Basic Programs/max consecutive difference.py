# Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

#You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

def max_consecutive_difference(lst):
    # Your code goes here
    if len(lst) < 2:
        return 0
    max_diff = 0 
    
    for i in range(1,len(lst)):
        
        current_diff = abs(lst[i]-lst[i-1])
        
        if current_diff > max_diff:
            max_diff = current_diff
            
    return max_diff