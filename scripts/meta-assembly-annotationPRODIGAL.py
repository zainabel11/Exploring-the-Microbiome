import argparse
from posixpath import join
import subprocess
import threading
from pathlib import Path


def assemble (forward,reverse,output):
    return subprocess.call (f'metaspades.py -1 {forward} -2 {reverse} -o {output}',shell = True)
def prodigal (folder, output):
    Path(output).mkdir(parents=True, exist_ok=True)
    return subprocess.call(f"prodigal -a {output}/contigs.aa.fasta -d {output}/contigs.nuc.fasta -i {folder}/contigs.fasta -f gff -p meta > {output}/contigs.gff")



parser = argparse.ArgumentParser(description='Give row data')
parser.add_argument('-f', '--input1', help='forward sequence')
parser.add_argument('-r', '--input2', help=' reverse sequnece')
parser.add_argument('-o', '--output', help='Output folder')
arguments = parser.parse_args()
arguments = arguments.__dict__
print(arguments)
forward = arguments['input1']
reverse = arguments['input2']
output = arguments['output'].rstrip('/')
try:
    assembly = threading.Thread(target=assemble, args=(forward, reverse, output))
    assembly.start()
    assembly.join()
    Path(f"{output}/prodigal").mkdir(parents=True, exist_ok=True)
    annotation = threading.Thread (target = prodigal, args = (output, f"{output}/prodigal"))
    annotation.start()
    annotation.join()

except:
    print('Error')
