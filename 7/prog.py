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


def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(x) for x in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count


def profile(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[(col.count(nuc) + 1) / (len(col) + 4) for nuc in 'ACGT']
            for col in columns]


def greedy_motif_search(dna_list, k, t):
    best_score = t*k

    for i in range(len(dna_list[0])-k+1):
        motifs = [dna_list[0][i:i+k]]
        for j in range(1, t):
            current_profile = profile(motifs)
            motifs.append(profile_kmer(dna_list[j], k, current_profile))
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


if __name__ == '__main__':
    fin = open('rosalind_ba2e.txt', 'r')
    fout = open('output.txt', 'w')
    k, t = map(int, fin.readline().split())
    dna_list = [line.strip() for line in fin]
    best_motifs = greedy_motif_search(dna_list, k, t)
    fout.write('\n'.join(best_motifs))
