class Station:
    def __init__(self, m):
        self.map = m
        self.width = len(m[0])
        self.height = len(m)

    def get_paths(self, sx, sy):
        board = [[None for i in range(self.width)] for i in range(self.height)]
        board[sx][sy] = 1

        q = [(sx, sy)]
        while len(q) > 0:
            x, y = q.pop(0)
            for i in [(1,0),(-1,0),(0,-1),(0,1)]:
                nx, ny = x + i[0], y + i[1]
                if 0 <= nx < self.height and 0 <= ny < self.width:
                    if board[nx][ny] is None:
                        board[nx][ny] = board[x][y] + 1
                        if self.map[nx][ny] == 1:
                            continue
                        q.append((nx, ny))
                    
        return board

def solution(map):
    station = Station(map)
    start_board = station.get_paths(0, 0)
    end_board = station.get_paths(station.height - 1, station.width - 1)
    board = []
    res = float('inf')
    for i in range(station.height):
        for j in range(station.width):
            if start_board[i][j] and end_board[i][j]:
                res = min(start_board[i][j] + end_board[i][j] - 1, res)
    return res

if __name__ == "__main__":
    map1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    print(solution(map1))

    map2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    print(solution(map2))