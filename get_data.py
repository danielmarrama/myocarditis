#!/usr/bin/env python3

import requests
from Bio import SeqIO


def get_human_proteome():
  """Get the human proteome from the UniProt API."""
  url = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&includeIsoform=true&query=%28proteome%3AUP000005640%29'
  r = requests.get(url)
  with open('data/human_proteome.fasta', 'w') as f:
      f.write(r.text)


def remove_myocarditis_antigens():
  """Remove the myocarditis antigens from the human proteome."""
  human_proteome_ids = [protein.id.split('|')[1] for protein in SeqIO.parse('data/human_proteome.fasta', 'fasta')]
  myocarditis_ids = [protein.id.split('|')[1] for protein in SeqIO.parse('data/myocarditis_antigens.fasta', 'fasta')]

  non_myocarditis_antigens = []
  for protein in SeqIO.parse('data/human_proteome.fasta', 'fasta'):
    if protein.id.split('|')[1] not in myocarditis_ids:
      non_myocarditis_antigens.append(protein)
  
  SeqIO.write(non_myocarditis_antigens, 'data/non_myocarditis_antigens.fasta', 'fasta')

def main():
  get_human_proteome()
  remove_myocarditis_antigens()

if __name__ == '__main__':
  main()