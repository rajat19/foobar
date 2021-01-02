def solution(x, y):
    diff = list(set(x) ^ set(y))
    return diff[0]

if __name__ == "__main__":
    x1, y1 = [13, 5, 6, 2, 5], [5, 2, 5, 13]
    print(solution(x1, y1))

    x2, y2 = [14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]
    print(solution(x2, y2))