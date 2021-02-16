# 用字典映射代替

# switch(day)
# {
#     case 0:
#         pass;
#         break;
#     default:
#     pass;
#     break;
# }

# 用字典改写代码
day = 0

switcher = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday'
}

day_name = switcher[day]
# print(day_name)

# 用枚举类改写代码
from enum import Enum

class Days(Enum):
    day0 = 'Sunday'
    day1 = 'Monday'
    day2 = 'Tuesday'

# print(Days('Sunday').value)
day_name = list(Days)[day].value
# print(day_name)

# 解决default分支的问题,使用get方法访问字典
day_name = switcher.get(day, 'Unknown')
# print(day_name)
day = 3
day_name = switcher.get(day, 'Unknown') # 当不符合全部key时，返回第二个参数！
# print(day_name)

# 模拟case中写入代码块
def get_Sunday():
    return 'Sunday'

def get_Monday():
    return 'Monday'

def get_Tuesday():
    return 'Tuesday'

switcher1 = {
    0 : get_Sunday(),
    1 : get_Monday(),
    2 : get_Tuesday()
}

def get_default():
    return 'Unknow'

day = 0
day_name = switcher.get(3, get_default)
# print(type(day_name))
if isinstance(day_name, str):
    print(day_name)
else:
    print(day_name())
# print(type(day_name))
# print(day_name)
