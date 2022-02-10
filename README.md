# Multidock: An Autodock Vina Client for High Throughput Protein Ligand Docking

# Pre-requisits: 
 Make sure Python 3.7 (or higher) version is installed in the system.
'pathlib' module needs to installed. It is advised to use virtual environment(e.g: conda) #
 
# Installing 'pathlib':
 
  Without conda environment: "pip install pathlib"
  
  With conda environment: "conda install pathlib"



 # Please follow the steps:
 1. Copy all the ligand (pdbqt files) in a folder
 2. Copy 'config.txt' and receptor (pdbqt files) in another subfolder
 3. Do not specify ligand molecule in config file
 4. Run 'multidock.py' from the sub-folder containing receptor and config files
 5. Insert location of the ligands
 6. Enter the name of 'Receptor' file
 7. Enter the number of iterations for each ligand 
 8. Press Enter 
 9. Folders with ligans name will contain outputs for each iteration

 #  Use the following command to run python script in cmd (in user directory)
 "python multidock.py"

 # Coded by- 
 Md Adnan Karim \
 MS Bioinformatics\
 Universität des Saarlandes\
 (mdka00001@stud.uni-saarland.de)
