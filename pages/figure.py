
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 使用Mac中的华文黑体
font = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc",size=16)

# 设置随机种子以确保可重复性
np.random.seed(0)

# 生成200个数据点
x = np.arange(200)

# 生成一系列的“真实值”和“预测值”
length = 200
true_values = [12] * length  # 初始化数组
increment = 3  # 每次增加的值
current_value = 12  # 初始值

# 从0到60，每10个增加
for i in range(0, 61):
    if i % 10 == 0 and i != 0:
        current_value += increment
    true_values[i] = current_value

# 从60到200，每20个增加，从60开始不再重复增加
for i in range(60, 200):
    if i % 20 == 0 and i != 60:
        current_value += increment
    true_values[i] = current_value

predictions = true_values + 5 * np.random.randn(200)

plt.figure(figsize=(10, 6))
plt.plot(x, true_values, 'r-', label="标注")  # 红线表示“真实值”
plt.plot(x, predictions, 'b-', label='预测')  # 蓝线表示“预测”
plt.fill_between(x, true_values, predictions, color='gray', alpha=0.1)  # 填充两线之间

# 添加图例、标签、标题和网格
plt.legend(prop=font)  # 使用fontproperties设置图例字体
plt.xlabel('图像序列', fontproperties=font)  # 设置x轴标签
plt.ylabel('车辆覆盖率 (%)', fontproperties=font)  # 设置y轴标签
plt.title('图像序列中的车辆覆盖率', fontproperties=font)  # 设置标题
plt.grid(True)

# 显示图形
plt.show()


