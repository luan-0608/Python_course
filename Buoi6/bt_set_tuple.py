
# Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
# a. Cho biết chiều dài của friends
# b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
# c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
# 2. Tạo một set trống có tên là set_a
# a. Thêm 'Anna' vào set_a
# b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
# c. In ra set_a và tính chiều dài của nó
# d. Xóa 'Jen' ra khỏi set_a
# e. Xóa tất cả các giá trị từ set_a

friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
print(friends,"\n")

# a. Cho biết chiều dài của friends
lengths= len(friends)
print(f'chiều dài của friends là: {lengths}')

# b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng

index_frist= friends[0]
print(f'kiểu của phần tử đầu là:{index_frist} kiểu {type(index_frist)}')
index_last= friends[-1]
print(f'kiểu của phần tử cuối là:{index_last} kiểu {type(index_last)}')
index_mid= lengths
print(f'kiểu của phần tử giữa là:{friends[lengths//2]} kiểu {type(friends[lengths//2])}')

# c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
# name= (input("Nhập vào tên: "))
# gender=(input("Giới tính: "))
# new_friend= (name,gender)
# friends.append(new_friend)
# print(f' danh sách sau khi thêm là: {friends}')

print("\n\n")

# 2. Tạo một set trống có tên là set_a
# a. Thêm 'Anna' vào set_a
# b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
# c. In ra set_a và tính chiều dài của nó
# d. Xóa 'Jen' ra khỏi set_a
# e. Xóa tất cả các giá trị từ set_a

set_a= set()
print(set_a)
set_a.add("Anna")
print(f'Thêm Anna vào set :{set_a}')
set_a.update(('Kenny', 'Jen', 'Danny'))
print(f'Thêm một tuple :{set_a}')

chieu_dai= len(set_a)
print(chieu_dai)


set_a.remove('Jen')
print(set_a)

set_a.clear()
print(set_a)