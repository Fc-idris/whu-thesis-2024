import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 使用Mac中的华文黑体
font = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc", size=16)

def plot_linear_data(slope, r2, max_x, n_points=35844, noise_multiplier=1):
    # 设置随机种子以保证结果可重复
    np.random.seed(0)

    # 分段定义x数据，前10%和后10%的数据量少
    first_segment = int(n_points * 0.05)  # 前5%的点数
    last_segment = int(n_points * 0.95)  # 后5%的点数开始位置

    # 三个区段的x值，使用np.arange确保只有整数值
    x_first = np.arange(0, max_x * 0.1, max_x * 0.1 / first_segment)
    x_middle = np.arange(max_x * 0.1, max_x * 0.9, (max_x * 0.9 - max_x * 0.1) / (n_points - 2 * first_segment))
    x_last = np.arange(max_x * 0.9, max_x, (max_x - max_x * 0.9) / first_segment)

    # 合并x数据
    x = np.concatenate((x_first, x_middle, x_last)).round().astype(int)  # 四舍五入并转换为整数

    # 生成理想的线性y数据
    y_true = slope * x

    # 计算噪声标准差，以确保R^2值
    explained_variance = np.var(y_true) * r2
    noise_variance = np.var(y_true) - explained_variance
    # 增大噪声的标准差来增加方差
    noise_std = np.sqrt(noise_variance / r2) * noise_multiplier

    # 生成噪声并添加到y数据
    noise = np.random.normal(0, noise_std, size=x.shape)
    y_noisy = y_true + noise

    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y_noisy, s=10, alpha=0.5, label='噪声数据')  # 设置数据点大小为10
    plt.plot(x, y_true, color='red', linewidth=2, label='真实关系')
    plt.xlabel('汽车数量', fontproperties=font)
    plt.ylabel('面积', fontproperties=font)
    plt.legend(prop=font)
    plt.grid(True)
    plt.show()

# 调用函数，参数为斜率10.353, R^2值0.9867, x的最大值100
plot_linear_data(slope=10.353, r2=0.9867, max_x=100)
plot_linear_data(slope=18.354, r2=0.9821, max_x=60,n_points=737)
plot_linear_data(slope=42.468, r2=0.9854, max_x=20,n_points=1211)
plot_linear_data(slope=27.323, r2=0.9376, max_x=8,n_points=60)