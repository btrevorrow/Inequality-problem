# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:15:45 2018

@author: btrev
"""

import inequality_problem as ip
import unittest

class TestDistincInts(unittest.TestCase):
    
    def test_n_distinct_ints(self):
        test_n = [1,10,100,999999]
        for n in test_n:
            with self.subTest(n=n):
                #check numer of integers = n
                ints = ip.n_distinct_int(n)
                self.assertEqual(n, len(ints)) 
                #check the integers are all distinct
                unique_ints = set(ints)
                self.assertEqual(len(ints), len(unique_ints))
        
    def test_solve_ineq_problem(self):    
        """Check the problem has been solved correctly."""
        test_n = [1,10,100,10000]
        for n in test_n:
            with self.subTest(n=n):
                solution = ip.solve_ineq_problem(n,'c')
                #should evaluate as True if solved correctly
                self.assertTrue(eval(solution))
                
        #check for exception when n is a negative number        
        with self.assertRaises(ValueError):
            ip.solve_ineq_problem(-1,'c')
            
        #check for exception when n is zero
        with self.assertRaises(AssertionError):
            ip.solve_ineq_problem(0)
            
        other_n = [7.2,'a',[],None,(10,11)]
        for n in other_n:
            with self.subTest(other_n = n):
                with self.assertRaises(TypeError):
                    ip.solve_ineq_problem(n,'c')
        
                
                
if __name__ == '__main__':
    unittest.main()