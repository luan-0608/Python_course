# a, b = map(int, input().split())
# print(a if a < b else b)

#
# """ Hàm eval """
# print(eval("1+2 **4"))

# lst=[1,3,4,6,7]
# print(*lst,sep="%")
# a= lst
# print("-".join(map(str,a)))


""" Làm tròn số bằng format """
# x= 2.45684
# print(format(x,".2f"))
# print(round(x,2))

# # pow
# print(pow(2.5,3))\

# """ Hàm sorted => luôn trà về danh sách mới (không thay đổi danh sách ban đầu) """
# new_lst = [1, 3, 5, 4, 2, 10]
# # new_lst.sort() # tạo ra lst moi khac sap xep
# print(new_lst)
# lst_sort = sorted(new_lst, reverse=True)
# print(lst_sort)

# """ ASCII """
# char= "A"
# print ("ASCII Code : ",ord(char))

# assii_code=65
# print(chr(assii_code))


# s="abcd"
# print(list(s)) # ["a","b","c","d"]

# lst_one= list(map(eval,input().split()))
# print(lst_one)
""" divmod => trả về một tuple """
print(divmod(4, 3))
thuong, phan_so = divmod(11, 3)  # 11//3 =3 , 11 % 3 =2
print(thuong)
print(phan_so)

""" 
012345
0b1010 """
int_number = 10
bianry_string = bin(int_number)
print(bianry_string[2:])
print(format(int_number, "b"))
print(f"{int_number:b}")
