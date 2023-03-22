#!/usr/bin/env python3

from pepmatch import Preprocessor, Matcher

import os

# search the spike and shuffled peptides in the myocarditis-associated antigens
Preprocessor('data/myocarditis_antigens.fasta', 'pickle').preprocess(k=2)
Matcher('data/spike_9mers.fasta', 'data/myocarditis_antigens.fasta', 5, 2).match()
Matcher('data/shuffled_9mers.fasta', 'data/myocarditis_antigens.fasta', 5, 2).match()
Matcher('data/spike_15mers.fasta', 'data/myocarditis_antigens.fasta', 7, 2).match()
Matcher('data/shuffled_15mers.fasta', 'data/myocarditis_antigens.fasta', 7, 2).match()

os.remove('myocarditis_antigens_2mers.pickle')
os.remove('myocarditis_antigens_names.pickle')