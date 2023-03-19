#!/usr/bin/env python3

from pepmatch import Preprocessor, Matcher

Preprocessor('myocarditis_antigens.fasta', 'pickle').preprocess(k=2)
Matcher('data/spike_9mers.fasta', 'myocarditis_antigens.fasta', 5, 2).match()
Matcher('data/shuffled_9mers.fasta', 'myocarditis_antigens.fasta', 5, 2).match()
Matcher('data/spike_15mers.fasta', 'myocarditis_antigens.fasta', 7, 2).match()
Matcher('data/shuffled_15mers.fasta', 'myocarditis_antigens.fasta', 7, 2).match()