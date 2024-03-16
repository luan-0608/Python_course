set1 = {1, 4, 3, 2}
set2 = {2, 3, 10, -10}

# Lấy phần tử giống nhau trong set
# set3= set1.intersection(set2)
# print(set3)
# print( set1 & set2)

# Lấy phần tử khác của set1 vs set2
# set3= set1.difference(set2)
# print(set3)
# print(set1-set2)

# Lấy tất cả
# set3= set1.union(set2)
# print(set3)
# print( set1 | set2 )

# lấy ra các phần tử trừ phần chung giống nhau trong set

set3 = set1.symmetric_difference(set2)
print(set3)
print(set1 ^ set2)
