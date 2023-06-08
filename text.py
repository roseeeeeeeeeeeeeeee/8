def count_ways(start, end):
    # ��ʼ��ͽ����������
    sx, sy = start
    ex, ey = end
    # ���ߵ�8������������꣩
    directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    # ��¼�ܹ�����ÿ����ķ�ʽ��
    ways = [[0 for _ in range(9)] for _ in range(10)]
    ways[sx][sy] = 1 # ��ʼ��ֻ��һ�ַ�ʽ����
    # ����ÿ����
    for x in range(sx, ex+1):
        for y in range(9):
            # �������ܹ��ߵ�ÿ������
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx < sx or nx > ex or ny < 0 or ny > 8:
                    # Խ������
                    continue
                ways[nx][ny] += ways[x][y] # ͳ�Ƶ��﷽ʽ��
    return ways[ex][ey] # �����ܹ����������ķ�ʽ��

start = (0, 0)
end = (9, 8)
ways = count_ways(start, end)
print("��({},{})��({},{})��{}�ַ�ʽ".format(start[0], start[1], end[0], end[1], ways))