# Protein-Analysis

This is a command line tool for protein analysis using UniProt XML, Clustalw2
(you will need to download both the Uniprot xml and Clustalw2), and
a few other libraries. The idea is to select proteins related by function, 
for example, if we wanted to study proteins that are associated with catabolism 
we enter the name of this python file in the command line along with path 
to the xml file and the word 'catabolism'. The programme is set to select 25 
proteins but you can open the Proto.py file and change the limit_results value. 
The programme will ask for the path to clustalw2, copy the path without
spaces and enter. The program will write a number of files, including 
an aln and a text files where you can view alignments. There are two alignment
 files to compare presentation and notation. The outputs also include a fasta 
 file of the selected proteins and a .txt file with a table that shows the 
 entry ID and associated cellular location for each protein
and at the end of that file it says which is the most common cellular location
(this is useful because it may highlight if a cellular process only occurs in a 
particular cellular location). A phylogenetic tree is also printed out to the 
command line for assesing the distance between the proteins.

Depending on the number of proteins to be analysed (limit_results) and the 
the word (relating to function like cata or syth) the program may take more
r less time to run.

Call command examples:

python Proto.py uniprot_sprot.xml catabolism
or
python Proto.py <'path_to_uniprot_sprot.xml'> synth

After calling, the program will run and search for proteins meeting the requirements
then it will prompt to you to direct it to the clustalw2 file. Do so without leaving
spacces. After that the code will write all the files mentioned above. 

The files can be used to analyse proteins that a related by function and maybe point
out a popular cellular location for a particular function.
