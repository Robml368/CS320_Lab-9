import random
from util import cost, best_path
from two_opt import two_opt


def ga_tsp(initial_population, distances, generations):
    if initial_population is None or distances is None or generations is None:
        raise ValueError("Invalid argument")
    if generations <= 0:
        raise ValueError("Invalid argument")

    def crossover(p1, p2):
        size = len(p1)
        start, end = sorted(random.sample(range(size), 2))
        child = [None] * size
        child[start:end] = p1[start:end]
        fill = [c for c in p2 if c not in child]
        for i in range(size):
            if child[i] is None:
                child[i] = fill.pop(0)
        return tuple(child)
