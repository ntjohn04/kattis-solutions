import math

a = input()
a = a.split(sep=" ")

h = int(a[0])
th = int(a[1])

print(math.ceil(h/math.sin(th*math.pi/180)))

