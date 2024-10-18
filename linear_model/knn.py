# 第一步：导包
import numpy as np
import matplotlib.pyplot as plt

# 第二步：设置数据集
# 2.1样本特征值
data_x = [
    [1.3, 6],
    [3.5, 5],
    [4.2, 2],
    [5, 3.3],
    [2, 9],
    [5, 7.5],
    [7.2, 4],
    [8.1, 8],
    [9, 2.5],
]
# 2.2样本的标记值
data_y = [0, 1, 1, 1, 1, 1, 1, 1, 1]
# 2.3将上述两个数组转化为array形式（同时作为训练集）
X_train = np.array(data_x)
Y_train = np.array(data_y)

# 第三步：绘制散点图
# 3.1绘制样本为true的散点图
plt.scatter(
    X_train[Y_train == 0, 0],
    X_train[Y_train == 0, 1],
    color="red",
    marker="x",
    label="正确样本",
)
# 3.2绘制样本为false的散点图
plt.scatter(
    X_train[Y_train == 1, 0],
    X_train[Y_train == 1, 1],
    color="blue",
    marker="o",
    label="错误样本",
)
plt.title("散点图绘制教程")
plt.xlabel("横坐标")
plt.ylabel("纵坐标")
from pylab import mpl

# 设置中文显示字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# 为不同类别指定不同的颜色
colors = {"正确样本": "red", "错误样本": "blue"}
plt.legend()
plt.show()
# 第四步：现在给你一个新点，如何判断它应该画成什么颜色呢
# 4.1新的样本点以及它在图中的位置
data_new = np.array([4, 5])
plt.scatter(data_new[0], data_new[1], color="black", marker="^")
# 4.2计算新样本点与原有样本点之间的距离
"""
for data in X_train:
    print(np.sqrt(np.sum((data-data_new)**2)))
"""
# 用简化版
result_distance = [np.sqrt(np.sum((data - data_new) ** 2)) for data in X_train]
# 接着我们需要按照距离的远近进行排序
sort_index = np.argsort(result_distance)  # 得到的将会是从小到大排序后的索引下标值
# 4.3选择k值
k = 5
k_data = [
    Y_train[i] for i in sort_index[0:k]
]  # 将前k个数据的标签值获取到,得到[0, 0, 1, 0, 0]
# 4.4计算各类别投票个数
from collections import Counter

Counter(k_data)  # 得到Counter({0: 4, 1: 1})属于字典形式，表示0标签有4个，1标签有1个
Counter(k_data).most_common()  # 得到[(0, 4), (1, 1)]，变成元组形式
Counter(k_data).most_common(1)  # 得到[(0, 4)]，代表选出投票最多的那个元组
final_result = Counter(k_data).most_common(1)[0][
    0
]  # 得到0，也就是得到第一行数据的第一个值，也就是标签值
print(final_result)
