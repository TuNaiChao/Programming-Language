#!/usr/bin/env python3

print("hello python!")

print('100 + 200 =', 100 + 200)

name = input('please enter your name: ')
print('hello,', name)

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('\\\t\\') # 输出 \	\
# Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\') # 输出 \\\t\\

# Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359

print('9 / 3 = ', 9 / 3)   # 除法，结果是浮点数
print('9 // 3 = ', 9 // 3) # 整除，结果是整数
print('9 % 3 = ', 9 % 3)   # 取余

# 字符串
print('ord(\'A\') =', ord('A')) # 获取字符的整数表示，ord()函数获取字符的整数表示
print('chr(65) =', chr(65))     # 获取整数对应的字符，chr()函数获取整数对应的字符
# 格式化
print('%2d-%02d' % (3, 1))  # %2d表示整数至少占2位，%02d表示整数至少占2位，不足2位前面补0
print('%.2f' % 3.1415926)   # %.2f表示小数点后保留2位
print('growth rate: %d %%' % 7) # %%表示一个百分号

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)) # {}表示占位符，冒号后面可以跟格式说明符    

r = 2.5
s = 3.14 * r * r
print(f'半径为{r}的圆的面积是{s:.2f}') # f表示格式化字符串，变量直接写在{}里面

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))      # 获取list的长度
print(classmates[0])        # 获取第一个元素
print(classmates[-1])       # 获取最后一个元素
classmates.append('Adam')   # 追加元素到末尾
classmates.insert(1, 'jack') # 插入元素到指定位置
classmates.pop()      # 删除末尾元素
classmates.pop(1)  # 删除指定位置的元素
classmates[1] = 'Sarah'  # 替换指定位置的元素

L = ['Apple', 123, True]  # list元素的数据类型也可以不同
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))          # list长度
print(s[2][1])        # 取出嵌套的list的元素

L =[]
print(len(L))  # 空list的长度为0

#tuple
t = (1, 2) # 定义一个tuple，tuple一旦初始化就不能修改
print(t[0]) # 取第一个元素  
print(t[-1])    # 取最后一个元素
t = ()  # 定义空的tuple
t = (1,) # 定义只有一个元素的tuple, 需要在元素后面加逗号
t = ('a', 'b', ['A', 'B']) # tuple中的元素不可变，但如果元素是可变对象，比如list，则list中的元素是可以变的

# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

x = 1
if x:
    print('True') # Python中，非0数值、非空字符串、非空list等都被认为是True

s = input('birth: ')
birth = int(s) # 将输入的字符串转换为整数
if birth < 2000:
    print('00前')
else:
    print('00后')

# 模式匹配
'''
age = 15
match age:
    case x if x < 10: # 当age < 10成立时匹配，且赋值给变量x
        print(f'<10 years old: {x}')
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19:
        print(f'10-19 years old: {age}')
    case _: # _表示匹配到其他任何情况
        print('20 years old or older')

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
# 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc',
# 第二个字符串绑定到变量file1，
# 后面的任意个字符串绑定到*files（符号*的作用将在函数的参数中讲解），它实际上表示至少指定一个文件；
'''

# 循环
sum = 0
for x in range(101): # range(101)生成0到100的整数序列
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n 
    n = n -2
print(sum)

n = 1
while n <= 100:
    if n > 10:
        break  # break语句可以提前退出循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue  # continue语句可以跳过当前的这次循环，直接开始下一次循环
    print(n)

# 字典dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} # 定义一个dict
print(d['Michael'])  # 通过key取值

d['Adam'] = 67  # 添加key-value
d['Bob'] = 88   # 修改key-value

'Thomas' in d  # 判断key是否存在
d.get('Thomas')  # 通过key取值，如果不存在返回None
d.get('Thomas', -1) # 通过key取值，如果不存在返回指定的默认值

d.pop('Bob') # 删除key-value

# 集合set
s = {1, 2, 3} # 定义一个set
s = set([1, 2, 3]) # 通过list创建set
s.add(4)    # 添加元素
s.remove(4) # 删除元素

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集

a = 'abc'
print(a.replace('a', 'A')) # replace()方法不会修改字符串a本身，而是返回一个新的字符串
print(a)  # 原字符串仍然是'abc'
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回