### This is a command line tool for protein analysis using UniProt XML, Clustalw2
# (you will need to download both the Uniprot xml and Clustalw2), and 
### a few other libraries. The idea is to isolate proteins by a function, for example
# if we wanted to study proteins that are assosiated with catabolism we enter the 
# the name of this python file in the command line along with path to the xml file and
# the word 'catabolism'. As the programme runs it will ask you for the number of proteins
# you want to look at and the path to clustalw2. The program will write a number of files,
# it will write a fasta file that only includes the selected proteins, txt files with alignments 
# , a table that shows the keywords or cellular location associated with each selected protein
# and at the end of that file it says which is the most common keyword or cellular location
# (this is useful because it may highlight if a cellular process only occours in a particular
# cellular location). A phylogenetic tree is also printed out to the command line.
#  distance  the path ofOn the command line you pass the python file with the 
### path to the Uniprot XML file and a keyword

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

#limit the number of proteins gathered
limit_results = 5 #input("How many proteins would you like to add? ") #could be argument 3
tei = []
count = 0
tab = tt.Texttable()
most_commn = []

##path to Uniprot XML file##
try:
    uniprot_xml = sys.argv[1]
    f = open(uniprot_xml)
    f = SeqIO.parse(f, "uniprot-xml")
except:
    #print("Argument not recognized")
    print('You entered: ' + sys.argv[1] + '\nYou should enter uniprot_sprot.xml or the path to uniprot_sprot.xml' )
    sys.exit()
#uniprot_xml = sys.argv[1]
#f = open(uniprot_xml)
#f = SeqIO.parse(f, "uniprot-xml")

#find proteins involved in some similar activity/function from Uniprot XML
try:
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
except:
    print('You need to enter a word relating to protein function like """catabolism""".')
    sys.exit

path = sys.argv[2] + ".fasta"
f = open(path, 'w')
SeqIO.write(tei, f, "fasta")
f.close

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
            #print("Done")
            q.write(format_alignment(*alignments[0:]))

#print(seq_comp(file))
f = open(path, 'r')
#print(type(f))
seq_comp(path)

with open(path, 'r') as f2:
    data = f2.read()
    #print(data)


#Use Clustaw2 for multiple sequence alignment
try:
      
    clustalw_exe = "/Users/brianmusonza/Downloads/clustalw-2.1-macosx/clustalw2" # Clustalw2 path
    #fs_file = open(sys.argv[2] + ".txt", "r")
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile = path)

    #cline = ClustalwCommandline("clustalw2", infile="enzymes.fasta")
    assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
    #clustalw_cline()
  
    stdout = clustalw_cline()
    stderr = clustalw_cline()

    # Read alignment file
    align = AlignIO.read(sys.argv[2] + ".aln", "clustal")
    #print(align)

    #Use dnd file to make a phylogenetic tree
    tree = Phylo.read(sys.argv[2] + ".dnd", "newick")
    Phylo.draw_ascii(tree)

except:
    print('Downlaod Clustalw2 and save it the directory with this file')
    sys.exit()
# This functions is used to count the most common keyword or location, 
# which can be used to find out if a particular function only occurs in a certain location
def Most_Common(lst): 
    data = Counter(lst)
    return data.most_common(1)[0][0]

# Put the locations/keywords of the proteins in a table
for entry in tei:
    if ("comment_subcellularlocation_location", "keywords" in entry.annotations.keys()):
        headings = ["Entry ID", "Keywords"]
        tab.header(headings)
        tab.add_row([entry.id, entry.annotations["keywords"]])

        # Computing the most frequent keyword/cellular location
        most_commn.append([entry.annotations["keywords"]])
        chero = [i for l in most_commn for i in l]  
        cg = [i for l in chero for i in l]
        mst_cmn_w = Most_Common(cg)

qs = "\nThe most frequent keywords phrase or cellular location is: \n" + mst_cmn_w
#print("\nThe most frequent keywords/location are; \n" + mst_cmn_w)        
s = tab.draw()

# Writing the table with keywords/locations
# and the most frequent keyword or cellular location
with open("Table_n_MstCmnKywdOrLctn.txt", 'w') as f:
    f.write(s)
    f.write(qs)
    f.close()



