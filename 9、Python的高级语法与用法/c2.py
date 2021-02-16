from enum import IntEnum, unique

@unique
class VIP(IntEnum):
    # Y = 'k' # 只能是数字类型的值
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4 

print(VIP.BLACK)