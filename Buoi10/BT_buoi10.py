"""
Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
Cho dict như sau:
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
In ra người già nhất
Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
In ra enumerate các key trong people dict
Sử dụng hàm dict để biến enumerate bên trên trở thành dict
Sử dụng zip function để tạo 2 lists sau trở thành một dict
fruits = ["banana", "apple", "kiwi", "mango", "cherry", "orange"]
amounts = [12, 34, 90, 100, 300, 45, 60, 70, 678] """

# Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
#cách 1
# lst=list(range(1000+1))
# # print(lst)
# chan=le=0

# for temp in lst:
#     if temp%2==0:
#         chan+=1
#     else:
#         le+=1
# print(f"Tổng chẵn là:{chan}, Tổng lẽ là: {le}")

# #cách 2
# chan= sum([1 for n in range(0,1001) if n%2 ==0])
# le= sum([1 for n in range(0,1001) if n%2 !=0])
# print(f"Số lượng giá trị chẵn trong [0, 1000]\t: {chan}")
# print(f"Số lượng giá trị lẻ trong [0, 1000]\t: {le}")
# # Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
# # lst_one= [1,2,3,4,35,10]
# # new_lst_one= [x*2 for x in lst_one]
# # print(new_lst_one)


# # 2. Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
# int_numbers = [int(x) for x in input("Nhập vào danh sách các số nguyên:\n").split()]
# doubled_numbers = [n*2 for n in int_numbers]

# print(doubled_numbers)

# Cho dict như sau:
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}

for i in people.items():
    key,value= i
    print(key)
    print(value)

a= people["Amy"]
print(a)