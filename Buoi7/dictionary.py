import json

student = {"name": "Bob", "age": 23, "grades": [45, 67, 90, 98, 99]}

# print(json.dumps(student,indent=4))

# value= student["name"]
# value = student.get("id", "0001")
# print(value)

student["id"] = "SV001"
student["name"] = "jack"
print(student)

student.update(id="SV001", gender="male")
print(json.dumps(student, indent=4))
