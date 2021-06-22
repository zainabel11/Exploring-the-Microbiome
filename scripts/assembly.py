import argparse
from posixpath import join
import subprocess
import threading
from pathlib import Path
def assemble_pe (file_path,forward,reverse,output):

    Path(f"{output}/assembly").mkdir(parents=True, exist_ok=True)
    return subprocess.call (f'python {file_path}/src/metaspades/metaspades.py -1 {forward} -2 {reverse} -o {output}/assembly',shell = True)
      
