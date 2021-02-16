import json

student = [
    {'name':'qiyue', 'age':18, 'flag':False},
    {'name':'Li', 'age':20}
]

json_str = json.dumps(student)
print(json_str)