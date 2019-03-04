# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from Bio import SeqIO
from Bio import SeqFeature

limit_results = 5
tei = []
count = 0

f = open("H:\\Downloads\\uniprot_sprot.xml")
f = SeqIO.parse(f, "uniprot-xml")

#find proteins invloved in catabolic activity from Uniprot XML
for entry in f:
    #print(entry.annotations['keywords'])
    if ("comment_function" in entry.annotations.keys()):
        value = entry.annotations["comment_function"]
        
        new_found = ["catabolism" in i for i in value]
        a_va = any(new_found)
                
        if a_va:
            tei.append(entry)
            count += 1
            if (count == limit_results):
                break

with open("catalyticactivity.fasta", 'w') as f:
    SeqIO.write(tei, f, "fasta")