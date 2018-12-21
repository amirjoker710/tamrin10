print("Common divisor :نمایش مقسوم علیه های مشترک ۲ عدد")
a=int(input("enter  first number : "))
b=int(input("enter  second number : "))

if a>b:
    a,b=b,a
L1=[]
for k  in range(1,a+1):
    if(a%k==0)and(b%k==0):
        L1.append(k)
print (L1)