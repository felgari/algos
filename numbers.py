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

"""Algorithms about numbers.
"""

import sys
import math
import time

NUM_ARGS = 3

def euclides(n1, n2):
    """Reference: https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
        
    it = 0
    a, b = (n1, n2) if n1 > n2 else (n2, n1)
    
    while b:
        d = a - b 
        a, b = (b, d) if b > d else (d, b) 
        it += 1

    return a, it

def euclides_div(n1, n2):
    """Reference: https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
    
    it = 0    
    a, b = (n1, n2) if n1 > n2 else (n2, n1)
    
    while b:
        c = a % b 
        a, b = (b, c) if b > c else (c, b) 
        it += 1        
   
    return a, it

def binary_gcd(n1, n2):
    """Reference: https://en.wikipedia.org/wiki/Binary_GCD_algorithm
    """
    it1 = it2 = it3 = 0
    shift = 0
    
    while not ( ( n1 | n2 ) & 1 ):
        n1 >>= 1
        n2 >>= 1
        
        shift += 1
        
        it1 += 1
        
    while not (n1 & 1):
        n1 >>= 1
        
        it2 += 1
        
    while n2:
        while not (n2 & 1):
            n2 >>= 1
            it3 += 1
            
        if n1 > n2:
            n1, n2 = n2, n1
            
        n2 = n2 - n1       
        
    return n1 << shift, max(it1, it2, it3)

def gcd_mcm(n1, n2):
    
    if n1 > 0 and n2 > 0:
        print "- GCD"
        
        print "GCD with Euclides algo is: %d (with %d iterations)" \
            % euclides(n1, n2)
            
        gcd, it = euclides_div(n1, n2)
                    
        print "GCD with Euclides algo using division is: %d (with %d iterations)" \
            %  (gcd, it)
               
        print "GCD with Binary GCD is: %d (with %d iterations)" \
            % binary_gcd(n1, n2)
            
        print "MCM is %d" % ( n1 * n2 / gcd)
    else:    
        print "For GCD arguments must be integer numbers greater than 0."
        
def is_prime(n):
    
    is_prim = True
    
    if n > 1:
        root = int(math.sqrt(n) + 0.1) + 1
        
        for i in range(2, root):
            if n % i == 0:
                is_prim = False
                break
        
    return is_prim      

def sieve_of_Eratosthenes(n):
    """Reference:https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes 
    """
    
    it = 0
    primes = [True] * (n + 1)
    
    if n > 1:
        root = int(math.sqrt(n) + 0.1) + 1
        
        for i in range(2, root):
            if primes[i]:
                base = i ** 2
                for j in range(0, n):                    
                    it += 1                    
                    
                    idx = base + j * i
                    
                    if idx > n:
                        break

                    primes[idx] = False  
    
    return [i for i in range(2, n+1) if primes[i]], it  

def other_sieve_for_primes(n):
    
    it = 0
    primes = [True] * (n + 1)
    
    if n > 1:
        
        root = int(math.sqrt(n) + 0.1) + 1
        
        for i in range(2, root):
            if primes[i]:
                for j in range(2, n):
                    it += 1
                                        
                    idx = i * j
                    
                    if idx > n:
                        break
    
                    primes[idx] = False  
    
    return [i for i in range(2, n+1) if primes[i]], it  
        
def primes(n):
    
    print "- PRIMES"
    
    start = int(round(time.time() * 1000.0))
    primes, it = sieve_of_Eratosthenes(n)
    end = int(round(time.time() * 1000.0))
    print "Sieve of Eratosthenes, list of primes until %d has %d in %g s (using %d iterations)" \
        % (n, len(primes), (end - start) / 1000.0, it)
        
    start = int(round(time.time() * 1000.0))
    primes, it = other_sieve_for_primes(n)
    end = int(round(time.time() * 1000.0))
    print "Other sieve, list of primes until %d has %d in %g s (using %d iterations)" \
        % (n, len(primes), (end - start) / 1000.0, it)        
        
    primes = [2]
    [ primes.append(i) for i in range(3,1000) if all(i % n != 0 for n in primes)]
    print "Primes generation using a list comprehension: %s" % primes
    
if __name__ == "__main__":
    
    if len(sys.argv) < NUM_ARGS:
        print"ERROR: Use: %s number1 number2 ..." % sys.argv[0]
    else:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        
        gcd_mcm(n1, n2)
        
        if len(sys.argv) > NUM_ARGS:
            primes(int(sys.argv[3]))
        else:
            primes(n1)
            