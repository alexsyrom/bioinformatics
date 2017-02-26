fin = open('rosalind_ba1i.txt', 'r')
fout = open('output.txt', 'w')

text = fin.readline()[:-1]
k, d = list(map(int, fin.readline().split()))

from itertools import combinations, product
from collections import Counter

words = Counter()

for index in range(len(text) - k + 1):
    substring = text[index : index + k]
    words[substring] = words[substring] + 1
    for diff in range(1, d + 1):
        for gens in product('ATGC', repeat=diff):
            for holes in combinations(range(k), diff):
                pattern = list(substring)
                for hole, gen in zip(holes, gens):
                    if gen != substring[hole]:
                        pattern[hole] = gen
                    else:
                        break
                else:
                    joined = ''.join(pattern)
                    words[joined] = words[joined] + 1   

max_frequency = words.most_common(1)[0][1]

for key, value in words.items():
    if value == max_frequency:
        print(key, end=' ', file=fout)




