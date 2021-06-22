import argparse
from posixpath import join
import subprocess
import threading
from pathlib import Path
import sys
import os
from Bio import Entrez
from collections import Counter
import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scripts import assembly, taxa_ann, taxonomy_frequency, ploting

parser = argparse.ArgumentParser(description='Give row data')
parser.add_argument('-f', '--forward', help='forward sequence')
parser.add_argument('-r', '--reverse', help=' reverse sequnece')
parser.add_argument('-s','--single', help='Single file')
parser.add_argument('-o', '--output', help='Output folder')
arguments = parser.parse_args()
arguments = arguments.__dict__
forward = arguments['forward']
reverse = arguments['reverse']
single = arguments['single']
output = arguments['output'].rstrip('/')
if output == None:
    raise KeyError ("Output folder should be mentiond")
elif os.path.isdir(output) == False:
    raise TypeError("The output folder is not supported")
else:
    if forward == None and reverse == None and single !=None:
        try:
            assembly = threading.Thread(target=assembly.assemble_se, args=(single, output))
            assembly.start()
            assembly.join()
            annotation = threading.Thread (target = taxa_ann.prodigal, args = (f"{output}/assembly", output))
            annotation.start()
            annotation.join()
            Path(f"{output}/taxa_stat").mkdir(parents=True, exist_ok=True)
            taxa = threading.Thread (target = taxonomy_frequency.tax_to_freq, args = (f"{output}/prodigal/contigs.gff", f"{output}/taxa_stat/taxa_freq.csv"))
            taxa.start()
            taxa.join()
            data = pd.read_csv(f"{output}/taxa_stat/taxa_freq.csv",sep='\t')
            plots = threading.Thread (target = ploting.ploting, args = (data,f"{output}/taxa_stat"))
            plots.start()
            plots.join()
        except:
            raise ChildProcessError("Error in a step")
    elif single ==None and forward !=None and reverse !=None:
        try:
            assembly = threading.Thread(target=assembly.assemble_se, args=(single, output))
            assembly.start()
            assembly.join()
            annotation = threading.Thread (target = taxa_ann.prodigal, args = (f"{output}/assembly", output))
            annotation.start()
            annotation.join()
            Path(f"{output}/taxa_stat").mkdir(parents=True, exist_ok=True)
            taxa = threading.Thread (target = taxonomy_frequency.tax_to_freq, args = (f"{output}/prodigal/contigs.gff", f"{output}/taxa_stat/taxa_freq.csv"))
            taxa.start()
            taxa.join()
            data = pd.read_csv(f"{output}/taxa_stat/taxa_freq.csv",sep='\t')
            plots = threading.Thread (target = ploting.ploting, args = (data,f"{output}/taxa_stat"))
            plots.start()
            plots.join()
        except:
            raise ChildProcessError("Error in a step")
    else:
        raise KeyError("You used unconfortable arguments")
