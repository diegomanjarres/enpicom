from Bio import SeqIO

def reverse(seq):
    return seq[::-1]

def complement(seq):
    comp = ''
    for b in seq:
        if b =='A':
            comp = comp + 'T'
        elif b == 'T':
            comp = comp + 'A'
        elif b == 'C':
            comp = comp + 'G'
        else:
            comp = comp + 'C'
    return comp

def isInDict(seq, dict):
    for k in dict.keys():
        if seq == k or seq == reverse(complement(k)):
            return True
    return False

def getCorrection(incorrect,correct):
    rc_correct = reverse(complement(correct))
    err_count = 0
    rc_err_count = 0
    correction = ''
    rc_correction = ''
    for i, c in enumerate(incorrect):
        # With original read
        if c == correct[i] and err_count <= 1:
            correction = correction + c
        else:
            err_count = err_count + 1
            correction = correction + correct[i]
        # With reverse complement
        if c == rc_correct[i] and rc_err_count <=1:
            rc_correction = rc_correction + c
        else:
            rc_err_count = rc_err_count +1
            rc_correction = rc_correction + rc_correct[i]

        if err_count > 1 and rc_err_count >1:
            return False, ''
    
    if err_count < rc_err_count:
        return True, correction
    else:
        return True, rc_correction


def main():
    seq_dict = {}
    correct = []
    fasta_sequences = SeqIO.parse(open('input.fasta'),'fasta')

    # Track observed occurrences
    for fasta in fasta_sequences:
        sequence = str(fasta.seq)
        if isInDict(sequence,seq_dict):
            seq_dict[sequence] = 1
            continue
        seq_dict[sequence] = 0

    # Get correct reads
    for k,v in seq_dict.items():
        if v == 1:
            correct.append(k)

    # Print corrections
    for k,v in seq_dict.items():
        if v == 1:
            continue
        for corr in correct:
            close_enough, correction = getCorrection(k,corr)
            if close_enough and k != correction:
                print(k+'->'+correction)
                break

main()