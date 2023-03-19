#!/usr/bin/env python3

from pepmatch import Preprocessor, Matcher

Preprocessor('cardiac_proteins.fasta', 'pickle').preprocess(k=2)
Matcher('data/spike_9mers.fasta', 'cardiac_proteins.fasta', 5, 2).match()
Matcher('data/shuffled_9mers.fasta', 'cardiac_proteins.fasta', 5, 2).match()
Matcher('data/spike_15mers.fasta', 'cardiac_proteins.fasta', 7, 2).match()
Matcher('data/shuffled_15mers.fasta', 'cardiac_proteins.fasta', 7, 2).match()