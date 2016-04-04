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

"""Script with algorithms related to strings.
"""

import sys

STR_1 = 'ABCDEFGFGFHIJK'
SUBSTR_1 = 'FGFH'

NUM_ARGS = 3
ARGS_LCST = 4 

# Looking for repeated substrings in a string.
def Knuth_Morris_Pratt(s, subs):
    """Reference: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
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
                    common_str = s1[i-greatest_len+1:i] 
                elif m[i][j] == greatest_len:
                    common_str = common_str + s1[i-greatest_len+1:i]
                    
    return common_str
    
if __name__ == "__main__":
    
    if len(sys.argv) < NUM_ARGS:
        print"ERROR: Arguments needed. Use: %s num1 num2 ..." % sys.argv[0]
    else:
        print "A substring of %s in %s (with Knuth-Morris-Pratt) is at: %d" % \
            (sys.argv[1], sys.argv[2], 
             Knuth_Morris_Pratt(sys.argv[1], sys.argv[2]))
        
        print "Longest common substring of %s and %s is: %s" % \
            (sys.argv[1], sys.argv[2], 
             longest_common_substring(sys.argv[1], sys.argv[2]))