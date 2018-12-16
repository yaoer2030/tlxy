import math
# 向上取整数,
print(math.ceil(5.5))

# 向下取整数,用floor
print(math.floor(5.1))

# 查看系统保留关键字,这些关键字不能做变量名
import keyword
print(keyword.kwlist)

# 四舍五入用round
print(round(5.6))
print(round(5.4))

# sqrt 开平方 返回浮点数
print(math.sqrt(4))

# pow 跟幂运算差不多,计算一个数的几次方
print(math.pow(3,4))    # 第一个参数是需要计算的数字,第二个参数为多少次方,返回浮点数
print(3**4)    # 表示3的4次方,返回整数

# fabs 对一个数取绝对值,返回绝对值

print(math.fabs(-1))
print(math.fabs(3))

# fsum 对整个序列求和,返回浮点数
print(math.fsum([1,5,8,6,32]))

# sum 内置求和,返回值由本身类型而定
print(sum([1,5,6,9,8,7,5]))




