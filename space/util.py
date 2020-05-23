import numpy as np
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set
import z3

def parse_dimacs(path: str) -> Sequence[Sequence[int]]:
    '''

    :param path:
    :return:
    '''

    dimacs = list()
    dimacs.append(list())
    with open(path) as mfile:
        lines = list(mfile)

        # parse names of features from DIMACS comments (lines starting with c)
        feature_lines = list(filter(lambda s: s.startswith("c"), lines))
        features = dict(map(lambda l: (int(l.split(" ")[1]), l.split(" ")[2].replace("\n", "")), feature_lines))
        print(features)

        # remove comments
        lines = list(filter(lambda s: not s.startswith("c"), lines))
        n_options = int(lines[0].split(" ")[2])

        for line in lines:
            tokens = line.split()
            if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                for tok in tokens:
                    lit = int(tok)
                    if lit == 0:
                        dimacs.append(list())
                    else:
                        dimacs[-1].append(lit)
        assert len(dimacs[-1]) == 0
        dimacs.pop()

    return dimacs

def __dimacs_to_bool_model(dimacs: Sequence[Sequence[int]]) -> Sequence[z3.And]:
    '''

    :param dimacs:
    :return:
    '''
    pass

def __dimacs_to_bit_model(dimacs: Sequence[Sequence[int]], n_options: int) -> Sequence[z3.Or]:
    '''

    :param dimacs:
    :return:
    '''

    clauses = []

    target = z3.BitVec('target', n_options)

    # add clauses of variability model
    for clause in dimacs:
        c = []
        for opt in clause:
            opt_sign = 1 if opt >= 0 else 0
            optid = n_options - abs(opt)
            c.append(z3.Extract(optid, optid, target) == opt_sign)

        clauses.append(z3.Or(c))

    return clauses