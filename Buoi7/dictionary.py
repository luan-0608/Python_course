import json

student = {"name": "Bob", "age": 23, "grades": [45, 67, 90, 98, 99]}

# print(json.dumps(student,indent=4))

# value= student["name"]
value = student.get("id", "0001")

print(value)
