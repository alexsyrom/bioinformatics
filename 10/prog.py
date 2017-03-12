def compute_hamming_distance(first, second):
    distance = 0
    for a, b in zip(first, second):
        if a != b:
            distance += 1
    return distance


def compute_distance(pattern, dna_list):
    k = len(pattern)
    distance = 0
    for text in dna_list:
        hamming_distance = 2 ** 30
        for begin in range(len(text) - k + 1):
            new_hamming_distance = compute_hamming_distance(
                    pattern, text[begin:begin+k])
            if hamming_distance > new_hamming_distance:
                hamming_distance = new_hamming_distance
        distance += hamming_distance
    return distance


if __name__ == '__main__':
    fin = open('rosalind_ba2h.txt', 'r')
    fout = open('output.txt', 'w')
    pattern = fin.readline()[:-1]
    dna_list = fin.readline().split()
    distance = compute_distance(pattern, dna_list)
    fout.write(str(distance))
