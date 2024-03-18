""" 
In các số từ 1 đến 100 trên cùng một hàng
In 100 lần dòng chữ "Hello World!"
In ra các số chia hết cho 3 trong đoạn [1, 1000]
Đếm số lượng số nguyên tố trong [1, 100]
Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n] """
# In các số từ 1 đến 100 trên cùng một hàng
# for i in range(1,101):
#     print(i,end=" ")

# In 100 lần dòng chữ "Hello World!"
# for i in range(1,101):
#     print(i,"Hello word")

# In ra các số chia hết cho 3 trong đoạn [1, 1000]

# for i in range( 1,1000):
#     if i%3==0:
#         print(i,end=" ")

# Đếm số lượng số nguyên tố trong [1, 100]
count = 0

for n in range(2, 101):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        count += 1
        
print(count)