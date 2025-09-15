#!/usr/bin/env python3
import sys
from collections import deque

# 读取地图文件，返回一个二维数组（grid）
def read_map(file_path):
    grid = []
    with open(file_path, "r") as f:
        for line in f:
            # 每一行按空格分割，并转成整数
            row = list(map(int, line.strip().split()))
            grid.append(row)
    return grid

# 广度优先搜索（BFS），寻找从 start 到 goal 的路径
def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])  # 地图的行数和列数
    sx, sy = start
    gx, gy = goal

    # 边界检查：起点或终点越界/在障碍物上 → 不可达
    if not (0 <= sx < rows and 0 <= sy < cols):
        return None
    if not (0 <= gx < rows and 0 <= gy < cols):
        return None
    if grid[sx][sy] == 1 or grid[gx][gy] == 1:
        return None

    # visited 记录是否访问过，parent 记录上一个节点
    visited = [[False]*cols for _ in range(rows)]
    parent = [[None]*cols for _ in range(rows)]
    
    # BFS 队列，初始放入起点
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    # 四个方向：上下左右
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()

        # 如果到达目标点，回溯路径
        if (x, y) == (gx, gy):
            path = []
            while (x, y) is not None:
                path.append((x, y))           # 加入路径
                if parent[x][y] is None:  # 如果没有父节点了，说明到达起点
                    break
                x, y = parent[x][y]  # parent[x][y] 最后会是 None，循环就结束
            return path[::-1]                 # 反转成从起点到终点

        # 遍历四个方向
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols:     # 边界检查
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)           # 记录父节点
                    q.append((nx, ny))                # 加入队列

    return None  # 没有找到路径

# 打印地图，并在路径上标记 *
def print_map(grid, path):
    path_set = set(path)   # 把路径放进集合，方便判断
    for i in range(len(grid)):
        line = ""
        for j in range(len(grid[0])):
            if (i, j) in path_set:    # 如果是路径上的点，画 *
                line += "* "
            else:                     # 否则保持原样
                line += str(grid[i][j]) + " "
        print(line.strip())

if __name__ == "__main__":
    # 命令行参数格式检查
    if len(sys.argv) != 6:
        print("Usage: ./pathfinder.py <map_file> <start_x> <start_y> <goal_x> <goal_y>")
        sys.exit(1)

    # 读取命令行参数
    map_file = sys.argv[1]
    start_x, start_y = int(sys.argv[2]), int(sys.argv[3])
    goal_x, goal_y = int(sys.argv[4]), int(sys.argv[5])

    # 读入地图
    grid = read_map(map_file)

    # 执行 BFS
    path = bfs(grid, (start_x, start_y), (goal_x, goal_y))

    # 输出结果
    if path:
        print_map(grid, path)
    else:
        print(f"I can't go to the postion ({goal_x},{goal_y}).")
