""" Interable """
""" List comprehensions """
lst=[ 1,2,3,4]
# new_lst=[]
# for i in lst:
#     value= i*2
#     new_lst.append(value)
# print(new_lst)

# cách khác
new_lst =[val*2 for val in lst]
print(new_lst)


# set_a={"a","c","b"}
# new_set={s.upper()for s in set_a}
# print(new_set)


# dict comprehesions

d={
    "a":1,
    "b":2,
    "c":3
}
new_d={
    k: v*2
    for k,v in d.items()
}
print(new_d)

