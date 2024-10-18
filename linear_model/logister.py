# 从Scikit-Learn库导入线性模型中的Logistic回归算法
import numpy as np
from sklearn.linear_model import LogisticRegression

# Scikit-Learn库带有知名的鸢尾花分类数据集，是一个分类问题的数据集
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 载入鸢尾花数据集
X, y = load_iris(return_X_y=True)

# 只选取数据集中的前两个特征进行可视化
X_vis = X[:, :2]  # 取第0列和第1列

# 训练模型
clf = LogisticRegression().fit(X_vis, y)

# 使用模型进行分类预测
res = clf.predict(X_vis)

# 绘制原始数据散点图
plt.scatter(
    X_vis[:, 0], X_vis[:, 1], c=y, cmap="viridis", marker="o", label="Original Data"
)

# 绘制分类边界和预测结果
# 为了绘制分类边界，我们需要生成一个网格并计算每个点的预测结果

# 创建网格
x_min, x_max = X_vis[:, 0].min() - 1, X_vis[:, 0].max() + 1
y_min, y_max = X_vis[:, 1].min() - 1, X_vis[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 绘制决策边界
plt.contourf(xx, yy, Z, alpha=0.8, cmap="viridis")

# 显示图表
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Logistic Regression on Iris Dataset")
plt.legend()
plt.show()
