# Protein-Analysis

This is a command line tool for protein analysis using uniprot_sprot.xml.gz, 
clustalw2 (which you will need to download including biopython and texttable modules).
The idea is to select proteins related by function for example, if we wanted 
to study proteins that are associated with catabolism we enter the name of this 
python file in the command line along with path to the uniprot_xml.gz file and the word 
'catabolism'. The programme is set to select 25 proteins but you can open the 
Proto.py file and change the limit_results value. The programme will ask for 
the path to clustalw2, copy the path without spaces and enter. 
The program will write a number of files, including an aln and a text files where 
you can view alignments. There are two alignment files to compare presentation and 
notation. The outputs also include a fasta file of the selected proteins and a 
.txt file with a table that shows the entry ID and associated cellular location 
for each protein and at the end of that file it tells you the most common cellular 
location (this is useful because it may highlight if a cellular process only occurs in a 
particular cellular location). A phylogenetic tree is also printed out to the 
command line for assesing the distance between the proteins.

Depending on the number of proteins to be analysed (limit_results) and the 
the word (relating to function like cata or syth) the program may take more
or less time to run.

Call command examples:

python Proto.py uniprot_sprot.xml.gz catabolism

or

python Proto.py <'path_to_uniprot_sprot.xml.gz'> synth

After calling, the program will run and search for proteins meeting the requirements
then it will prompt you to direct it to the clustalw2 file. Do so without leaving
spaces or just drag the clustalw execution file to the terminal (if you're using 
windows, remove the quotation marks from the path then enter). After that the 
code will write all the files mentioned above. 

Windows clustalw2 path input should look like:

C:\Program Files (x86)\ClustalW2\clustalw2.exe

Not:

"C:\Program Files (x86)\ClustalW2\clustalw2.exe"

Download and decompress Uniprot XML from:

ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz


Download Clustalw2 from:

http://www.clustal.org/clustal2/

Dependenies:

Biopython

texttable




The output of this tool can be used to analyse proteins that a related by function and maybe point
out a popular cellular location for a particular function.
 
