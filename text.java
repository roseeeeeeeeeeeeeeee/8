
public class Chess {
    private static final int[][] directions = {{-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}, {1, -2}, {2, -1}, {2, 1}, {1, 2}}; // ���ߵ�8������������꣩

    public static int countWays(int sx, int sy, int ex, int ey) {
        int[][] ways = new int[10][9]; // ��¼�ܹ�����ÿ����ķ�ʽ��
        ways[sx][sy] = 1; // ��ʼ��ֻ��һ�ַ�ʽ����
        // ����ÿ����
        for (int x = sx; x <= ex; x++) {
            for (int y = 0; y <= 8; y++) {
                // �������ܹ��ߵ�ÿ������
                for (int[] direction : directions) {
                    int dx = direction[0], dy = direction[1];
                    int nx = x + dx, ny = y + dy;
                    if (nx < sx || nx > ex || ny < 0 || ny > 8) { // Խ������
                        continue;
                    }
                    ways[nx][ny] += ways[x][y]; // ͳ�Ƶ��﷽ʽ��
                }
            }
        }
        return ways[ex][ey]; // �����ܹ����������ķ�ʽ��
    }

    public static void main(String[] args) {
        int ways = countWays(0, 0, 9, 8);
        System.out.printf("��(%d,%d)��(%d,%d)��%d�ַ�ʽ", 0, 0, 9, 8, ways);
    }
}