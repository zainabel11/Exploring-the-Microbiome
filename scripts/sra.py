import subprocess
def retrive(id, output):
    with open (f"{output}/retrive.out", 'w') as out, open(f'{output}/retrive.err','w') as err:
        return subprocess.call(f'SRAdownload -f {output} {id}', shell=True, stdout=out,stderr=err)
retrive("SRR2223576", '/home/abdellah')