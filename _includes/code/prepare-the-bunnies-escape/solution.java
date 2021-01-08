import java.util.List;
import java.util.ListIterator;
import java.util.ArrayList;
import java.util.Arrays;

class Point {
    int x;
    int y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Station {
    int[][] map;
    int width;
    int height;
    
    Station(int[][] map) {
        this.map = map;
        this.height = map.length;
        this.width = map[0].length;
    }

    public int[][] getPaths(int sx, int sy) {
        int[][] board = new int[this.height][this.width];
        for (int i = 0; i < this.height; i++) {
            for (int j = 0; j < this.width; j++) {
                board[i][j] = -1;
            }
        }
        board[sx][sy] = 1;
        List<Point> points = new ArrayList<>();
        points.add(new Point(sx, sy));
        ListIterator<Point> it = points.listIterator();
        List<Point> directions = Arrays.asList(
            new Point(1, 0),
            new Point(-1, 0),
            new Point(0, -1),
            new Point(0, 1)
        );
        while(it.hasNext()) {
            Point p = it.next();
            for(Point d: directions) {
                int nx = p.x + d.x, ny = p.y + d.y;
                if (nx >= 0 && nx < this.height && ny >= 0 && ny < this.width) {
                    if (board[nx][ny] == -1) {
                        board[nx][ny] = board[x][y] + 1;
                        if (this.map[nx][ny] == 1) continue;
                        it.add(new Point(nx, ny));
                    }
                }
            }
        }
        return board;
    }
}


class Solution {
    public static int solution(int[][] map) {
        Station station = new Station(map);
        int[][] startBoard = station.getPaths(0, 0);
        int[][] endBoard = station.getPaths(station.height - 1, station.width - 1);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < station.height; i++) {
            for (int j = 0; j < station.width; j++) {
                if (startBoard[i][j] > 0 && endBoard[i][j] > 0) {
                    res = Math.min(startBoard[i][j] + endBoard[i][j] - 1, res);
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[][] map1 = { {0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0} };
        System.out.println(Solution.solution(map1));

        int[][] map2 = { {0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0} };
        System.out.println(Solution.solution(map2));
    }
}