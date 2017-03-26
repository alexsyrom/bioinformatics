if __name__ == '__main__':
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    k = int(fin.readline())
    s = ['1' for i in range(k)]
    counts = set()
    counts.add('1' * k)
    need = 2 ** k
    have = 1
    while have < need:
        ss = s[-k+1:]
        if ''.join(ss) + '0' in counts:
            if ''.join(ss) + '1' not in counts:
                have += 1
                counts.add(''.join(ss) + '1')
            s.append('1')
        else:
            s.append('0')
            have += 1
            counts.add(''.join(ss) + '0')
    fout.write(''.join(s[:-k+1]))
