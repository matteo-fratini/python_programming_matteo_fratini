
			
def find_max(scores):
    max_score = max(scores)
    max_path = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            max_score = scores[i]
            max_path.append(i)
    return(max_score, max_path)

def print_matrix(M):
    for row in M:
        print(row)


    
    s = { "A":{"A":2, "G":1, "C":0, "T":0},\
                "G":{"A":1, "G":2, "C":0, "T":0},\
                "C":{"A":0, "G":0, "C":2, "T":1},\
                "T":{"A":0, "G":0, "C":1, "T":2}}
    d = 2
    seq1 = "ATGCCTA"
    seq2 = "CTGAA"
    n1 = len(seq1)
    n2 = len(seq2)
    M = [[0 for i in range(n2)] for y in range(n1)]
    B = [[0 for i in range(n2 - 1)] for y in range(n1 - 1)]


    M[0] = [-d*i for i in range(n2)]
    first_col = [-d*i for i in range(n1)]
    for row in range(n1):
        M[row][0] = first_col[row]

    for row in range(1, n1):
        for col in range(1, n2):
            gap1 = M[row][col - 1] - d
            gap2 = M[row - 1][col] - d
            match = M[row - 1][col - 1] + s[seq1[row]][seq2[col]]
            max_score, max_path = find_max([gap1, gap2, match])
            M[row][col] = max_score
            B[row - 1][col - 1] = max_path
    print_matrix(M)
    print_matrix(B)
    
    pointer_row = len(B) - 1
    pointer_col = len(B[0]) - 1
    alignment = {"seq1":"", "seq2":""}
    while pointer_row != -1 and pointer_col != -1:
        backtrace = B[pointer_row][pointer_col]
        trace = backtrace[len(backtrace) - 1]
        if trace == 0:
            alignment["seq1"] = alignment["seq1"] + "-"
            alignment["seq2"] = alignment["seq2"] + seq2[pointer_col + 1]
            pointer_col += -1
        elif trace == 1:
            alignment["seq1"] = alignment["seq1"] + seq1[pointer_row + 1]
            alignment["seq2"] = alignment["seq2"] + "-"
            pointer_row += -1
        elif trace == 2:
            alignment["seq1"] = alignment["seq1"] + seq1[pointer_row + 1]
            alignment["seq2"] = alignment["seq2"] + seq2[pointer_col + 1]
            pointer_col += -1
            pointer_row += -1

    alignment["seq1"] = alignment["seq1"][::-1]
    alignment["seq2"] = alignment["seq2"][::-1]

    print(alignment["seq1"])
    print(alignment["seq2"])