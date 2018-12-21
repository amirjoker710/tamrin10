import math as M

x1 = int(input("::  مولفه 1 نقطه اول را وارد کنید"))
y1 = int(input("::  مولفه 2 نقطه اول را وارد کنید"))
x2 = int(input("::  مولفه 1 نقطه دوم را وارد کنید"))
y2 = int(input("::  مولفه 2 نقطه دوم را وارد کنید"))
x3 = int(input("::  مولفه 1 نقطه سوم را وارد کنید"))
y3 = int(input("::  مولفه 2 نقطه سوم را وارد کنید"))
a = M.sqrt(M.pow((x2-x1),2) + M.pow((y2-y1),2))#Sideways
b = M.sqrt(M.pow((x3-x1),2) + M.pow((y3-y1),2))#Sideways
c = M.sqrt(M.pow((x2-x3),2) + M.pow((y2-y3),2))#Sideways
p = (a+b+c)//2
area = M.sqrt(p*(p-a)*(p-b)*(p-c)) #heroon
print(" :: محیط ",2*p)
print(" :: مساحت ",area)