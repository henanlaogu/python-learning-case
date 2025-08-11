# 创建一个示例列表
number_list = [5, 3, 8, 1, 9, 2]

#使用内置的sorted函数对列表进行升序排序
sorted_list = sorted(number_list)
print("排序后的列表：", sorted_list)

# 筛选出大于5的元素
num3 = 5
filtered_list = [num for num in sorted_list if num > num3]
print("筛选后的列表：", filtered_list)
