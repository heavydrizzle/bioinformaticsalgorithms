# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:23:05 2019

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is
formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU

@author: Efren A. Serra

Reference:
    http://rosalind.info/problems/rna/
"""

def transcribe_dna_to_rna(s):
    transcription_map = \
    dict(map(lambda k,v: (k,v), ('A', 'C', 'G', 'T'), ('A', 'C', 'G', 'U')))

    rna = ''
    for nc in s[:]:
        rna += transcription_map[nc]

    return rna

def main():
    with open("rosalind_rna.txt") as f:
        data_set = f.read().strip()
    print (transcribe_dna_to_rna(data_set))

if __name__ == "__main__":
    main()