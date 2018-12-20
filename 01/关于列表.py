# 关于列表排序
cars = ['bmw',"audi","toyota","subaru"]
cars.sort()  # 永久性正序排列列表
print(cars)
cars.sort(reverse=True)  # 永久性倒序排列列表,括号传入参数reverse=True
print(cars)
lists = ["f","b","c","d"]
print(sorted(lists))  # 临时正序排列
print(sorted(lists,reverse=True))  # 临时倒序排列 注意括号内参数传入的位置
print(lists)   # 此条证明上一条代码为临时排序


cars1 = ['bmw',"audi","toyota","subaru"]
print(cars1)
cars1.reverse()   # 永久按列表原有顺序倒序排列,
print(cars1)

list1 = ["1","2","3","4"]
print(len(list1))  # 获取列表长度(包含元素个数)


