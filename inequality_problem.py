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


def calc_critical_pts(ineqs, verbose = False):
    """
    Calculates the critical points in a list of random inequalities. i.e. the
    places where a '<' is followed by a '>' or vice-versa.
    """
    critical_pts = [0]
    critical_pt_diffs = []
    critical_max_pts = []
    critical_min_pts = []
    
    #ADDED SOMETHING HERE
    #TODO: Replace all of this with simpler system with no need for critical_pts
    #create list that represents the empty gaps between inequalities with'min',
    #'max', 'incr' or 'decr'. Then populate this list with the correct integers
    #from the sorted list.
    no_ineqs = len(ineqs)
    for i in range(no_ineqs - 1): 
        if ineqs[i] != ineqs[i+1]:  #find the critical points
            critical_pts.append(i+1)
            end = len(critical_pts) - 1  #calculate gap between crit pts
            critical_pt_diffs.append(critical_pts[end] - critical_pts[end-1])
            
    critical_pts.append(no_ineqs) #add the final critical point
    critical_pt_diffs.append(critical_pts[-1] - critical_pts[-2])
    
    #find if first and last spaces are crit mins or crit maxs
    if ineqs[0] == '<':
        critical_min_pts.append(0)
    else:
        critical_max_pts.append(0)
    if ineqs[no_ineqs - 1] == '<':
        critical_max_pts.append(no_ineqs)
    else:
        critical_min_pts.append(no_ineqs)
    
    #categorise the rest of the critical points    
    for critpt in critical_pts[1:len(critical_pts)-1]: #TODO: replace with [1:-1]
        if ineqs[critpt-1] == '>' and ineqs[critpt] == '<':
            critical_min_pts.append(critpt)
        else:
            critical_max_pts.append(critpt)
    
    if verbose == True:
        print("The inequalities: ", ineqs)
        print("The critical points are: ", critical_pts)
        print("The critical differences are: ", critical_pt_diffs)
        print("The critical maximums are: ", critical_max_pts)
        print("The critical minimums are: ", critical_min_pts)
            
    return [critical_pts, critical_pt_diffs, critical_max_pts,
            critical_min_pts]
            
    
def place_ints(ints, ineqs, crits):
    """
    Places the maximum and minimum numbers in the list in the critical places
    between the inequalities. Then fills the remainder of the places with
    ordered numbers.
    """
    N = len(ints)
    ints.sort()       
    ineqs = ineqs               #not necessary
    correct_order = [0]*N
    max_index = N-1 #Can use .pop() to do away with max index
    min_index = 0
    critical_pts = crits[0]
    critical_pt_diffs = crits[1]
    critical_max_pts = crits[2]
    critical_min_pts = crits[3]
    
    for critpt in critical_max_pts:
        correct_order[critpt] = ints[max_index]
        max_index = max_index - 1
    
    for critpt in critical_min_pts:
        correct_order[critpt]  = ints[min_index]
        min_index = min_index + 1
    
    #place the rest of the points based on number of empty spaces
    backstop = 0
    for crit_diff in critical_pt_diffs:
        if crit_diff > 1:
            crit_index =  critical_pt_diffs.index(crit_diff, backstop)
            crit_value = critical_pts[crit_index]
            place_value = crit_value + 1
            if ineqs[crit_value] == '>':
                for i in range(crit_diff - 1):
                    correct_order[place_value] = ints[max_index]
                    place_value = place_value + 1
                    max_index = max_index - 1
            else:
                for i in range(crit_diff - 1):
                    correct_order[place_value] = ints[min_index]
                    place_value = place_value + 1
                    min_index = min_index + 1
        backstop +=1
    
    return correct_order
            
        
def solve_ineq_problem(N = 10, verbose = False, ret_ineqs = False):
    """
    Solves the inequality problem for N distinct integers and N-1 random
    inequalities. 
    Returns a list with the integers arranged into the correct order.
    """
    ints = N_distinct_int(N)
    ineqs = random_inequalities(N-1)
    crits = calc_critical_pts(ineqs, verbose)
    solution = place_ints(ints,ineqs,crits)
    
    if ret_ineqs == False:
        return solution
    else:
        return [solution,ineqs]

def solve_and_print(N = 10, verbose = False):
    """
    Solves the inequality problem for N distinct integers and N-1 random 
    inequalities, then the integers placed between the inequalities.
    
    If verbose = True, then details of the integers, inequalities and critical
    points are also printed
    """
    sol = solve_ineq_problem(N,verbose, ret_ineqs = True)
    ints = sol[0]
    ineqs = sol[1]
    printable = ''
    for i in range(N):
        if i == N - 1:
            printable += str(ints[i])
        else:
            printable += (str(ints[i]) + ' ' + str(ineqs[i]) + ' ')
            
    print(printable)
    
solve_and_print()


    
    
    
    
