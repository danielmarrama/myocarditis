#!/bin/bash

echo "Getting data..."
python3 get_data.py
echo "Shuffling peptides..."
python3 shuffled_peptides.py
echo "Searching in myocarditis antigens..."
python3 myocarditis_antigen_search.py
echo "Creating and searching in random protein sets..."
python3 random_sets.py