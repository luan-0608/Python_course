movies_list=["One Peace",
             "Shin","Conan",
             "Doaremon",
             "Pokemon",
             "Gió"]
print(f"danh sách phim ban đầu: {movies_list}")
#2 nhập tên phim
them_phim=input("Nhập tên phim không có trong list: ")

#3 Thêm tên mới nhập vào cuối danh sách
movies_list.append(them_phim)
print(f"Thêm phim  {them_phim} vào cuối danh sách phim")
print(f"Danh sách phim là {movies_list}")

#4 In ra phim đầu tiên phim cuối cùng phim ở giữ danh sách
print(f"Phim đầu tiên trong danh sách phim là : {movies_list[0]}")
print(f"Phim cuối trong danh sách phim là : {movies_list[-1]}")
amount= len(movies_list)
print(f"Phim giữa trong danh sách phim là : {movies_list[amount//2]}")


# Tổng số phim
tong_phim = len(movies_list)
print(f"tổng phim trong list là: {tong_phim}")

# xóa phim đầu danh sách
xoa_dau= movies_list
print(xoa_dau.pop(0))
print(f"danh sách cập nhật sao khi xóa đầu:{xoa_dau}")

# xóa phim cuối danh sách
movies_list.pop()
print(f" danh sách sau khi xóa cuối:{movies_list}")
# chèn phim vao đầu danh sách
movies_list.insert(0,"Ori")
print(movies_list)

dem_phim=movies_list.count("One Peace")
print(dem_phim)
# tìm vị trí phim
vi_tri=movies_list.index("Gió")
print(vi_tri)

movies_new=["A","B","C","D"]
movies_list.extend(movies_new)
print(movies_list)
movies_list.clear()
print(movies_list)
