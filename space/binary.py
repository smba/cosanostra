import numpy as np
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set
import z3

def distance_based_sampling(
        fm: Sequence[Sequence[int]],
        size: int,
) -> np.ndarray:
    '''<s

    :param fm:
    :param size:
    :return:
    '''
    pass

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

def __config_to_vector(config: np.ndarray) -> z3.BitVecVal:
    '''

    :param config:
    :return:
    '''
    pass

def __vector_to_config(vector: z3.BitVecVal) -> np.ndarray:
    '''

    :param vector:
    :return:
    '''
    pass

def __parse_dimacs(path: str) -> Sequence[Sequence[int]]:
    '''

    :param path:
    :return:
    '''
    pass