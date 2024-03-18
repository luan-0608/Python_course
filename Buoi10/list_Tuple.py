# lst= [4,10,5,6]
# lst_set= {4,10,5,6} # in khong theo thứ tự

# for value in lst:
#     print(value)

d = {"a": 1, "b": 2, "c": 3}
print(type(d))

# for key in d.values():
#     print(key)

for item in d.items():
    key,value = item
    print(key,end=" ")
    print(value)
    print('-'*20)
    