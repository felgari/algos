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
        print "The sorting is NOT ok."

def quick_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Quicksort
    """
    
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
    
    return quick_sort(less) + pivot + quick_sort(more) 

def bubble_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Bubble_sort
    """
    
    max_pos = len(the_list) - 1
    
    for i in range(max_pos):
        for j in range(0, max_pos - i):
            if the_list[j] > the_list[j+1]:
                the_list[j+1], the_list[j] = the_list[j], the_list[j+1]
                
    return the_list  

def merge(left, right): 
    
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
    
    result.extend(left[l_idx:])
    result.extend(right[r_idx:])
    
    return result

def merge_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Merge_sort
    """
    
    if len(the_list) <= 1:
        return the_list
    
    middle_pos = len(the_list) / 2
            
    left = merge_sort(the_list[:middle_pos])
    right = merge_sort(the_list[middle_pos:])
    
    return merge(left, right)

def selection_sort(the_list):
    """Reference: https://en.wikipedia.org/wiki/Selection_sort
    """
    
    for j in range(len(the_list)):
        
        mini = j
        
        for i in range(j + 1, len(the_list)): 
            
            if the_list[i] < the_list[mini]:
                mini = i
                
        if min != j:
            the_list[mini], the_list[j] = the_list[j], the_list[mini]
    
    return the_list

def generate_random_list():
        
    random.seed(THE_SEED)
    
    the_list = [int(MULT * random.random()) for _ in xrange(NUM_ELTS)]
    
    return the_list

def main():
    
    the_list = generate_random_list()
    
    print "Trying selection sort."
    
    list_sorted = selection_sort(the_list)
    
    test_sort(list_sorted)
    
    print "Trying quick sort."
    
    the_list = generate_random_list()
    
    list_sorted = quick_sort(the_list)
    
    test_sort(list_sorted)    
    
    print "Trying bubble sort."
    
    the_list = generate_random_list()
    
    list_sorted = bubble_sort(the_list)
    
    test_sort(list_sorted)
    
    print "Trying merge sort."
    
    the_list = generate_random_list()
    
    list_sorted = merge_sort(the_list)
    
    test_sort(list_sorted)

if __name__ == "__main__":
    
    main()