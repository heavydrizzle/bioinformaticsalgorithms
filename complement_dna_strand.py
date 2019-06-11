# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:49:16 2019

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT

@author: Efren A. Serra

Reference:
    http://rosalind.info/problems/revc/
"""

def complement_dna_strand(strand):
    complement_map = \
    dict(map(lambda k,v: (k,v), ('A', 'C', 'G', 'T'), ('T', 'G', 'C', 'A')))

    cstrand = ''
    for nc in strand[::-1]:
        cstrand += complement_map[nc]

    return cstrand

def main():
    with open("rosalind_revc.txt") as f:
        data_set = f.read().strip()
    print (complement_dna_strand(data_set))

if __name__ == "__main__":
    main()