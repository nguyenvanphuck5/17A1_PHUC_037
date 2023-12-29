list=[]
while True:
    gia_tri=int(input('Nhập giá trị: '))
    list.append(gia_tri)
    x=int(input('Tiếp tục nhập giá trị? 1: Có,0: không   '))
    if x == 1:
        continue
    elif x==0:
        break
x=int(input('Nhập vào một giá trị cần tìm của x:'))
print('List:',list)
print('Tổng các giá trị trong list:',sum(list))
print(x,'xuất hiện',list.count(x),'trong list')
print(min(list),'không lớn hơn tất cả số trong list')
list1=[]
for i in list1:
    if i>x:
       list1.append(i)
print('các số lớn hơn',x,'trong list:',list1)