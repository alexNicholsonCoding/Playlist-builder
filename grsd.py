def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    curr_seq = []
    high_seq = []
    ll = len(L)
    start = -1
    end = ll
    for i in L:
        start += 1
        end = ll
        while end > start:
            for a in L[start:end]:
                curr_seq.append(a)

                if sum(curr_seq) > sum(high_seq):
                    high_seq = curr_seq
            curr_seq = []

            end -= 1
    return sum(high_seq)


L = [3, 4, -8, 15, -1, 2]

print(max_contig_sum(L))
print(sum(L))