abs(-20) # 求绝对值，可以使用help（abs）查看帮助文档
max(1,3,2,5,4) # 求最大值
min(1,3,2,5,4) # 求最小值
sum([1,2,3,4,5]) # 求和
round(3.14159,2) # 四舍五入，保留两位小数  
pow(2,3) # 幂运算，2的3次方

def my_abs(x):
    """自定义绝对值函数"""
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-10))

# 空函数
def nop():
    pass # 占位符，表示什么都不做

# 参数检测
def my_abs2(x):
    """自定义绝对值函数，带参数检测"""
    if not isinstance(x, (int, float)): # 检查参数类型
        raise TypeError('bad operand type') # 抛出类型错误
    if x > 0:
        return x
    else:
        return -x

# 返回多个值
import math

def move(x, y, step, angle=0):
    """移动坐标"""
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny  # 返回多个值，实际上返回的是一个tuple

# 默认参数
def power(x, n=2):
    """计算x的n次方, 默认n=2"""
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

# 默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L

print(add_end()) # ['END']
print(add_end()) # ['END', 'END']
print(add_end()) # ['END', 'END', 'END']

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end2()) # ['END']
print(add_end2()) # ['END']
print(add_end2()) # ['END']

# 可变参数
def calc(*numbers): # 可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3)) # 14

nums = [1,2,3]
print(calc(*nums)) # 14, *nums表示把nums这个list的所有元素作为可变参数传进去

# 关键字参数
def person(name, age, **kw): # kw接受关键字参数，kw是一个dict
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数中
                            # 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineer')
# person2('Jack', 24, 'Beijing', 'Engineer') # 报错，city和job必须用关键字参数传入 

# 命名关键字参数可以有缺省值
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person3('Jack', 24, job='Engineer') # city使用默认值'Beijing'

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person4(name, age, *args, city='Beijing', job):
    print(name, age, args, city, job)

person4('Jack', 24, 'M', job='Engineer')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw): 
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw) 

def f2(a, b, c=0, *, d, **kw): 
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)

# 递归函数
def fact(n):
    """计算阶乘"""
    if n == 1:
        return 1
    return n * fact(n - 1)
