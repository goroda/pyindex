# Copyright (c) 2018, University of Michigan
# Author: Alex Gorodetsky
# Email: goroda@umich.edu
# License: MIT


from __future__ import print_function
import numpy as np
import scipy.special

class TotalOrder:
    """ Total order index set iterator 

    >>> for c in TotalOrder(2, 3):
            print(c)
    >>> [0, 0]
    [0, 1]
    [0, 2]
    [0, 3]
    [1, 0]
    [1, 1]
    [1, 2]
    [2, 0]
    [2, 1]
    [3, 0]

    """
    def __init__(self, dimension, order):
        assert dimension > 0, "Dimension must be greater than zero"
        assert order > -1, "Order must be a positive integer"
        
        self.d_minus_1 = dimension - 1
        self.on_dim = dimension - 1
        self.current_sum = 0
        self.current_inds = [0]*dimension
        self.start = True
        self.max_sum = order
        self.count = int(scipy.special.binom(dimension + order, dimension))
        self.max_indices = [order] * dimension

    def get_count(self):
        return self.count
    
    def get_max_indices(self):
        return self.max_indices
    
    def _print_current_state(self):
        """ Diagnostics Functions """
        print("\n ")
        print("on_dim = ", self.on_dim)
        print("d_minus_1 = ", self.d_minus_1)
        print("current_sum = ", self.current_sum)
        print("max_sum = ", self.max_sum)
        print("current_inds = ", self.current_inds)
        print("start = ", self.start)

    def __iter__(self):
        return self

    def _basefunc(self):

        if 0 <= self.on_dim < self.d_minus_1:
            if self.current_sum < self.max_sum:
                self.current_inds[self.on_dim] = self.current_inds[self.on_dim] + 1
                self.current_sum = self.current_sum + 1
                self.on_dim = self.d_minus_1
                return self.current_inds            
            else: #self.current_sum == self.max_sum
                return self._reset()
        elif self.on_dim == self.d_minus_1:
            if self.current_sum < self.max_sum:
                self.current_inds[self.on_dim] = self.current_inds[self.on_dim] + 1
                self.current_sum = self.current_sum + 1
                return self.current_inds
            else:
                return self._reset()
        else: #self.on_dim == -1
            self.on_dim = self.d_minus_1
            self.current_sum = 0
            self.current_inds = [0]*(self.d_minus_1+1)
            self.start = True
            return None
            
    def _reset(self):
        self.current_sum = self.current_sum - self.current_inds[self.on_dim]
        self.current_inds[self.on_dim] = 0
        self.on_dim = self.on_dim - 1
        return self._basefunc()
        
    def __next__(self):
        # self._print_current_state()
        if self.start is True:
            self.start = False
            return self.current_inds
        else:
            retval = self._basefunc()
            if retval:
                return retval
            else:
                raise StopIteration
        
    next = __next__ # for python2
    
def totalorder1():
    for c in TotalOrder(4, 0):
        print(c)

def totalorder2():
    for c in TotalOrder(1, 2):
        print(c)

def totalorder3():
    for c in TotalOrder(3, 5):
    # for c in TotalOrder(20, 3):
        print(c)

def totalorder4():
    d = list(TotalOrder(3, 5))
    for c in d:
        print(c)

if __name__ == "__main__":

    print("Totalorder 1")
    totalorder1()

    print("\n\n")
    
    print("Totalorder 2")
    totalorder2()

    print("\n\n")
    
    print("Totalorder 3")
    totalorder3()
    
    

