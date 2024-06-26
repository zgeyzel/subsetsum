from typing import Iterator, List
from ctypes import c_longlong
import _subsetsum as _cpp

__version__ = _cpp.__version__


def solutions(nums: List[c_longlong], target: c_longlong) -> Iterator[List[c_longlong]]:
    """Enumerates all solutions to SUBSET-SUM. If `nums` is empty,
        no solutions will be generated.

    Args:
        nums (List[long long]): A list of integers (positive or negative)
            from which subsets will be generated
        target (long long): The target value (positive or negative) for the
            sum of each subset

    Returns:
        Iterable: An iterator over the set of solutions, where each
            solution is a list of integers that index into the original
            list `nums` to form a subset
    """

    solver = _cpp.Solver(nums, target)

    if not solver.hasSolution():
        return
        yield

    solver.initSolutionIterator()
    solution = solver.getNextSolution()
    while solution:
        yield solution
        solution = solver.getNextSolution()


def has_solution(nums: List[c_longlong], target: c_longlong) -> bool:
    """Determines if there is a subset of `nums` which sums to
        `target`. If `nums` is empty, the result is always false.

    Args:
        nums (List[long long]): A list of integers (positive or negative)
            for the SUBSET-SUM problem
        target (long long): The target value (positive or negative) which
            will be used in the SUBSET-SUM problem

    Returns:
        bool: True if there exists a subset of `nums` which sums to
            `target`, otherwise false
    """

    return _cpp.Solver(nums, target).hasSolution()
