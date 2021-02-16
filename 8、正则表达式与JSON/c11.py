import json

# 序列化
json_str = '{"name":"qiyue","age":18,"IsMan":true}' # 注意布尔类型之间的不同

student = json.loads(json_str)
print(type(student))
print(student)

for key,value in student.items():
    print(key + ":" + str(value))

print(student['name'])
print(student['age'])

another_json_str = '[{"name":"qiyue","age":18}, {"name":"Li","age":20}]'
students = json.loads(another_json_str)
print(students)
