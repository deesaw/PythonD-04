def fact(n):
    if n < 0:
        raise ValueError("negative numbers do not have factorials")
    f=1
    for x in range(2,n+1):
        f*=x
    return  f

print(fact(10))
print(fact(0))
print(fact(-10))
