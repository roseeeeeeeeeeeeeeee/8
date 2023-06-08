def count_ways(start, end):
    # 起始点和结束点的坐标
    sx, sy = start
    ex, ey = end
    # 马走的8个方向（相对坐标）
    directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    # 记录能够到达每个点的方式数
    ways = [[0 for _ in range(9)] for _ in range(10)]
    ways[sx][sy] = 1 # 起始点只有一种方式到达
    # 遍历每个点
    for x in range(sx, ex+1):
        for y in range(9):
            # 遍历马能够走的每个方向
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx < sx or nx > ex or ny < 0 or ny > 8:
                    # 越界的情况
                    continue
                ways[nx][ny] += ways[x][y] # 统计到达方式数
    return ways[ex][ey] # 返回能够到达结束点的方式数

start = (0, 0)
end = (9, 8)
ways = count_ways(start, end)
print("从({},{})到({},{})有{}种方式".format(start[0], start[1], end[0], end[1], ways))