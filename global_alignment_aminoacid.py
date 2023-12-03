import numpy as np

def global_alignment_aminoacids(s, t):
    
    dp = np.zeros((len(s) + 1, len(t) + 1))
    
    for i in range(1, len(s) + 1):
        dp[i][0] = dp[i-1][0] - 5
    for j in range(1, len(t) + 1):
        dp[0][j] = dp[0][j-1] - 5
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            match = dp[i-1][j-1] + blosum62(s[i-1], t[j-1])
            delete = dp[i-1][j] - 5
            insert = dp[i][j-1] - 5
            dp[i][j] = max(match, delete, insert)
    
    align_s = ""
    align_t = ""
    i, j = len(s), len(t)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + blosum62(s[i-1], t[j-1]):
            align_s = s[i-1] + align_s
            align_t = t[j-1] + align_t
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] - 5:
            align_s = s[i-1] + align_s
            align_t = "-" + align_t
            i -= 1
        else:
            align_s = "-" + align_s
            align_t = t[j-1] + align_t
            j -= 1
    
    return align_s, align_t

def blosum62(a, b):
    blosum62_matrix = np.array([
        [4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
        [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
        [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
        [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
        [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
        [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
        [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
        [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
        [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
        [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
        [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
        [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
        [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
        [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
        [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
        [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
        [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
        [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
        [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
        [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]
    ])
    
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return blosum62_matrix[amino_acids.index(a)][amino_acids.index(b)]