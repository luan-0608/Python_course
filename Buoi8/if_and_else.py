# n = int(input("n= "))
""" if n > 0:
    print(" so duong")
elif n < 0:
    print("so am")
else:
    print("so 0")
 """
# shift + Alt + A - comment nhiều dòng
# """ VDụ IF ngắn """
# print("N chia hết cho 3" if n%3==0 else "n không chia hết cho 3")

a= int(input("Nhap a: "))
b= int(input("Nhap b: "))

print(a if a>b else b)

# cách khác
m= a

if b>a:
    m=b
print(m)

