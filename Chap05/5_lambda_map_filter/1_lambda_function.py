
c2f = lambda c: (c * (9 / 5)) + 32
print (c2f(100))

t=[0,10,20,30,100]
f=list(map(lambda c: c2f(c), t))
print(f)

num1 = [4, 5, 6]
num2 = [5, 6, 7]
result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

