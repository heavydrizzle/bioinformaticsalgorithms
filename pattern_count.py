# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:59:10 2019

@author: serra
"""

def PatternCount(Text, Pattern):
    count = 0
    for n in range(len(Text)-len(Pattern)+1):
        print(Text[n:n+len(Pattern)])
        if Text[n:n+len(Pattern)] == Pattern:
            count += 1

    print ("Patter count: %d"%count)
    print("Text length: %d"%len(Text))
    print("Pattern length: %d"%len(Pattern))

PatternCount("AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB", "AAB")