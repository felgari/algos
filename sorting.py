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

"""Script with several sorting algorithms.
"""

import random
import time

THE_SEED = 1
NUM_ELTS = 5000
MULT = ( 10 * NUM_ELTS )

def test_sort(the_list):
    
    sort_ok = True
    
    for i in range(len(the_list) - 1):
        if the_list[i] > the_list[i+1]:
            sort_ok = False
            break
        
    if sort_ok:
        print "... the sorting is ok."
    else:
        print "... the sorting is NOT ok."
        
def selection_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Selection_sort
    """
    
    nops = 0    
    
    # Walk the list to set in each iteration the minimum item of the
    # rest of the list in position j.
    for j in range(len(the_list)):
        
        mini_idx = j
        
        # Walk from j to the end of the list looking for the index of the
        # minimum item.
        for i in range(j + 1, len(the_list)): 
            
            # Find the index of the minor element.
            if the_list[i] < the_list[mini_idx]:
                mini_idx = i
                
            nops += 1
                
        # Swap the minimum item found with that in j.
        if min != j:
            the_list[mini_idx], the_list[j] = the_list[j], the_list[mini_idx]
    
    return the_list, nops   

def insertion_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Insertion_sort
    """
    
    nops = 0    
    
    # Walk the list from the second item to the end.
    for i in range(1, len(the_list)):
        
        j = i
        
        # Walk a sublist from i to 0 while adjacent items are out of order,
        # and in that case swap them.
        while j and the_list[j - 1] > the_list[j]:
            the_list[j - 1], the_list[j] = the_list[j], the_list[j - 1]
            j -= 1
            
            nops += 1
    
    return the_list, nops

def bubble_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Bubble_sort
    """
    
    nops = 0    
    
    max_pos = len(the_list) - 1
    
    for i in range(max_pos):
        for j in range(0, max_pos - i):
            if the_list[j] > the_list[j+1]:
                the_list[j+1], the_list[j] = the_list[j], the_list[j+1]
                
            nops += 1
                
    return the_list, nops       

def quick_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Quicksort
    """
    
    nops = 0    
    
    if len(the_list) <= 1:
        return the_list, nops
    
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
            
        nops += 1
        
    qless, lnops = quick_sort(less)  
    qmore, mnops = quick_sort(more)
    
    return (qless + pivot + qmore), (nops + lnops + mnops) 

def merge(left, right): 
    
    nops = 0
    result = []
    
    left_len = len(left)
    right_len = len(right)
    
    l_idx = 0
    r_idx = 0
    
    while l_idx < left_len and r_idx < right_len:
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
            
        nops += 1
    
    result.extend(left[l_idx:])
    result.extend(right[r_idx:])
    
    return result, nops

def merge_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Merge_sort
    """
    
    if len(the_list) <= 1:
        return the_list, 0
    
    middle_pos = len(the_list) / 2
            
    left, lnops = merge_sort(the_list[:middle_pos])
    right, rnops = merge_sort(the_list[middle_pos:])
    
    mresult, mnops = merge(left, right)
    
    return mresult, mnops + lnops + rnops

def tim_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Timsort
    """
    
    return the_list, 0

def generate_random_list():
        
    random.seed(THE_SEED)
    
    the_list = [int(MULT * random.random()) for _ in xrange(NUM_ELTS)]
    
    return the_list

def perform_sort(sort_name, sort_fun):
    
    print "- Trying %s sort ..." % sort_name
    
    the_list = generate_random_list()    
    
    start = time.time()
    
    list_sorted, nops = sort_fun(the_list)
    
    end = time.time()
    
    print "%d operations. Time elapsed: %s s." % (nops, end - start)
    
    test_sort(list_sorted)    

def main():
    
    sorting_algos = { "selection" : selection_sort,
                      "insertion" : insertion_sort,
                      "bubble": bubble_sort,
                      "quick" : quick_sort,
                      "merge" : merge_sort,
                      "timsort": tim_sort }
    
    for k, v in sorting_algos.items():    
        perform_sort(k, v)

if __name__ == "__main__":
    
    main()