"""
+zip
+enumerate
"""

# lst = ["a", "b", "c"]
# lst2 = (1, 2, 3, 4)
# # chứa giá trị tương ứng
# print(list(zip(lst, lst2)))

#     #  0   1   2
#     #  1   2   3
# lst= ["a",'b','c']

# print(list(enumerate(lst,start=1))) # [(0, 'a'), (1, 'b'), (2, 'c')]

# lst= ('a','b','c')
# lst2=(1,2,3)

# print(dict(zip(lst,lst2)))


# lst = [1, 2, 3, 4]
# new_lst = [v**3 for v in lst]
# print(new_lst)

# new_lstt=[]
# for i in lst:
#     val= i**3
#     new_lstt.append(val)
# print(new_lstt)

    #  0  1  2  3
lst = [1, 2, 3, 4]

# {i} -{value}
# for item in enumerate(lst,start=1):
#     idx, value = item
#     print(f"{idx} - {value}")
# print(list(zip(enumerate(lst,start=1))))

# print(list(range(len(lst))))

# for i in range(len(lst)):
#     print(i,lst[i])


for i,v in enumerate(lst):
    if i%2!=0:
        print(i,v)
