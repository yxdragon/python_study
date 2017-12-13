def fib(lim, a=1, b=0, lev=1):
    if lev == lim:return a+b
    return fib(lim, b, a+b, lev+1)

def fib_lst(lim, lst, a=1, b=0, lev=1):
    lst.append(a+b)
    if lev == lim:return lst
    return fib_lst(lim, lst, b, a+b, lev+1)

print(fib(5))
print(fib_lst(5, []))
