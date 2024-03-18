numbers= [100,34,56,78,80,-46,3,5,-11]

# total=[v for v in numbers if v%2!=0 ]
# print(total)
# print(sum(total))

new_lst=[v*2 if v%2==0 else v*3 for v in numbers ]
print(new_lst)
new_lst=[]
for x in numbers:
    if x%2 ==0:
        new_lst.append(x*2)
    else:
        new_lst.append(x*3)
print(new_lst)