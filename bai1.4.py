import math
# đô dài các cạnh
a=float(input("Nhập độ dài cạnh a: "))
b=float(input("Nhập độ dài cạnh b: "))
c=float(input("Nhập độ dài cạnh c: "))
#nửa chu vi
p=(a+b+c)/2
#diện tích bằng công thức Heron
dien_tich=math.sqrt(p*(p-a)*(p-b)*(p-c))
# kq
print("Diện tích của tam giác là:", dien_tich)