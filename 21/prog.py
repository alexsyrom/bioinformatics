if __name__ == '__main__':
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    N = int(fin.readline())
    coins = list(map(int, fin.readline().split(',')))
    coins.sort()
    dp = [10 ** 10 for j in range(N + 1)]
    dp[0] = 0
    for j in range(1, N + 1):
        for i in range(len(coins)):
            if j < coins[i]:
                break
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    fout.write(str(dp[N]))


