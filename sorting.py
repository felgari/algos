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

"""Script with sorting algorithms.
"""

import random

THE_SEED = 1
NUM_ELTS = 100
MULT = ( 10 * NUM_ELTS )

def test_sort(the_list):
    
    sort_ok = True
    
    for i in range(len(the_list) - 1):
        if the_list[i] > the_list[i+1]:
            sort_ok = False
            break
        
    if sort_ok:
        print "The sorting is ok."
    else:
        print "The sorting is not ok."

def qsort(the_list):
    
    if len(the_list) <= 1:
        return the_list
    
    less = []
    pivot = [the_list[-1]]
    more = []
    
    for j in range(len(the_list) - 1):
        if the_list[j] < the_list[-1]:
            less.append(the_list[j])
        elif the_list[j] > the_list[-1]:
            more.append(the_list[j])
        else:
            pivot.append(the_list[j])
    
    return qsort(less) + pivot + qsort(more)    

def generate_random_list():
        
    random.seed(THE_SEED)
    
    the_list = [int(MULT * random.random()) for _ in xrange(NUM_ELTS)]
    
    return the_list

def main():
    
    the_list = generate_random_list()
    
    list_sorted = qsort(the_list)
    
    test_sort(list_sorted)

if __name__ == "__main__":
    
    main()