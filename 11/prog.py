if __name__ == '__main__':
    fin = open('rosalind_ba3h.txt', 'r')
    fout = open('output.txt', 'w')
    k = int(fin.readline())
    lines = {line[:k-1]: line[1:k] for line in fin.readlines()}
    while len(lines) != 1:
        newlines = dict()
        for key, value in lines.items():
            if value in lines.keys():
                newlines[key + value[-1]] = value[0] + lines[value]
        lines = newlines
    key = list(lines.keys())[0]
    value = lines[key]
    fout.write(key + value[-1])
