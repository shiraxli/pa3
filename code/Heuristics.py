import numpy as np
import math

"""
Implementations of number partition heuristics.

nums: int numpy array, numbers to be partitioned
start: int numpy array, initial solution
rep: Solution object
n_iter: int, number of optimization iterations
returns: int, residue
"""

def rr(nums, start, rep, n_iter):
    """Repeated Random"""
    n = len(nums)
    soln, res = np.copy(start), rep.residue(start, nums)

    for i in range(n_iter):
        candidate = rep.get_rand(n)
        c_res = rep.residue(candidate, nums)
        if c_res < res:
            soln, res = np.copy(candidate), c_res

    return res


def hc(nums, start, rep, n_iter):
    """Hill Climbing"""
    n = len(nums)
    soln, res = np.copy(start), rep.residue(start, nums)

    for i in range(n_iter):
        candidate = rep.get_neighbor(soln)
        c_res = rep.residue(candidate, nums)
        if c_res < res:
            soln, res = np.copy(candidate), c_res

    return res


def T(i):
    """Cooling Schedule"""
    return (10 ** 10) * (0.8 ** (i // 300))

def sa(nums, start, rep, n_iter):
    """Simulated Annealing"""
    n = len(nums)
    soln, res = np.copy(start), rep.residue(start, nums)
    best_soln, best_res = np.copy(soln), res

    for i in range(n_iter):
        candidate = rep.get_neighbor(soln)
        c_res = rep.residue(candidate, nums)

        if c_res < res or np.random.random_sample() < math.exp(-(c_res - res) / T(i)):
            soln, res = np.copy(candidate), c_res

        if res < best_res:
            best_soln, best_res = np.copy(soln), res

    return res