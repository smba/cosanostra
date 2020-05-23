import numpy as np
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set
import space.util as util
import z3


def distance_based_sampling(
        fm: Sequence[Sequence[int]],
        features: dict,
        size: int,
) -> np.ndarray:
    '''

    :param fm:
    :param size:
    :return:
    '''

    n_options = len(features)
    origin = z3.BitVecVal("0" * n_options, n_options)

    clauses, target = util.dimacs_to_bit_model(fm, n_options)
    clauses = z3.And(clauses)

    solver = z3.Solver()

    # add esxisting constraints to solver
    solver.add(clauses)

    # set of existing solutions
    solutions = []
    for i in range(size):
        print(i)
        while True:
            # sample a random distance
            distance = np.random.randint(0, n_options)
            solver.add(__hamming(origin, target, 1) == distance)

            if solver.check() == z3.unsat:
                # remove distance based constraint
                constraints = solver.assertions()
                solver.reset()
                solver.add(constraints[:-1])

            else: # solver.check() == z3.sat
                solution = solver.model()[target]

                # add current solution to solver assertions = new constraint
                solver.add( target != solution )

                # add current solution to set of solutions
                solutions.append(solution)

                break

    return solutions

def t_wise_sampling(
        fm: Sequence[Sequence[int]],
        size: int,
        negative: bool = False,
        t: int = 1,
        cumulative: bool = False
) -> np.ndarray:
    '''

    :param fm: list representation of the feature model
    :param size: number of configurations to sample
    :param negative: enables negative-feature/twise sampling
    :param t: degree of interactions to sample; if cumulative=True, t is the max. degree of interactions
    :param cumulative: sample interactions degrees up to t
    :return: numpy array with configurations
    '''
    pass

def random_sampling(
        fm: Sequence[Sequence[int]],
        size: int
) -> np.ndarray:
    '''

    :param fm:
    :param size:
    :return:
    '''
    pass

def __config_to_int(config: np.ndarray) -> int:
    '''

    :param config:
    :return:
    '''
    pass

def __int_to_config(i: int, n_options: int) -> np.ndarray:
    '''

    :param i:
    :param n_options:
    :return:
    '''

    offset = n_options - int(np.ceil(np.log2(i)))
    binary_string = "0" * offset + str(bin(i))[2:]
    assert(len(binary_string) == n_options)

    binary = np.array([int(bit) for bit in binary_string])
    return binary

def __hamming(V1, V2, target):
    h = V1 ^ V2
    s = max(target.bit_length(), V1.size().bit_length())
    return z3.Sum([z3.ZeroExt(s, z3.Extract(i, i, h)) for i in range(V1.size())])

if __name__ == "__main__":

    a = __int_to_config(42, 10)
    print(a)