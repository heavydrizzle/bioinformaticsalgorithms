# -*- coding: utf-8 -*-
"""
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string
that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that
the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly
used method of string labeling is called FASTA format. In this format, the string
is introduced by a line that begins with '>', followed by some labeling information.
Subsequent lines contain the string itself; the first line to begin with '>' indicates
the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID
"Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content
of that string. Rosalind allows for a default error of 0.001 in all decimal answers
unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540

Created on Mon Jun 24 14:10:18 2019
@author: Efren A. Serra

Reference:
    http://rosalind.info/problems/gc/
"""

import re
import os
from numpy.compat import (
    isfileobj
)

def read_fasta_dataset(fd):
    if isfileobj(fd):
        # file already opened
        ctx = fd
    else:
        # open file
        ctx = open(os.fspath(fd), 'r')

    with ctx as fd:
        fasta_dataset = dict()
        k = str()
        pattern = re.compile(r'^>\w+')

        for line in ctx:
            m = pattern.match(line)
            if m:
                # new FASTA ID
                k = m.group(0)
                fasta_dataset[k] = str()
            else:
                fasta_dataset[k] += line.strip()

    return fasta_dataset

def count_GC_content(dataset):
    dataset_count = dict.fromkeys(dataset, 0)

    for k,dna_string in dataset.items():
        for nc in dna_string:
            if nc == 'G' or nc == 'C':
                dataset_count[k] += 1
        dataset_count[k] *= (100/len(dna_string))

    print(dataset_count)

if __name__ == "__main__":
    count_GC_content(read_fasta_dataset("rosalind_gc.txt"))
