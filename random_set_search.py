#!/usr/bin/env python3

from pepmatch import Preprocessor, Matcher

for i in range(1000):
  Preprocessor(f'random_sets/random_protein_set_{i+1}.fasta', 'pickle').preprocess(k=2)
  Matcher('spike_9mers.fasta', f'random_protein_set_{i+1}', 5, 2).match()
  Matcher('shuffled_9mers.fasta', f'random_protein_set_{i+1}', 5, 2).match()
  Matcher('spike_15mers.fasta', f'random_protein_set_{i+1}', 7, 2).match()
  Matcher('shuffled_15mers.fasta', f'random_protein_set_{i+1}', 7, 2).match()
