import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 生成数据集
x = np.linspace(-3, 3, 10)
y = 3 * x + 2

# 将x和y转换为二维数组
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

# 训练线性回归模型
model = linear_model.LinearRegression()
model.fit(x, y)

# 进行预测
x_pred = np.array([[4], [-4]])
y_pred = model.predict(x_pred)

# 绘制生成数据
plt.scatter(x, y, color="blue", label="Generated Data")

# 绘制训练后的回归线
x_plot = np.linspace(-3, 3, 100)
x_plot = x_plot.reshape(-1, 1)
y_plot = model.predict(x_plot)
plt.plot(x_plot, y_plot, color="red", label="Fitted Line")

# 绘制预测点
plt.scatter(x_pred, y_pred, color="green", label="Predicted Points")

# 添加图例
plt.legend()

# 设置图表标题和轴标签
plt.title("Linear Regression Example")
plt.xlabel("X")
plt.ylabel("Y")

# 显示图表
plt.show()
