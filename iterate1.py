from Bio import SeqIO
from itertools import combinations


def score(sequence1, sequence2):
    a = 0
    for pos in range(0, min(len(sequence1), len(sequence2))):
        if sequence1[pos] == sequence2[pos]:
            a += 2
        if sequence1[pos] != sequence2[pos]:
            a += -1
        if sequence1[pos] == sequence2[pos] == '-':
            a += -2
    return a


def sequence_compare(file):
    seq_records = SeqIO.parse(file, "fasta")
    for record1, record2 in combinations(seq_records, 2):
        sequence1 = record1.seq
        sequence2 = record2.seq
        a = score(sequence1, sequence2)
        print(sequence1)
        print(sequence2)
        print(a)

file = "H:\\Desktop\\AdvancedProgramming\\catalyticactivity.fasta"
print(sequence_compare(file))