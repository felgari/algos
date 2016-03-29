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

"""Script woth algorithms with sequences as random numbers generation, finding
cycles in sequences and looking for substrings.
"""

SEED = 3771

#M_BBS = (71 * 73)
#M_BBS = (311 * 313) 
M_BBS = (523 * 541)

STR_1 = 'ABCDEFGFGFHIJK'
SUBSTR_1 = 'FGFH'

# Generation of random numbers.
def blum_blum_shum(n):
    """ Reference: https://en.wikipedia.org/wiki/Blum_Blum_Shub
    """
    
    return pow(n,2) % M_BBS

# Looking for cycles in a sequence of numbers.
def floyd(fun, x0):
    """ Reference: https://en.wikipedia.org/wiki/Floyd%27s_cycle-finding_algorithm
    """
        
    # Find a cycle.
    tortoise = fun(x0)
    hare = fun(fun(x0))
    while tortoise != hare:
        tortoise = fun(tortoise)
        hare = fun(fun(hare))

    # Find the beginning of the first complete cycle.    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = fun(tortoise)
        hare = fun(hare)
        mu += 1
 
    # Find the length of the shortest cycle.
    lam = 1
    hare = fun(tortoise)
    while tortoise != hare:
        hare = fun(hare)
        lam += 1
 
    return lam, mu

def brent(fun, x0):
    """ Reference: https://en.wikipedia.org/wiki/Cycle_detection#Brent.27s_algorithm
    """

    power = lam = 1
    tortoise = x0
    hare = fun(x0) 

    # Search cycles comparing values generated at successive powers of two 
    # with the values generated until a length of that power of two.
    # 'lam' is the length of the shortest cycle.
    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power *= 2
            lam = 0
        hare = fun(hare)
        lam += 1

    # Find a position of the first complete cycle. This position is shifted 
    # from the beginning of the cycle as many positions as the first position 
    # of the first cycle is shifted from x0. 
    hare = x0    
    for _ in range(lam):
        hare = fun(hare)
        
    # Find the first position of the first cycle.
    mu = 0
    tortoise = x0    
    while tortoise != hare:
        tortoise = fun(tortoise)
        hare = fun(hare)
        mu += 1
 
    return lam, mu

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

def main():
    
    print "Generating random numbers with Blum, Blum, Shum."
    print "Floyd -> Shortest cycle: %d, position of the first cycle: %d" % \
            floyd(blum_blum_shum, SEED)

    print "Brent -> Shortest cycle: %d, position of the first cycle: %d" % \
            brent(blum_blum_shum, SEED)   
            
    print "'%s' is found in '%s' with Knuth-Morris-Pratt at position: %d" % \
        (SUBSTR_1, STR_1, Knuth_Morris_Pratt(STR_1, SUBSTR_1))

if __name__ == "__main__":
    
    main()