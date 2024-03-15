# Cho danh sách (list) friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
# Yêu cầu:
# a. Lấy ra 4 người bạn đầu tiên trong friends
# b. Lấy ra 4 người bạn cuối trong friends
# c. Đảo ngược danh sách friends
# d. Lấy ra những người bạn từ vị trí 1 đến hết
# e. Copy danh sách ban đầu thành một danh sách mới
# f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
# Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
# students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# Yêu cầu:
# a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
# b. Lấy ra tuổi của sinh viên thứ hai
# c. Lấy ra thông tin hai sinh viên cuối cùng
# d. Lấy ra id của sinh viên thứ ba

friends = ["Jen",
           "Jack", 
           "Kenny", 
           "Jelly", 
           "Bob", 
           "Henry", 
           "Anne"]

print(friends,"\n")
# a. Lấy ra 4 người bạn đầu tiên trong friends
friends_frist_four= friends[:4]
print(f"4 người đẩu tiên là: {friends_frist_four}")


# b. Lấy ra 4 người bạn cuối trong friends
friends_last_four= friends[-4:]
print(f"4 người cuối cùng là: {friends_last_four}")

# c. Đảo ngược danh sách friends
reverseds_friend= friends[::-1]
print(f'danh sách đảo ngược là: {reverseds_friend}')

# d. Lấy ra những người bạn từ vị trí 1 đến hết
location_one= friends[1:]
print(f'vị trí từ 1 đến hết: {location_one}')

# e. Copy danh sách ban đầu thành một danh sách mới
new_friends=friends.copy()
print(f'danh sách coppy là:{new_friends}')

# f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
location_two= friends[1:-1]
print(f'Vị trí thứ 2 đến vị trí sát cuối là: {location_two}')

print("\n\n\n")

students = [["SV001", "Bob", 23], 
            ["SV002", "Kenny", 34], 
            ["SV003", "Henry", 45]]
print(students)

# a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
students_info_sv1= students[0]
print(f'ID: { students_info_sv1[0]}, Name: { students_info_sv1[1]}, Age: { students_info_sv1[2]}')

# b. Lấy ra tuổi của sinh viên thứ hai
students_age_sv2= students[1][2]
print(f'Tuổi sinh viên 2 là : {students_age_sv2}')

# c. Lấy ra thông tin hai sinh viên cuối cùng
students_info_sv2_sv3= students[1:]
print("Thông tin sinh viên 2 là: ")
print(f"ID: {students_info_sv2_sv3[0][0]}, Name: {students_info_sv2_sv3[0][1]}, Age:{students_info_sv2_sv3[0][2]}")
print(f"ID: {students_info_sv2_sv3[1][0]}, Name: {students_info_sv2_sv3[1][1]}, Age:{students_info_sv2_sv3[1][2]}")
# d. Lấy ra id của sinh viên thứ ba
students_id_three= students[2][0]
print(f'ID sinh viên 3 là: {students_id_three}')


