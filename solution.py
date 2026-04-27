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
        idx = 0
        for i in range(size):
            if child[i] is None:
                child[i] = fill[idx]
                idx += 1
        return tuple(child)

    population = initial_population

    for _ in range(generations):
        population = sorted(population, key=lambda p: cost(p, distances))
        parents = population[:len(population)//2]

        children = []
        while len(children) < len(population):
            p1, p2 = random.sample(parents, 2)
            child = crossover(p1, p2)
            children.append(child)

        population = parents + children
        population = sorted(population, key=lambda p: cost(p, distances))
        population = population[:len(initial_population)]

    return best_path(population, distances)
