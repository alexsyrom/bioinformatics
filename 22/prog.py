if __name__ == '__main__':
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    n, m = list(map(int, fin.readline().split()))
    down = [[0 for j in range(m + 1)] for i in range(n)]
    right = [[0 for j in range(m)] for i in range(n + 1)]
    for i in range(n):
        down[i] = list(map(int, fin.readline().split()))
    fin.readline()
    for i in range(n + 1):
        right[i] = list(map(int, fin.readline().split()))
    
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + down[i - 1][0]
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + right[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j] + down[i - 1][j], 
                           dp[i][j - 1] + right[i][j - 1])
    fout.write(str(dp[n][m]))


