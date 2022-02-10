#!/bin/env python

import os
import subprocess
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
print("Insert location of the ligands:")
f=input()

#insert receptor file name
print("Insert receptor file name:")
receptor=input()

#insert number of iteration for each ligand
print("insert number of iteration for each ligand:")
st=input()

itr=int(st)

path=Path(f)

#location of vina.exe
vina='"C:\Program Files (x86)\The Scripps Research Institute\Vina\\vina.exe"'



for i in os.listdir(path):

  #for output file naming purpose
  lig=i.split(".")

  if not os.path.exists(lig[0]):
    os.mkdir(lig[0])

  #iterator for each ligand
  for j in range(0,itr):



    output_dir=lig[0]+"/"+lig[0]+"_"+str(j+1)
    
    if not os.path.exists(output_dir):
      os.mkdir(output_dir)

    #command to be executed
    s=" --receptor "+receptor+" --ligand "+"ligand/"+i+" "+"--config config.txt "+"--log "+output_dir+"/"+lig[0]+".txt "+"--out "+output_dir+"/"+"output_"+i
    #print(vina+s)
    os.system(vina+s)

print("\nDocking has been completed\n\n")

outro="Coded by-\n\
Md Adnan Karim\n\
MS Bioinformatics\n\
Universität des Saarlandes\n\
mdka00001@stud.uni-saarland.de\n"

print(outro)
