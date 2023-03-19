#!/usr/bin/env python3

import requests

def get_human_proteome():
  """Get the human proteome from the UniProt API."""
  url = 'https://rest.uniprot.org/uniprotkb/stream?format=fasta&includeIsoform=true&query=%28proteome%3AUP000005640%29'
  r = requests.get(url)
  with open('data/human_proteome.fasta', 'w') as f:
      f.write(r.text)

if __name__ == '__main__':
  get_human_proteome()