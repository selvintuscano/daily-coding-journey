def armstrong(n):
    order = len(str(n))

    sum = 0 
    temp = n 

    while temp>0:
        digit = temp%10
        sum = sum + digit ** order
        temp = temp // 10

    if sum == n:
        print('number is armstrong')
        return True
    else:
        print('not an armstrong number')
        return False


print(armstrong(13))