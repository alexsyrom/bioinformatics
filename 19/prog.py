import gc

peptide_mass = {
    'A':   71.0788,
    'C':   103.1388,
    'D':   115.0886,
    'E':   129.1155,
    'F':   147.1766,
    'G':   57.0519,
    'H':   137.1411,
    'L':   113.1594,
    'M':   131.1986,
    'N':   114.1039,
    'P':   97.1167,
    'Q':   128.1307,
    'R':   156.1875,
    'S':   87.0782,
    'T':   101.1051,
    'V':   99.1326,
    'W':   186.2132,
    'Y':   163.1760
}


def expand(peptides):
    result = []
    for key, value in peptide_mass.items():
        for peptide in peptides:
            result.append(peptide + (int(value),))
    return result


def compute_mass(peptide):
    return sum(int(x) for x in peptide)


def parentmass(masses):
    return max(masses)


def compute_spectrum(peptide):
    result = [0,]
    int_sum = [0 for x in peptide]
    int_sum.append(0)
    for i in range(1, len(peptide) + 1):
        int_sum[i] = int_sum[i - 1] + peptide[i - 1]
    for length in range(len(peptide)):
        for begin in range(len(peptide) - length + 1):
            result.append(int_sum[begin + length] - int_sum[begin])
    result.sort()
    return result


def score(peptide, masses):
    spectrum = compute_spectrum(peptide)
    i = 0
    j = 0
    result = 0
    while i < len(masses) and j < len(spectrum):
        if masses[i] == spectrum[j]:
            result += 1
            i += 1
            j += 1
        elif masses[i] < spectrum[j]:
            i += 1
        else:
            j += 1
    return result


def lcs(masses, N):
    leaderboard = [()]
    leaderpeptide = ()
    leader_score = score(leaderpeptide, masses)
    parent_mass = parentmass(masses)
    while leaderboard:
        leaderboard = expand(leaderboard)
        gc.collect()
        masses_x = [compute_mass(x) for x in leaderboard]
        leaderboard = [x for x, mass in zip(leaderboard, masses_x) if mass <= parent_mass]
        masses_x = [compute_mass(x) for x in leaderboard]
        scores = [score(x, masses) for x in leaderboard]
        for peptide, score_x, mass_x in zip(leaderboard, scores, masses_x):
            if mass_x == parent_mass and score_x > leader_score:
                leaderpeptide = peptide
                leader_score = score_x
        leaderboard_pairs = list(zip(leaderboard, scores))
        leaderboard_pairs.sort(key=lambda x: -x[1])
        if len(leaderboard_pairs) > N:
            leaderboard = [x for x, s in leaderboard_pairs if s <= leaderboard_pairs[N - 1][1]]
    return leaderpeptide


if __name__ == '__main__':
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
    N = int(fin.readline())
    masses = list(map(int, fin.readline().split()))
    print('-'.join(str(x) for x in lcs(masses, N)), file=fout)
