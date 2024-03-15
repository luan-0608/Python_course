lst=[2,3,4,6,7,8,3]
new_lst=lst[0:2:1]
print(new_lst)

print(lst is new_lst)  #so sánh địa chỉ bộ nhớ
print(lst == new_lst)  #so sánh giá trị
print(id(lst),id(new_lst)) # in ra thông tin bộ nhớ
