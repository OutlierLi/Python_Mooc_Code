from t import s4
import seven1

print("package:" + (s4.__package__ or '入口文件不属于任何包'))
print("package:" + (seven1.__package__ or '入口文件不属于任何包'))
print("package:" + (__package__ or '入口文件不属于任何包'))
# 顶级包与入口文件同级