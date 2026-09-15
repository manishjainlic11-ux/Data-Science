import numpy as n

a = n.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

b = n.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for x in range(10):
    if b[x] % 2 != 0:
        b[x] = -1

c = n.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])

s = 0
for x in range(10):
    v = a[x]
    if v % 2 == 0:
        s = s + v

print(a)
print(b)
print(c)
print(s)
