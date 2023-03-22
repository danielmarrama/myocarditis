#!/usr/bin/env python3

import os
import random
from Bio import SeqIO
from pepmatch import Preprocessor, Matcher


os.makedirs('data/random_sets', exist_ok=True)

def make_random_sets():
  """
  Make 1000 random sets of the human proteome sampling 35 proteins for each set.

  We use 35 because that is the number of myocarditis-associated antigens 
  we found.
  """
  human_proteome = list(SeqIO.parse('data/non_myocarditis_antigens.fasta', 'fasta'))
  
  for i in range(1000):
    os.makedirs(f'data/random_sets/{i+1}', exist_ok=True)
    with open(f'data/random_sets/{i+1}/random_protein_set_{i+1}.fasta', 'w') as f:
      proteins = random.sample(human_proteome, 35)
      SeqIO.write(proteins, f, 'fasta')

def search_random_sets():
  """The spike and shuffled peptides in the random sets."""
  for i in range(1000):
    random_set_path = f'data/random_sets/{i+1}'

    # preprocess each random set
    Preprocessor(f'{random_set_path}/random_protein_set_{i+1}.fasta', 'pickle', preprocessed_files_path=random_set_path).preprocess(k=2)

    # search each random set for all peptides (spike/shuffled 9/15mers)
    Matcher('data/spike_9mers.fasta', f'{random_set_path}/random_protein_set_{i+1}', 5, 2, preprocessed_files_path=random_set_path).match()
    Matcher('data/shuffled_9mers.fasta', f'{random_set_path}/random_protein_set_{i+1}', 5, 2, preprocessed_files_path=random_set_path).match()
    Matcher('data/spike_15mers.fasta', f'{random_set_path}/random_protein_set_{i+1}', 7, 2, preprocessed_files_path=random_set_path).match()
    Matcher('data/shuffled_15mers.fasta', f'{random_set_path}/random_protein_set_{i+1}', 7, 2, preprocessed_files_path=random_set_path).match()

def main():
  make_random_sets()
  search_random_sets()

if __name__ == '__main__':
  main()