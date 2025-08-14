import numpy as np
import matplotlib.pyplot as plt

# 定义爱心形状的参数方程
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# 创建画布并设置背景颜色
plt.figure(figsize=(8, 6), dpi=80)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')  # 关闭坐标轴显示

# 设置线条样式和填充颜色
plt.fill_between(x, y, color="red", alpha=0.7)
plt.plot(x, y, color="darkred", linewidth=2)

# 显示图像
plt.show()