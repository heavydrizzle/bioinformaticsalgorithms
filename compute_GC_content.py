# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:10:18 2019

@author: Efren A. Serra
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
        k = v = str()
        pattern = re.compile(r'^>\w+')

        for line in ctx:
            print(line)
            m = pattern.match(line)
            if m:
                # new FASTA ID
                k = m.group(0)
                fasta_dataset[k] = str()

            else:
                fasta_dataset[k] += line

    return fasta_dataset

print (read_fasta_dataset("rosalind_gc.txt"))