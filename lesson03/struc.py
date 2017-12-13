ls = []
ls.append(1)
ls.append(2)
print(ls)
print(ls[0])
for i in ls:
    print(i)
del ls[0]
print(ls)


tp = (1,2,3,4,5)
print(tp)
print(tp[2])

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1-s2)
print(s1&s2)
print(s1|s2)

dic = {}
dic['book'] = '书籍'
dic['apple'] = '苹果'
print(dic['book'])

dic[1] = 'd'
dic[2] = [1,2,3]
print(dic[1])


