import math
def A(x, n):
    S=math.pow(math.pow(x,2)+x+1,n) + math.pow(math.pow(x,2)-x+1,n)
    return S
x=float(input("nhập số x:"))
n=float(input("nhập số n:"))
print("Giá trị của S là:",A(x, n))
