def power(n,p):
    if p==0:
        return 1
    if p%2==0:
        return power(n,p//2)*power(n,p//2)
    return power(n,p//2)*power(n,p//2)*n
print(power(2,10))