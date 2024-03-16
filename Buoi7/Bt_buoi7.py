# Cho hai tập hợp (set)
# art_students = {"John", "Max", "Anna", "Bob", "Obito"}
# math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
# Tìm những người bạn học cả vẽ lẫn toán
# Tìm những người bạn học vẽ nhưng không học toán
# Tìm những người bạn học toán nhưng không học vẽ
# Tìm những người bạn học vẽ hay toán không phải cả hai
# Tìm tất cả những người bạn

art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}


# Tìm những người bạn học cả vẽ lẫn toán
art_and_math = art_students.intersection(math_students)
print(f"những người bạn học cả vẽ lẫn toán :{art_and_math}")
print(f"những người bạn học cả vẽ lẫn toán: {art_students & math_students}")

# Tìm những người bạn học vẽ nhưng không học toán
art_not_math = art_students.difference(math_students)
print(f"Tìm những người bạn học vẽ nhưng không học toán {art_not_math}")
print(f"Tìm những người bạn học vẽ nhưng không học toán {art_students- math_students}")

# Tìm những người bạn học toán nhưng không học vẽ
math_not_art = math_students.difference(art_students)
print(f"Tìm những người bạn học toán nhưng không học vẽ: {math_not_art}")
print(f"Tìm những người bạn học toán nhưng không học vẽ: {math_students-art_students}")
# Tìm những người bạn học vẽ hay toán không phải cả hai
chung_khac_nhau = art_students.symmetric_difference(math_students)
print("Phần chung khác nhau: ", chung_khac_nhau)
# Tìm tất cả những người bạn
all_math_and_art = art_students.union(math_students)
print("Tất cả những người bạn cùng học là: ", all_math_and_art)
print("Tất cả những người bạn cùng học là: ", art_students | math_students)


# Cho dict sau:
# album_info = {
#     "album_name": "The Dark Side of the Moon",
#     "band": "Pink Floyd",
#     "release_year": 1973,
#     "track_list": [
#         "Speak to Me",
#         "Breathe",
#         "On the Run",
#         "Time",
#         "The Great Gig in the Sky",
#         "Money",
#         "Us and Them",
#         "Any Colour You Like",
#         "Brain Damage",
#         "Eclipse"
#     ]
# }
# Yêu cầu:
# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
# Thay đổi giá trị của key: release_year từ 1973 thành 1971
# Xóa phần tử với key là track_list
# Thêm một key mới là amount = 2000 bằng hai cách
# Làm trống dict: album_info
print("\n\n")
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse",
    ],
}


# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
print("\n")
# cách 1
values = (
    album_info["album_name"],
    album_info["band"],
    album_info["release_year"],
    album_info["track_list"],
)
print("Các giá trị trong dic là: ", values)
print("\n")
# cách 2
keys = (
    album_info.get("album_name"),
    album_info.get("band"),
    album_info.get("release_year"),
    album_info.get("track_list"),
)
print("Các giá trị trong dic là: ", keys)
print("\n")
# Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info["release_year"] = "1971"
print("Thay đổi year: ", album_info)
print("\n")
# Xóa phần tử với key là track_list
del album_info["release_year"]
print(album_info)
print("\n")


# Thêm một key mới là amount = 2000 bằng hai cách
# cách 1:
album_info.update(amount=2000)
print(album_info)

# cách 2:
info={
    "anount":2000
}
album_info.update(info)
print(album_info)

# cách 3:
album_info["anount"]=2000

# Làm trống dict: album_info
album_info.clear()
print(album_info)