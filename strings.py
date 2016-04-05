#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Algorithms related to strings.
"""

import sys

STR_1 = 'ABCDEFGFGFHIJK'
SUBSTR_1 = 'FGFH'

NUM_ARGS = 3
ARGS_LCST = 4 

def do_reverse(s):
    
    rev_list = [ s[i] for i in range(len(s) - 1, -1, -1) ]
        
    return ''.join(rev_list)

def uses_only(s1, s2):
    
    only = [ ch in s2 for ch in s1 ]
    
    return all(only) 

def most_frequent(s1):
    
    freq = dict()
    
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    return sorted(freq, key=freq.get, reverse=True)

def is_abecedarian(s1):
    
    return all([ s1[i] <= s1[i+1] for i in range(0, len(s1) - 1)])

def is_palindrome(s1):
    """Without using reverse."""
    
    le = len(s1)
    
    return all([ s1[i] == s1[le-i-1] for i in range(le / 2) ])

def is_anagram(s1, s2):
    
    is_anag = False
    
    if len(s1) == len(s2):
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        
        is_anag = ( s1_sorted == s2_sorted )
    
    return is_anag

# Looking for repeated substrings in a string.
def Knuth_Morris_Pratt(s, subs):
    """Reference:https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    
    Without partial match table.
    """ 
    
    s_idx = subs_idx = 0
    
    while s_idx + subs_idx < len(s) - 1:
        if subs[subs_idx] == s[s_idx + subs_idx]:
            if subs_idx == len(subs) - 1:
                return s_idx 
            subs_idx += 1
        else:
            subs_idx = 0
            s_idx += 1
    
    return -1

def longest_common_substring(s1, s2):
    """Reference:https://en.wikipedia.org/wiki/Longest_common_substring_problem
    """
    
    len_s1 = len(s1)
    len_s2 = len(s2)    
    m = [ [0  for _ in range(len_s2) ] for _ in range(len_s1) ]
    greatest_len = 0
    common_str = ''
    
    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                
                if i == 1 or j == 1:
                    m[i][j] = 1
                else:
                    m[i][j] = m[i-1][j-1] + 1
                    
                if m[i][j] > greatest_len:
                    greatest_len = m[i][j]
                    common_str = s1[i-greatest_len+1:i+1] 
                elif m[i][j] == greatest_len:
                    common_str = common_str + s1[i-greatest_len+1:i+1]
                    
    return common_str
    
if __name__ == "__main__":
    
    if len(sys.argv) < NUM_ARGS:
        print"ERROR: Arguments needed. Use: %s num1 num2 ..." % sys.argv[0]
    else:
        s1 = sys.argv[1]
        s2 = sys.argv[2]
        
        print "Reverse of %s is %s" % (s1, do_reverse(s1))
        
        print "%s uses only chars in %s is: %s" % (s1, s2, uses_only(s1, s2))
        
        print "%s most frequent characters are: %s" % (s1, most_frequent(s1))
        
        print "%s is abcedarian: %s" % (s1, is_abecedarian(s1))
        
        print "%s is palindrome: %s" % (s1, is_palindrome(s1))
        
        print "%s and %s are anagrams: %s" % (s1, s2, is_anagram(s1, s2))
                
        print "A substring of %s in %s (with Knuth-Morris-Pratt) is at: %d" % \
            (s1, s2, Knuth_Morris_Pratt(s1, s2))
        
        print "Longest common substring of %s and %s is: %s" % \
            (s1, s2, longest_common_substring(s1, s2))