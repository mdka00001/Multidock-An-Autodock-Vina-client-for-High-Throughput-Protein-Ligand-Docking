import os
import subprocess
from pathlib import Path

intro="\nMultidock: An Autodock Vina client for High Throughput Protein-Ligand Docking\n\n # Pre-requisits: 'pathlib' module needs to installed.\
It is advised to use virtual environment\
(e.g: conda) #\n\n Please follow the steps:\n 1. Copy all the ligand (pdbqt files) in a folder\n \
2. Copy 'config.txt' and receptor (pdbqt files) in another subfolder\n 3. Do not specify ligand molecule in config file\n 4. Run 'multidock.py'\
   from the sub-folder containing receptor and config files\n 5. Insert location of the ligands\n 6. Press Enter\n \n Coded and written by- Md Adnan Karim\n"

print(intro)
print("Insert location of the ligands:")
f=input()

path=Path(f)

vina='"C:\Program Files (x86)\The Scripps Research Institute\Vina\\vina.exe"'

for i in os.listdir(path):

  lig=i.split(".")
  s=" --receptor modeller.pdbqt "+"--ligand "+"ligand/"+i+" "+"--config config.txt "+"--log "+lig[0]+".txt "+"--out "+"output_"+i
  #print(vina+s)
  os.system(vina+s)

print("\nDocking has been completed")