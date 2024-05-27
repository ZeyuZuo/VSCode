import math
import random

# 目标函数
def func(x):
    return 11 * math.sin(6 * x) + 7 * math.cos(5 * x)

# 生成新解的邻域函数
def get_neighbor(x, step):
    return x + (random.random() * 2 - 1) * step

# 模拟退火算法
def simulated_annealing(init_temp, min_temp, alpha, max_iter):
    # 初始化
    curr_temp = init_temp
    curr_sol = random.random() * 2 * math.pi  # 初始解在[0, 2π]范围内随机生成
    best_sol = curr_sol
    best_score = func(best_sol)

    # 开始迭代
    for i in range(max_iter):
        # 生成新解
        neighbor = get_neighbor(curr_sol, 1)  # 步长为1
        neighbor_score = func(neighbor)

        # 计算接受概率
        ap = math.exp((best_score - neighbor_score) / curr_temp)

        # 决策是否接受新解
        if ap > random.random():
            curr_sol = neighbor
            if neighbor_score < best_score:
                best_sol = neighbor
                best_score = neighbor_score

        # 降温
        curr_temp = curr_temp * alpha

    return best_sol, best_score

# 主函数
if __name__ == "__main__":
    # 设置算法参数
    init_temp = 100  # 初始温度
    min_temp = 1e-8  # 终止温度
    alpha = 0.99     # 冷却速率
    max_iter = 10000 # 最大迭代次数

    # 执行模拟退火算法
    best_sol, best_score = simulated_annealing(init_temp, min_temp, alpha, max_iter)

    # 输出结果
    print(f"最小值为: {best_score:.6f}")
    print(f"对应的自变量值为: {best_sol:.6f}")