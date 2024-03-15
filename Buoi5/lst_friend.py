friends=["jack","Join","kelly","Herry"]
print(friends[1])
print(friends[2])
friends[0]="Anna"
print(friends)
print(len(friends))
friends.insert(1,"Jen")
print(friends)
last=friends.pop()
print(friends)
friends.remove("join".title())
print(friends)
del friends[1]
print(friends)

print(friends[0])
max_value=max(friends)
print(max_value)