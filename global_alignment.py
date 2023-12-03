def global_alignment_dna(seq1, seq2, match_score=1, mismatch_score=-3, gap_penalty=-2):
    matrix = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

    for i in range(1, len(seq1) + 1):
        matrix[i][0] = gap_penalty * i
    for j in range(1, len(seq2) + 1):
        matrix[0][j] = gap_penalty * j

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            score = match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score
            diagonal = matrix[i - 1][j - 1] + score
            up = matrix[i - 1][j] + gap_penalty
            left = matrix[i][j - 1] + gap_penalty
            matrix[i][j] = max(diagonal, up, left)

    align_seq1 = ''
    align_seq2 = ''
    i = len(seq1)
    j = len(seq2)
    while i > 0 and j > 0:
        if matrix[i][j] == matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
            align_seq1 = seq1[i - 1] + align_seq1
            align_seq2 = seq2[j - 1] + align_seq2
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i - 1][j] + gap_penalty:
            align_seq1 = seq1[i - 1] + align_seq1
            align_seq2 = "-" + align_seq2
            i -= 1
        else:
            align_seq1 = "-" + align_seq1
            align_seq2 = seq2[j - 1] + align_seq2
            j -= 1

    while i > 0:
        align_seq1 = seq1[i - 1] + align_seq1
        align_seq2 = "-" + align_seq2
        i -= 1
    while j > 0:
        align_seq1 = "-" + align_seq1
        align_seq2 = seq2[j - 1] + align_seq2
        j -= 1

    return align_seq1, align_seq2