import math
a1 = int(input("Enter value of a1 \n"))
b1 = int(input("Enter value of b1 \n"))
a2 = int(input("Enter value of a2 \n"))
b2 = int(input("Enter value of b2 \n"))
a3 = int(input("Enter value of a3 \n"))
b3 = int(input("Enter value of b3 \n"))
#Below x is equation for collinear
x = a1 * (b2 - b3) + a2 * (b3 - b1) + a3 * (b1 - b2)
#Below p,q,r is the sides of the triangle
p = a1 + b1
q = a2 + b2
r = a3 + b3
if p == q == r:
  print("Triangle is Equilateral")
elif p==q or q==r or r==p:
  print("Triangle is Isosceles")
elif x == 0:
  print("collinear")
else:
  print("Triangle is Scalene")


