# for _ in range(5):
#     print("Hello world!")


# lst= list(range(0,5))
# print(lst)

# lst_one= list(range(-4)) # range( 0,-4,1)
# print(lst_one)

# for i in range (1,21):
#     if i%2==0:
#         print(i,end=' ')
# q=input("> ")
# while q != "q":
#     print("Ok")
#     q=input("> ")

""" + Break
    + continue 
 """
# for i in range(1,21):
#     if i>5:
#         break
#     print(i,end=" ")

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
