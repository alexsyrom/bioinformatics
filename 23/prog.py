from Bio.SubsMat import MatrixInfo
blosum = MatrixInfo.blosum62


if __name__ == '__main__':
    fin = open('rosalind_ba5e.txt', 'r')
    fout = open('output.txt', 'w')
    s = fin.readline().strip()
    t = fin.readline().strip()
    dp = [[-5 * max(i, j) for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) - 5
            pair = (s[i], t[j])
            if pair in blosum:
                sc = blosum[pair]
            else:
                sc = blosum[pair[::-1]]
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + sc)
    fout.write('{}\n'.format(dp[len(s)][len(t)]))
    result = []
    i = len(s)
    j = len(t)
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] - 5:
            result.append((s[i - 1], '-'))
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] - 5:
            result.append(('-', t[j - 1]))
            j -= 1
        else:
            result.append((s[i - 1], t[j - 1]))
            i -= 1
            j -= 1
    result = result[::-1]
    S = ''.join(x[0] for x in result)
    T = ''.join(x[1] for x in result)
    fout.write('{}\n{}'.format(S, T))

