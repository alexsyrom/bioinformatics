if __name__ == '__main__':
    fin = open('rosalind_ba3j.txt', 'r')
    fout = open('output.txt', 'w')
    k, d = list(map(int, fin.readline().split()))
    d += 1
    lines = dict()
    for line in fin.readlines():
        line = ''.join(line.split())
        first, second = line.split('|')
        lines[(first[:k-1], second[:k-1])] = (first[1:k], second[1:k])
    while d > 0:
        newlines = dict()
        for key, value in lines.items():
            if value in lines.keys():
                vv = lines[value]
                newkey = tuple(key[i] + value[i][-1] for i in range(2))
                newvalue = tuple(value[i] + vv[i][-1] for i in range(2))
                newlines[newkey] = newvalue
        d -= 1
        lines = newlines
    lines = {key[0] + key[1]: value[0] + value[1]
             for key, value in lines.items()}
    while len(lines) != 1:
        newlines = dict()
        for key, value in lines.items():
            if value in lines.keys():
                newlines[key + value[-1]] = value[0] + lines[value]
        lines = newlines
    key = list(lines.keys())[0]
    value = lines[key]
    fout.write(key + value[-1])
