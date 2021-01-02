def solution(n):
    arr = [None]*(n+1)
    for i in range(n+1):
        arr[i] = [None]*(n+1)
        for j in range(n+1):
            arr[i][j] = 0
    
    arr[0][0] = 1
    for i in range(1, n+1):
        for j in range(n+1):
            arr[i][j] = arr[i-1][j]
            if j >= i:
                arr[i][j] += arr[i-1][j-i]
    return arr[n][n] - 1

    if __name__ == "__main__":
        n1 = 3
        print(solution(n1))

        n2 = 200
        print(solution(n2))