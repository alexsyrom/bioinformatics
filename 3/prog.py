fin = open('rosalind_ba1h.txt', 'r')
fout = open('output.txt', 'w')

pattern = fin.readline()[:-1]
text = fin.readline()[:-1]
d = int(fin.readline())

for index in range(len(text) - len(pattern) + 1):
    substring = text[index : index + len(pattern)]
    diff = 0
    for pattern_char, text_char in zip(pattern, substring):
        if pattern_char != text_char:
            diff += 1
            if diff > d:
                break
    else:
        print(index, end=' ', file=fout)

