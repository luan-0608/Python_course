""" 
Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ
Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số
Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)

"""

# # Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ
n = int(input("Nhập số nguyên N: "))
# kiểm tra chẵn lẽ
# if n % 2 == 0:
#     print("N là số chẵn")
# else:
#     print("N là số lẽ")

# cách khác
temp= "N là số chẵn"
if n%2 !=0:
    temp="N là số lẽ"
print(temp)    

# # Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
# input_year = int(input("Nhập vào năm: "))
# if input_year % 2 == 0:
#     print(f"Năm {input_year} là năm nhuận")
# else:
#     print("Không phải năm nhuận")

# # Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số
# a = input("Nhập a: ")
# b = input("Nhập b: ")

# temp = a
# if b > a:
#     temp = b
#     print(f"số lớn nhất là: {temp}")
#     print(f"số nhỏ nhất là: {a}")

# else:
#     print(f"số lớn nhất là: {a}")
#     print(f"số nhỏ nhất là: {a}")

# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
# a=int(input("Nhập a: "))
# b=int(input("Nhập b: "))
# if a==0:
#     print("phương trình vô nghiệm")
# elif a<0:
#     print("phuong trình có nghiệm: ",b/a)
# elif b==0:
#      if a==0:
#     print("phuong trình có vô số nghiệm")
# else:
#     print("Phương trình có nghiệm là: ",-b/a)
          