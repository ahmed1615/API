def p(x,y):
    if y==0:
        return 1
    else:
        return x*p(x,y-1)
print(p(2,3))
