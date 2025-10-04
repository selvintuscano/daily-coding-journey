my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2

count = 0
for item in my_list:
    if item == element:
        count += 1
        
print(f"The element {element} appears {count} times")
