import argparse
from posixpath import join
import subprocess
import threading
from pathlib import Path


def prodigal (folder, output):
    with open (f"{output}/taxa_ann.out",'w') as out, open (f"{output}/tax_ann.err",'w') as err:
        Path(f"{output}/prodigal").mkdir(parents=True, exist_ok=True)
        return subprocess.call(f"prodigal -a {output}/assembly/contigs.aa.fasta -d {output}/prodigal/contigs.nuc.fasta -i {folder}/prodigal/contigs.fasta -f gff -p meta > {output}/prodigal/contigs.gff",stderr=err,stdout=out)
# print('Total found sp:',len(tax))
# print('Total nodes',total)
# print('Writing output file >',out_file)
# df.to_csv(out_file,sep='\t',index=False)