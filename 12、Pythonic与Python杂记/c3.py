# iterator和generator 可迭代对象和迭代器

# 将普通对象变为迭代器
class students:
    def __iter__(self):
        pass
    def __next__(self):
        pass

class Book:
    pass

class BookCollection(Book):
    def __init__(self):
        self.data = ['《往事》', '《只能》', '《回味》']
        self.cur = 0
        pass
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur >= len(self.data):
            self.cur = 0
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r

books = BookCollection()
for book in books:
    print(book)

for book in books:
    print(book)

# books1 = BookCollection()
# print(next(books1))
# print(next(books1))
# print(next(books1)) # 一种调用私有函数__next__的外部方法

# import copy
# books_copy = copy.copy(books)
# books_copy.cur = 1
# print(books_copy.cur)
# for book in books_copy:
#     print(book)
