import argparse
from posixpath import join
import subprocess
import threading
from pathlib import Path
def assemble_pe (forward,reverse,output):
    with open (f"{output}/assemble.out",'w') as out, open (f"{output}/assemble.err",'w') as err:
        Path(f"{output}/assembly").mkdir(parents=True, exist_ok=True)
        return subprocess.call (f'metaspades.py -1 {forward} -2 {reverse} -o {output}/assembly',shell = True, stderr=err, stdout=out)
def assemble_se (sequence,output):
    with open (f"{output}/assemble.out",'w') as out, open (f"{output}/assemble.err",'w') as err:
        Path(f"{output}/assembly").mkdir(parents=True, exist_ok=True)
        return subprocess.call (f'metaspades.py -s {sequence} -o {output}/assembly',shell = True, stderr=err, stdout=out)