# filter的使用,剔除元素

list_x = [1, 0, 1, 0, 0, 1]
r = filter(lambda x: True if x==1 else False, list_x) # True代表保留
print(r)
print(list(r))
