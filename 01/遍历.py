# 遍历一个列表
list1 = ["1","2","3","4"]
for i in list1:  # 不要忘记冒号,否则报错
    print(i)

# 使用list()函数将range()作为参数传递生成列表
numbers = list(range(6))
print(numbers)


# 创建一个值为1-10的平方的列表
list1 = []
for value in range(1,11): # 0的平方没有意义,所以从1开始
    list1.append(value**2)  # 调用方法append
print(list1)

# 下面代码和上面代码同效
list1 = [value**3 for value in range(1,11)]  # value**2 是表达式
print(list1)
