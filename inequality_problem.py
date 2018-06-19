# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:06:30 2018

@author: btrev

Places N distinct integers in a sequence of N-1 random inequalities.
"""

import sys
from random import sample, randint

def n_distinct_int(n):
    """Returns a list of n distinct integers between 1 and 2n."""
    selection = range(1,2*n)
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
    assert type(ints) == list and ints != [],\
           "Pass a list containing at least one integer." 
    assert len(ineqs) == len(ints)-1,\
           "There must be one fewer inequality than there are integers."
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
            
def solve_ineq_problem(n=10, verbose='v'):
    """
    Solves the inequality problem for n distinct integers and n-1 random
    inequalities. 
    Returns a string with the integers placed bewteen the inequalities in the
    correct order. The string is printed if verbose='v'
    """
    ints = n_distinct_int(n)
    ineqs = random_inequalities(n-1)
    soln = place_ints(ints,ineqs)
    printable = ' '.join(f'{i} {ineq}' for i, ineq in zip(soln,ineqs + ['']))
    if verbose == 'v':
        print(printable.strip())
    return printable
    
def main(argv=None):
    """Command line argument is N, must be integer"""
    if argv is None:
        argv = sys.argv
        if len(argv) == 3:
            #used for verbosity
            solve_ineq_problem(int(argv[1]), argv[2])
        elif len(argv) == 2:
            #defining n in the problem
            solve_ineq_problem(int(argv[1]))
        else:
            solve_ineq_problem()
    return 0

if __name__ == '__main__':
    sys.exit(main())
    
    
    
    
