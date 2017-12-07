'''
print('0+1+2+3...+100:')
s = 0
for i in range(1, 101):
    s += i
print(s)

print('找出0-100之间，能被100整出的数：')
for i in range(1, 101):
    if 100%i == 0:
        print(i)

print('找出0-100之间，各个数位上数字相加是9的偶数：')
for i in range(1, 101):
    if i%2==0 and i//10+i%10 == 9:
        print(i)
'''
print('找出七个各个数位上数字相加是9的偶数：')
s, i = 0, 0
while True:
    i += 1
    if i%2==1: continue
    cs, ci = 0, i
    while ci>0:
        cs += ci%10
        ci //= 10
    if cs == 9:
        s += 1
        print(i)
        if s==7:break
