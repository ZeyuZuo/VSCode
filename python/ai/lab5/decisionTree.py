import numpy as np
import pandas as pd

def load_data(filepath):
    data = np.genfromtxt(filepath, delimiter=' ', dtype=float)
    X, y = data[:, :-1], data[:, -1].astype(int)
    return X, y

def calculate_entropy(y):
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / counts.sum()
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def best_split(X, y):
    base_entropy = calculate_entropy(y)
    best_info_gain = 0
    best_feature = None
    best_threshold = None
    
    n_samples, n_features = X.shape
    for feature in range(n_features):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_mask = X[:, feature] <= threshold
            right_mask = ~left_mask
            left_entropy = calculate_entropy(y[left_mask])
            right_entropy = calculate_entropy(y[right_mask])
            weighted_entropy = (left_entropy * left_mask.sum() + right_entropy * right_mask.sum()) / n_samples
            info_gain = base_entropy - weighted_entropy
            
            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    class Node:
        def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
            self.feature = feature
            self.threshold = threshold
            self.left = left
            self.right = right
            self.value = value
    
    def fit(self, X, y, depth=0):
        if len(np.unique(y)) == 1 or (self.max_depth is not None and depth == self.max_depth):
            return self.Node(value=np.bincount(y).argmax())
        feature, threshold = best_split(X, y)
        if feature is None:
            return self.Node(value=np.bincount(y).argmax())

        left_mask = X[:, feature] <= threshold
        left_node = self.fit(X[left_mask], y[left_mask], depth + 1)
        right_node = self.fit(X[~left_mask], y[~left_mask], depth + 1)
        return self.Node(feature=feature, threshold=threshold, left=left_node, right=right_node)

    def predict(self, X):
        node = self.tree
        while node.value is None:
            if X[node.feature] <= node.threshold:
                node = node.left
            else:
                node = node.right
        return node.value

    def fit_predict(self, X_train, y_train, X_test):
        self.tree = self.fit(X_train, y_train)
        predictions = [self.predict(x) for x in X_test]
        return predictions

def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

# Load data
X_train, y_train = load_data('D:\Git\VSCode\python\\ai\lab5\\traindata.txt')
X_test, y_test = load_data('D:\Git\VSCode\python\\ai\lab5\\testdata.txt')

# train_data = pd.read_csv('D:\Git\VSCode\python\\ai\lab5\\traindata.txt', header=None, delim_whitespace=True)
# test_data = pd.read_csv('D:\Git\VSCode\python\\ai\lab5\\testdata.txt', header=None, delim_whitespace=True)

# # Split features and labels
# X_train = train_data.iloc[:, :-1]
# y_train = train_data.iloc[:, -1]
# X_test = test_data.iloc[:, :-1]
# y_test = test_data.iloc[:, -1]

# Initialize and train the decision tree
tree = DecisionTree()  # Example: limited depth to avoid overfitting
y_pred = tree.fit_predict(X_train, y_train, X_test)

# Calculate accuracy
print("Accuracy:", accuracy(y_test, y_pred))

# Visualization code would go here
