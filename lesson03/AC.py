def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def A(n, m):
    s = 1
    for i in range(n-m+1, n+1):
        s *= i
    return s

# 开发效率优先
def A2(n, m):
    return fact(n)//fact(n-m)

def C(n, m):
    return A(n, m)//fact(m)
