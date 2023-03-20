#!/usr/bin/env python3

import random


def shuffle_peptides(file):
  shuffle_peptides = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if line.startswith('>'):
        continue
      else:
        peptide = line.strip()
        shuffle_peptides.append(''.join(random.sample(peptide, len(peptide))))
  return shuffle_peptides


def write_peptides(file, peptides):
  count = 1
  with open(file, 'w') as f:
    for peptide in peptides:
      f.write(f'>{count}\n')
      f.write(f'{peptide}\n')
      count += 1


if __name__ == '__main__':
  write_peptides('data/shuffled_9mers.fasta', shuffle_peptides('data/spike_9mers.fasta'))
  write_peptides('data/shuffled_15mers.fasta', shuffle_peptides('data/spike_15mers.fasta'))
