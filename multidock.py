#!/bin/env python

import os
import subprocess
import statistics as sp
from pathlib import Path

intro="\nMultidock: An Autodock Vina client for High Throughput Protein-Ligand Docking\n\n\
# Pre-requisits: 'pathlib' module needs to installed.\
It is advised to use virtual environment(e.g: conda) #\n\n\
Please follow the steps:\n\
1. Copy all the ligand (pdbqt files) in a folder\n\
2. Copy 'config.txt' and receptor (pdbqt files) in another subfolder\n\
3. Do not specify ligand molecule in config file\n\
4. Run 'multidock.py' from the sub-folder containing receptor and config files\n\
5. Insert location of the ligands\n\
6. Enter the name of 'Receptor' file\n\
7. Enter the number of iterations for each ligand\n\
8. Press Enter\n\
9. Folders with ligans name will contain outputs for each iteration\n\n\n"

print(intro)

f=input("Insert location of the ligands: ")

#insert receptor file name

receptor=input("Insert receptor file name: ")

#insert number of iteration for each ligand

st=input("insert number of iteration for each ligand: ")

itr=int(st)

path=Path(f)

#location of vina.exe
vina='"C:\Program Files (x86)\The Scripps Research Institute\Vina\\vina.exe"'

#Calculating average and standard deviation for each ligand after n iterations
lig_list=[]
mn=[]
std=[]

for i in os.listdir(path):

  #for output file naming purpose
  lig=i.split(".")
  scores=[]
  lig_list.append(lig[0])

  if not os.path.exists(lig[0]):
    os.mkdir(lig[0])

  #iterator for each ligand
  for j in range(0,itr):



    output_dir=lig[0]+"/"+lig[0]+"_"+str(j+1)
    
    if not os.path.exists(output_dir):
      os.mkdir(output_dir)

    #command to be executed
    s=" --receptor "+receptor+" --ligand "+"ligand/"+i+" "+"--config config.txt "+"--log "+output_dir+"/"+lig[0]+".txt "+"--out "+output_dir+"/"+"output_"+i
    
    os.system(vina+s)

    #reading output.txt file
    tx_file=open(output_dir+"/"+lig[0]+".txt")

    #Selecting best dock score
    content = tx_file.readlines()[26].split()


    scores.append(float(content[1]))
    
  #calculating average and stdev
  mn.append(sum(scores)/len(scores))
  std.append(sp.stdev(scores))




print("\nDocking has been completed\n\nDocking socre summary after %d iteration:\n" % itr)

final_results=[]
for k in range(0,len(lig_list)):
  s=("%s Average: %f±%f"%(lig_list[k],mn[k],std[k]))
  final_results.append(s)
  print("%s\n"%s)



outro="\n\nCoded by- \n\
Md Adnan Karim\n\
MS Bioinformatics\n\
Universität des Saarlandes\n\
mdka00001@stud.uni-saarland.de\n"

print(outro)

#Final output as text file
with open('Score_average.txt', 'w') as f:
    for line in final_results:
        f.write(line)
        f.write('\n')
