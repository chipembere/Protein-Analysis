'''This is a command line tool for protein analysis using uniprot_sprot.xml.gz, 
clustalw2 (which you will need to download including biopython and 
texttable modules). The idea is to select proteins related by function 
for example, if we wanted to study proteins that are associated with catabolism 
we enter the name of this python file in the command line along with path to 
the uniprot_xml.gz file and the word 'catabolism'. The programme is set to 
select 25 proteins but you can open the Proto.py file and change the limit_results 
value. The programme will ask for the path to clustalw2, copy the path without 
spaces and enter. The program will write a number of files, including an aln 
and a text files where you can view alignments. There are two alignment files 
to compare presentation and notation. The outputs also include a fasta file of the 
selected proteins and a .txt file with a table that shows the entry ID and 
associated cellular location for each protein and at the end of that file it 
tells you the most common cellular location (this is useful because it may highlight 
if a cellular process only occurs in a particular cellular location). A phylogenetic 
tree is also printed out to the command line for assesing the distance between the 
proteins.'''

import sys
from Bio import SeqIO
from Bio import SeqFeature
from itertools import combinations
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import AlignIO
import texttable as tt
from collections import Counter
import os
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO
from Bio import Phylo
import gzip
from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner

'''limit the number of proteins gathered'''
limit_results = 25
tei = []
count = 0
tab = tt.Texttable()
most_commn = []

try:
    '''path to Uniprot XML file'''
    uniprot_xml = sys.argv[1]
    with gzip.open(uniprot_xml) as f:
        f = SeqIO.parse(f, "uniprot-xml")

except:
    '''if path is not provided'''
    print("Argument not recognized or missing")
    print('Enter uniprot_sprot.xml.gz or the path to uniprot_sprot.xml.gz' )
    print("For example: 'python Proto.py uniprot_sprot.xml.gz catabolic'\n or\n python Proto.py <path_to_uniprot_sprot.xml.gz catabolism ")
    sys.exit()
with gzip.open(uniprot_xml) as f:
    f = SeqIO.parse(f, "uniprot-xml")
    try:
        '''find proteins involved in some similar activity/function from Uniprot XML'''
        for entry in f:
            #print(entry.annotations['keywords'])
            if ("comment_subcellularlocation_location" in entry.annotations.keys()):
                if ("comment_function" in entry.annotations.keys()):
                    value = entry.annotations["comment_function"]
                    new_found = [sys.argv[2] in i for i in value]
                    a_va = any(new_found)
                            
                    if a_va:
                        tei.append(entry)
                        count += 1
                        if (count == limit_results):
                            break
    except:
        print('You need to enter a word relating to protein function like """catabolism""" as your 3rd argument.')
        sys.exit()
        
path = sys.argv[2] + ".fasta"
f = open(path, 'w')
SeqIO.write(tei, f, "fasta")
f.close

def seq_comp(file):
    '''scoring and alignment function'''
    seq_r = SeqIO.parse(file, "fasta")
    for record1, record2 in combinations(seq_r, 2):
        seq1 = record1.seq
        seq2 = record2.seq
        q = open(sys.argv[2] + "2ndaln.txt", 'w')
        for alignments in pairwise2.align.globalxx(seq1, seq2):          
            q.write(format_alignment(*alignments[0:]))

f = open(path, 'r')
seq_comp(path)

with open(path, 'r') as f2:
    data = f2.read()
    #print(data)

try:
    '''Use Clustaw2 for multiple sequence alignment'''  
    clustalw_exe = input("Copy clustalw2 file path here, no spaces: ") # Clustalw2 path
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile = path)

    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"  
    stdout = clustalw_cline()
    stderr = clustalw_cline()

    '''Read alignment file'''
    align = AlignIO.read(sys.argv[2] + ".aln", "clustal")

    '''Use dnd file to make a phylogenetic tree'''
    tree = Phylo.read(sys.argv[2] + ".dnd", "newick")
    Phylo.draw_ascii(tree)

except:
    print('Downlaod Clustalw2 and copy the file path (without spaces) when prompted')
    sys.exit()

def Most_Common(lst):
    '''This functions is used to count the most common keyword or location, 
    which can be used to find out if a particular function only occurs in a 
    certain location'''
    data = Counter(lst)
    return data.most_common(1)[0][0]

# Put the locations of the proteins in a table
for entry in tei:
    '''This is to make a table of protein and cellular location'''

    if ("comment_subcellularlocation_location" in entry.annotations.keys()):
        value = entry.annotations["comment_subcellularlocation_location"]
        headings = ["Entry ID", "Subcellularlocation"]
        tab.header(headings)
        tab.add_row([entry.id, entry.annotations["comment_subcellularlocation_location"]])

        for l in value:            
            most_commn.append(l)
        
# Computing the most frequent cellular location
mst_cmn_w = Most_Common(most_commn)

qs = "\nThe most frequent cellular location for selected function is: \n" + mst_cmn_w
s = tab.draw()

'''Writing the table with keywords/locations
and the most frequent keyword or cellular location'''
with open("Table_n_MstCmnKywdOrLctn.txt", 'w') as f:
    f.write(s)
    f.write(qs)
    f.close()
