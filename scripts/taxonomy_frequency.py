import sys
from Bio import Entrez
from collections import Counter
import pandas as pd
###########################################
def get_tax_id(species):
    species = species.replace(" ", "+").strip()
    search = Entrez.esearch(term = species, db = "taxonomy", retmode = "xml")
    record = Entrez.read(search)
    return record['IdList'][0]
###############################################
def get_tax_data(taxid):
    search = Entrez.efetch(id = taxid, db = "taxonomy", retmode = "xml")
    return Entrez.read(search)
###############################################
def tax_to_freq(in_file,out_file):
  Entrez.email = 'idrissi.azami.abdellah@gmail.com'
  print('Reading input file .....')
  with open (in_file,'r', encoding='utf-8') as inpt:
    sps = []
    content = inpt.readlines()
    print('Extracting nodes ...')
    for i in content:
      if '# Model Data:' in i:
        sp = i.split ('|')[1].split('|')[0].replace('_',' ')
        sps.append(sp)
  print('Counting nodes....')
  counter = dict(Counter(sps))
  total = 0
  for i in counter:
    try:
      taxid = get_tax_id(i)
      taxdata = get_tax_data(taxid)
      total = total + counter[i]
    except:
      pass
  print ('Retriving taxonomy ...')
  tax = []
  for i in counter:
    try:
      taxid = get_tax_id(i)
      taxdata = get_tax_data(taxid)
      lineage = {d['Rank']:d['ScientificName'] for d in
        taxdata[0]['LineageEx'] if d['Rank'] in ['superkingdom','phylum','class','order', 'family','genus','species']}
      lineage['Strain']=i
      lineage['#Hits']=counter[i]
      lineage['Frequency (%)']=(counter[i]/total)*100
      tax.append(lineage)
    except:
      pass
  df = pd.DataFrame(tax)
  df.to_csv(out_file,sep='\t',index=False)
  return df

