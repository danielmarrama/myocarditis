#!/usr/bin/env python3

import os
import random
from Bio import SeqIO
from pepmatch import Preprocessor, Matcher


os.makedirs('random_sets', exist_ok=True)

def make_random_sets():
  """
  Make 1000 random sets of the human proteome sampling 35 proteins for each set.

  We use 35 because that is the number of myocarditis-associated antigens 
  we found.
  """
  human_proteome = list(SeqIO.parse('data/non_myocarditis_antigens.fasta', 'fasta'))
  
  for i in range(1000):
    with open(f'random_sets/random_protein_set_{i+1}.fasta', 'w') as f:
      proteins = random.sample(human_proteome, 35)
      SeqIO.write(proteins, f, 'fasta')

def search_random_sets():
  """The spike and shuffled peptides in the random sets."""
  for i in range(1000):
    Preprocessor(f'random_sets/random_protein_set_{i+1}.fasta', 'pickle').preprocess(k=2)
    Matcher('spike_9mers.fasta', f'random_protein_set_{i+1}', 5, 2).match()
    Matcher('shuffled_9mers.fasta', f'random_protein_set_{i+1}', 5, 2).match()
    Matcher('spike_15mers.fasta', f'random_protein_set_{i+1}', 7, 2).match()
    Matcher('shuffled_15mers.fasta', f'random_protein_set_{i+1}', 7, 2).match()

def main():
  make_random_sets()
  search_random_sets()

if __name__ == '__main__':
  main()