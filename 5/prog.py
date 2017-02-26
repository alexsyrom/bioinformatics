from itertools import combinations, product
from collections import Counter


def count_words(text, k, d):
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
    return words


def pair(c):
    pair_dict = {'A':'T',
                 'T':'A',
                 'G':'C',
                 'C':'G'}
    return pair_dict[c]


def comp(text):
    return ''.join(pair(c) for c in reversed(text))


if __name__ == '__main__':
    fin = open('rosalind_ba1j.txt', 'r')
    fout = open('output.txt', 'w')

    text = fin.readline()[:-1]
    k, d = list(map(int, fin.readline().split()))

    words = count_words(text, k, d)
    comp_words = count_words(comp(text), k, d)
    all_words = words + comp_words

    max_frequency = all_words.most_common(1)[0][1]

    for key, value in all_words.items():
        if value == max_frequency:
            print(key, end=' ', file=fout)
