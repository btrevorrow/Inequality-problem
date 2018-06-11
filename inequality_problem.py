# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:06:30 2018

@author: btrev

Places N distinct integers in a sequence of N-1 random inequalities.
"""

import sys
from random import sample, randint

def n_distinct_int(n=10, maximum=25):
    """Returns a list of 10 distinct integers between 1 and maximum(=25)."""
    selection = range(1,maximum+1)
    return sample(selection,n)

def random_inequalities(n=9):
    """ Creates a list of n random inequalities, either < or >."""
    ineq = ['<','>']
    return [ineq[randint(0,1)] for i in range(n)]
    
def place_ints(ints, ineqs):
    """
    Sorts the integers into an ordered list from minimum to maximum. If the
    next inequality is '<' then the minimum in the list is placed before it. If
    the inequality is '>' then the maximum in the list is chosen.
    """
    ints.sort()
    correct_order = []
    
    for ineq in ineqs:
        if ineq == '<':
            correct_order.append(ints.pop(0))
        elif ineq == '>':
            correct_order.append(ints.pop())
            
    #append the final integer
    correct_order.append(ints.pop())
    return correct_order
            
def solve_ineq_problem(n=10, ret_ineqs=False):
    """
    Solves the inequality problem for n distinct integers and n-1 random
    inequalities. 
    Returns a list with the integers arranged into the correct order.
    The inequalities are also returned if ret_ineqs == True
    """
    ints = n_distinct_int(n,n*2)
    ineqs = random_inequalities(n-1)
    solution = place_ints(ints,ineqs)
    
    if ret_ineqs == False:
        return solution
    else:
        return [solution,ineqs]

def solve_and_print(n=10):
    """
    Solves the inequality problem for n distinct integers and n-1 random 
    inequalities, then prints a string with the integers placed between the 
    inequalities.
    """
    ints, ineqs = solve_ineq_problem(n, ret_ineqs = True)
    printable = ' '.join(f'{i} {ineq}' for i, ineq in zip(ints,ineqs + ['']))
    print(printable.strip())
    
def main(argv=None):
    """Command line argument is N, must be integer"""
    if argv is None:
        argv = sys.argv
        solve_and_print(int(argv[1]))
    return 0

if __name__ == '__main__':
    sys.exit(main())
    
    
    
    
