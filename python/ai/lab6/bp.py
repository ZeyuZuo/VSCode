import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score

# 激活函数及其导数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 数据预处理
def load_data(filename):
    data = pd.read_csv(filename, header=None)
    data.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # 标签编码，转换为独热编码
    encoder = OneHotEncoder(sparse_output=False)  # Use sparse_output instead of sparse
    y_encoded = encoder.fit_transform(y.reshape(-1, 1))

    # 特征缩放
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y_encoded, test_size=0.5, random_state=1)

X_train, X_test, y_train, y_test = load_data('D:\Git\VSCode\python\\ai\lab6\Iris.txt')

# 网络参数初始化
input_size = X_train.shape[1]
hidden_size = 10
output_size = y_train.shape[1]  # 根据目标类别数设置输出层大小
learning_rate = 0.01

np.random.seed(1)
weights_input_hidden = np.random.normal(scale=0.1, size=(input_size, hidden_size))
bias_hidden = np.zeros(hidden_size)
weights_hidden_output = np.random.normal(scale=0.1, size=(hidden_size, output_size))
bias_output = np.zeros(output_size)

# 训练网络
for epoch in range(1000):
    # 前向传播
    hidden_layer_input = np.dot(X_train, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    # 计算误差
    error = y_train - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    # 反向传播
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # 更新权重和偏置
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    bias_output += np.sum(d_predicted_output, axis=0) * learning_rate
    weights_input_hidden += X_train.T.dot(d_hidden_layer) * learning_rate
    bias_hidden += np.sum(d_hidden_layer, axis=0) * learning_rate

# 测试网络
hidden_layer_input = np.dot(X_test, weights_input_hidden) + bias_hidden
hidden_layer_output = sigmoid(hidden_layer_input)
output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
predicted_output = sigmoid(output_layer_input)
predictions = np.argmax(predicted_output, axis=1)
true_labels = np.argmax(y_test, axis=1)

# 计算准确率
accuracy = accuracy_score(true_labels, predictions)
print(f'Accuracy: {accuracy * 100:.2f}%')
