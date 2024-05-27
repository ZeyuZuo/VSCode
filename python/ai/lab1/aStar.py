import heapq

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()  # Newline for better readability between moves

def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        x1, y1 = divmod(state.index(num), 3)
        x2, y2 = divmod(goal.index(num), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def successors(state):
    index = state.index(0)
    moves = []
    if index % 3 != 0:  # Not on the left edge
        moves.append(index - 1)
    if index % 3 != 2:  # Not on the right edge
        moves.append(index + 1)
    if index >= 3:  # Not on the top edge
        moves.append(index - 3)
    if index < 6:  # Not on the bottom edge
        moves.append(index + 3)
    for move in moves:
        new_state = state[:]
        new_state[index], new_state[move] = new_state[move], new_state[index]
        yield new_state

def a_star(initial, goal):
    open_heap = []
    heapq.heappush(open_heap, (0 + manhattan_distance(initial, goal), 0, initial))
    visited = set()
    while open_heap:
        _, cost, current = heapq.heappop(open_heap)
        print("Current board state with cost", cost)
        print_board(current)  # Print the current board state
        if current == goal:
            return cost  # Return the number of moves
        if tuple(current) in visited:
            continue
        visited.add(tuple(current))
        for state in successors(current):
            heapq.heappush(open_heap, (cost + 1 + manhattan_distance(state, goal), cost + 1, state))

# 初始状态和目标状态
initial = [2, 8, 3, 1, 6, 4, 7, 0, 5]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# 调用A*算法
moves = a_star(initial, goal)
print(f"Required moves: {moves}")
