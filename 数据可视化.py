import matplotlib.pyplot as plt

# 假设的一个月内每天的销售额数据（示例数据，可根据实际情况修改）
sales_data = [100, 120, 90, 110, 130, 140, 120, 150, 160, 140, 130, 170, 180, 190, 200, 180, 170, 160, 150, 140, 130,
              120, 110, 100, 90, 80, 70, 60, 50]

# 设置横坐标标签（这里是日期，简单用数字表示天数）
days = list(range(1, len(sales_data) + 1))

# 绘制折线图
plt.plot(days, sales_data)

# 添加标题和坐标轴标签
plt.title("一个月内每天的销售额变化趋势")
plt.xlabel("天数")
plt.ylabel("销售额")

# 显示图形
plt.show()