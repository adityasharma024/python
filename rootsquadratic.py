from cmath import sqrt


a=int(input("Enter the value of a\n"))
b=int(input("Enter the value of b\n"))
c=int(input("Enter the value of c\n"))
D=sqrt(b*b-4*a*c)
r1=(-b-D)/2*a
r2=(-b+D)/2*a
print(r1,r2)
