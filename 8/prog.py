from numpy.random import randint


def profile_kmer(dna, k, profile):
    nuc_loc = {nucleotide: index for index, nucleotide in enumerate('ACGT')}
    max_probability = -1

    for i in range(len(dna)-k+1):
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]
        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable


def motifs_from_profile(dna, k, profile):
    return [profile_kmer(seq, k, profile) for seq in dna]


def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(x) for x in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[(col.count(nuc) + 1) / (len(col) + 4) for nuc in 'ACGT']
            for col in columns]


def greedy_motif_search(dna_list, k, t):
    rand_ints = [randint(0, len(dna_list[0])-k) for a in range(t)]
    motifs = [dna_list[i][r:r+k] for i, r in enumerate(rand_ints)]
    best_score = [score(motifs), motifs]
    while True:
        current_profile = profile(motifs)
        motifs = motifs_from_profile(dna_list, k, current_profile)
        current_score = score(motifs)
        if current_score < best_score[0]:
            best_score = [current_score, motifs]
        else:
            return best_score


if __name__ == '__main__':
    fin = open('rosalind_ba2f.txt', 'r')
    fout = open('output.txt', 'w')
    k, t = map(int, fin.readline().split())
    dna_list = [line.strip() for line in fin]
    best_motifs = greedy_motif_search(dna_list, k, t)
    for i in range(1, 1000):
        new_motifs = greedy_motif_search(dna_list, k, t)
        if new_motifs[0] < best_motifs[0]:
            best_motifs = new_motifs
    fout.write('\n'.join(best_motifs[1]))
