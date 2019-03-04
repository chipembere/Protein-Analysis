from Bio import SeqIO
from itertools import combinations
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

#scoring algorithim

#def score(seq1, seq2):
   # a = 0
    #for pos in range(0, min(len(seq1), len(seq2))):
        #if seq1[pos] == seq2[pos]:
            #a += 2
        #if seq1[pos] != seq2[pos]:
            #a += -1
        #if seq1[pos] == seq2[pos] == '-':
            #a += -2
    #return a

#sequence comparion algorithim

def sequence_compare(file):
    seq_records = SeqIO.parse(file, "fasta")
    for record1, record2 in combinations(seq_records, 2):
        seq1 = record1.seq
        seq2 = record2.seq
        a = score(seq1, seq2)
        #print(sequence1)
        #print(sequence2)
        print(a)

def seq_comp(file):
    seq_r = SeqIO.parse(file, "fasta")
    for record1, record2 in combinations(seq_r, 2):
        seq1 = record1.seq
        seq2 = record2.seq
        alignments = pairwise2.align.globalxx(seq1, seq2)
        print(format_alignment(*alignments[0]))

        
file = "H:\\Desktop\\AdvancedProgramming\\catalyticactivity.fasta"
#print(sequence_compare(file))
seq_comp(file)