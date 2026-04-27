import random
from util import cost, best_path
from two_opt import two_opt


def ga_tsp(initial_population, distances, generations):
    if initial_population is None or distances is None or generations is None:
        raise ValueError("Invalid argument")
    if generations <= 0:
        raise ValueError("Invalid argument")
