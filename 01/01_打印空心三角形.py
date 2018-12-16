
# 打印空心三角形
# 用i 控制三角形的横向行
for i in range(5):
    # 用j控制三角形每一行的列
    for j in range(i+1):
        # 当i =0 或者i =4 代表在第一行或者最后一行的时候完整输出星号
        if i == 0 or i == 4:
            print("*",end=" ")
        # 当 j 等于第一行或者当前的行号等于当前的列号时,打印星号
        elif j == 0 or j == i:
            print("*",end=" ")
        # 否则,打印空号
        else:
            print(" ",end=" ")
    print()
