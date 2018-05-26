# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 16:06:30 2018

@author: btrev
"""

from random import sample
from random import randint

def N_distinct_int(choose = 10, maximum = 25):
    """
    Creates a list of 10 distinct integers within the range specified.
    """
    Range = range(1,maximum+1)
    rand_distinct = sample(Range,choose)
    return rand_distinct


def random_inequalities(N = 9):
    """
    Creates a list of N random inequalities, either < or >.
    """
    ineq = ['<','>']
    rand_ineq = []
    for i in range(N):
        rand_binary = randint(0,1)
        rand_ineq.append(ineq[rand_binary])
        
    return rand_ineq


def categorise_ineqs(ineqs, verbose = False):
    """
    Categorises the points between the inequalities: 'min' if '>' is followed
    by '<'. 'max' if '<' is followed by '>'. 'incr' if '<' is followed by '<'
    and 'decr' if '>' is followed by '>'. Returns a list which indicates the
    type of each point.
    """
    categorised = []
      
    if ineqs[0] == '<':                 #categorise first point
        categorised.append('min')
    else:
        categorised.append('max')
        
    for i in range(len(ineqs)-1):       #categorise the middle points
        if ineqs[i] == '<' and ineqs[i+1] == '>':
            categorised.append('max')
        elif ineqs[i] == '<' and ineqs[i+1] == '<':
            categorised.append('incr')
        elif ineqs[i] == '>' and ineqs[i+1] == '<':
            categorised.append('min')
        else:
            categorised.append('decr')
    
    if ineqs[-1] == '<':                #categorise the final point
        categorised.append('max')
    else:
        categorised.append('min')
        
    if verbose == True:
        print("The inequalities: ", ineqs)
        print("The categorised points are", categorised)

    
    return categorised
    
def place_ints(ints, ineqs):
    """
    Places the maximum and minimum numbers in the list in the critical places
    between the inequalities. Then fills the remainder of the places with
    ordered numbers.
    """
    correct_order = categorise_ineqs(ineqs)
    ints.sort()
    
    for i in range(len(correct_order)):      #populate max and min points
        if correct_order[i] == 'max':
            correct_order[i] = ints.pop()
        elif correct_order[i] == 'min':
            correct_order[i] = ints.pop(0)
    
    for i in range(len(correct_order)):      #populate incr and decr points
        if correct_order[i] == 'decr':
            correct_order[i] = ints.pop()
        elif correct_order[i] == 'incr':
            correct_order[i] = ints.pop(0)
            
    return correct_order
            
def solve_ineq_problem(N = 10, ret_ineqs = False):
    """
    Solves the inequality problem for N distinct integers and N-1 random
    inequalities. 
    Returns a list with the integers arranged into the correct order.
    """
    ints = N_distinct_int(N,N*2)
    ineqs = random_inequalities(N-1)
    solution = place_ints(ints,ineqs)
    
    if ret_ineqs == False:
        return solution
    else:
        return [solution,ineqs]

def solve_and_print(N = 10):
    """
    Solves the inequality problem for N distinct integers and N-1 random 
    inequalities, then the integers placed between the inequalities.
    
    If verbose = True, then details of the integers, inequalities and critical
    points are also printed
    """
    sol = solve_ineq_problem(N, ret_ineqs = True)
    ints = sol[0]
    ineqs = sol[1]
    printable = ''
    for i in range(N):
        if i == N - 1:
            printable += str(ints[i])
        else:
            printable += (str(ints[i]) + ' ' + str(ineqs[i]) + ' ')
            
    print(printable)
    
solve_and_print(20)


    
    
    
    
