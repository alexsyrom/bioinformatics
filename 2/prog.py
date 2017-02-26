fin = open('rosalind_ba1f.txt', 'r')
fout = open('output.txt', 'w')

genome = fin.readline()
skew = 0
skews = [0 for i in range(len(genome) + 1)]

for index, gen in enumerate(genome):
    if gen == 'C':
        skew -= 1
    elif gen == 'G':
        skew += 1
    skews[index + 1] = skew

min_skew = min(skews)
for index, skew in enumerate(skews):
    if skew == min_skew:
        print(index, end=' ', file=fout)
