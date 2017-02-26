fin = open('rosalind_ba1e.txt', 'r')
fout = open('output.txt', 'w')

genome = fin.readline()
k, L, t = list(map(int, fin.readline().split()))
answer = set()

for begin in range(len(genome) - L + 1):
    if genome.count(genome[begin : begin + k], begin, begin + L) >= t:
        answer.add(genome[begin : begin + k])

for elem in answer:
    print(elem, end=' ', file=fout)
