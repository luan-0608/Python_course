# friend=[
#     ("Bob",23),
#     ("Ann",63),
#     ("Luci",28),
#     ("Herry",73),
# ]
# print(friend[-1])
from copy import deepcopy
lst=[[1,[2,3]],(2,4)]
print(lst[0][1][0])

lst1= deepcopy(lst)
lst[0][1].append(100)
print(lst)

print(lst is lst1)
print(lst1)

