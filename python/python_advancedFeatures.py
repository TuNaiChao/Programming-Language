# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])   # 取前3个元素，包含索引0，不包含索引3
print(L[:3])    # 省略0，效果同上
print(L[1:3])   # 取索引1到索引3的元素
print(L[-2:])   # 取倒数两个元素
print(L[-2:-1]) # 取倒数第二个元素 倒数第一个元素是-1，不包含-1
print(L[:])     # 取所有元素

L = list(range(100)) # 生成0-99的数列
print(L[:10])    # 前10个数
print(L[-10:])   # 后10个数
print(L[10:20])  # 10-19的数
print(L[:10:2])  # 前10个数，每2个取一个
print(L[::5])    # 所有数，每5个取一个
print(L[:])      # 复制一个list

print((0, 1, 2, 3, 4, 5)[:3]) # 对tuple也可以进行切片操作，结果仍是tuple
# 字符串也可以看成是一种list，每个元素就是一个字符
print('Hello, World!'[:5]) # 取前5个字符
print('ABCDEFG'[::2]) # 每2个取一个字符

def trim(s):
    "去除字符串首尾的空格"
    while s[0:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:  # 默认情况下，dict迭代的是key
    print(key)
for value in d.values(): # 如果要迭代value，可以用for value in d.values()
    print(value)
for k, v in d.items():  # 如果要同时迭代key和value，可以用for k, v in d.items()
    print(k, '=', v)

# 迭代字符串
for ch in 'ABC':
    print(ch)

# 判断是否是可迭代对象
from collections.abc import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
print(isinstance([1,2,3], Iterable)) # list是否可迭代
print(isinstance(123, Iterable)) # 整数是否可迭代

for i, value in enumerate(['A', 'B', 'C']): # enumerate()函数可以把一个list变成索引-元素对
    print(i, value)

# 列表生成式
print([x * x for x in range(1, 11) if x % 2 == 0])  # 生成1-10中偶数的平方
print([m + n for m in 'ABC' for n in 'XYZ']) # 两层循环，生成全排列

import os
print([d for d in os.listdir('.')]) # 列出当前目录下的所有文件和目录名

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()]) # 生成['x=A', 'y=B', 'z=C']

print([s.lower() for s in ['Hello', 'World', 'IBM']]) # 把所有字符串变成小写

print([x for x in range(1, 11) if x % 2 == 0]) # 筛选出1-10的偶数
print([x if x % 2 == 0 else -x for x in range(1, 11)]) # 1-10的数，偶数不变，奇数取反   
#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else

# 生成器
g = (x * x for x in range(10)) # 创建一个生成器对象
for n in g:
    print(n)

def fib(max):
    "斐波那契数列"
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # yield语句返回一个值，并暂停函数的执行状态
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数
# 调用generator函数会返回一个生成器对象
# 生成器对象也是一个迭代器，可以使用next()函数获得下一个值
# 也可以使用for循环来迭代它，直到没有yield语句
# 生成器的好处是可以节省大量的内存空间，因为它不是一次性把所有的值都生成出来，而是每次需要的时候才生成一个值

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o)) # 执行到第一个yield，返回1，并暂停
print(next(o)) # 继续执行，直到下一个yield，返回3，并暂停
print(next(o)) # 继续执行，直到下一个yield，返回5，并暂停
# print(next(o)) # 继续执行，发现没有yield，抛出StopIteration

next(odd()) # 每次调用next()都会创建一个新的生成器对象，从头开始执行    
next(odd())
next(odd())
# 调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。

# 迭代器
# 可迭代对象：可以使用for循环遍历的对象统称为可迭代对象（Iterable）
from collections.abc import Iterable
print(isinstance((x for x in range(10)), Iterable)) # 生成器是可迭代对象
print(isinstance([], Iterable)) # list是可迭代对象
print(isinstance({}, Iterable)) # dict是可迭代对象
print(isinstance('abc', Iterable)) # str是可迭代对象

# 迭代器：可以被next()函数调用并不断返回下一个值的对象称为迭代器（Iterator）
from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator)) # 生成器都是迭代器
print(isinstance([], Iterator)) # list不是迭代器
print(isinstance({}, Iterator)) # dict不是迭代器
print(isinstance('abc', Iterator)) # str不是迭代器

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator)) # 通过iter()函数获得的迭代器
print(isinstance(iter('abc'), Iterator)) # 通过iter()函数获得的迭代器
print(isinstance(iter({}), Iterator)) # 通过iter()函数获得的迭代器

# 生成器都是Iterator，但list、dict、str虽然是Iterable，却不是Iterator。
# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的，例如
for x in [1, 2, 3, 4, 5]:
    pass
# 实际上完全等价于
# 首先获得Iterator对象
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        # 通过next()获得下一个值
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
# 所以，for循环只能用于Iterable对象，而不能用于Iterator对象。