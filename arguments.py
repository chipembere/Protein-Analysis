import sys
from Bio import SeqIO
from Bio import SeqFeature
from itertools import combinations
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import AlignIO
import texttable as tt

#limit the number of proteins gathered
limit_results = 5 #could be argument 3
tei = []
count = 0
tab = tt.Texttable()

##path to Uniprot XML file##
uniprot_xml = sys.argv[1]
#comment = sys.argv[2]
f = open(uniprot_xml)
f = SeqIO.parse(f, "uniprot-xml")

#find proteins invloved in some similar activity/function from Uniprot XML
for entry in f:
    #print(entry.annotations['keywords'])
    if ("comment_function" in entry.annotations.keys()):
        value = entry.annotations["comment_function"]
        
        new_found = [sys.argv[2] in i for i in value]
        a_va = any(new_found)
                
        if a_va:
            tei.append(entry)
            count += 1
            if (count == limit_results):
                break

path = sys.argv[2] + ".fasta"
f = open(path, 'w')
SeqIO.write(tei, f, "fasta")

#Put the locations/keywords of the proteins in a table
for entry in tei:
    if ("comment_subcellularlocation_location", "keywords" in entry.annotations.keys()):
        headings = ["Entry ID", "Keywords"]
        tab.header(headings)
        tab.add_row([entry.id, entry.annotations["keywords"]])

s = tab.draw()
with open("Table.txt", 'w') as f:
    f.write(s)
    f.close()

#scoring and alignment function

#file = sys.argv[2] + ".fasta"
#file = "catabolism.fasta"
#print(sys.argv)
def seq_comp(file):
    seq_r = SeqIO.parse(file, "fasta")
    
    # print([i for i in seq_r])
    for record1, record2 in combinations(seq_r, 2):
        seq1 = record1.seq
        seq2 = record2.seq
        q = open(sys.argv[2] + ".txt", 'w')
        for alignments in pairwise2.align.globalxx(seq1, seq2):
            print("Done")
            q.write(format_alignment(*alignments[0:]))

#print(seq_comp(file))
f = open(path, 'r')
# print(type(f))
seq_comp(path)