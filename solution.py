import random
from util import cost, best_path
from two_opt import two_opt


def ga_tsp(initial_population, distances, generations):

    # basic input checks so we don't crash later
    if initial_population is None or distances is None or generations is None:
        raise ValueError("Invalid argument")
    if generations <= 0:
        raise ValueError("Invalid argument")

    # combine two parent paths into a new child path
    def crossover(p1, p2):
        size = len(p1)

        # pick a random chunk from parent 1
        start, end = sorted(random.sample(range(size), 2))

        child = [None] * size
        child[start:end] = p1[start:end]

        # fill in remaining cities from parent 2 (skip duplicates)
        fill = [c for c in p2 if c not in child]

        idx = 0
        for i in range(size):
            if child[i] is None:
                child[i] = fill[idx]
                idx += 1

        return tuple(child)

    # start with whatever population we were given
    population = initial_population

    # run the genetic algorithm for the given number of generations
    for _ in range(generations):

        # sort by cost so best paths come first
        population = sorted(population, key=lambda p: cost(p, distances))

        # keep top half as parents
        parents = population[:len(population)//2]

        children = []

        # keep generating children until we refill population
        while len(children) < len(population):

            # randomly pick two parents
            p1, p2 = random.sample(parents, 2)

            # create a child from them
            child = crossover(p1, p2)

            # try to improve the child a bit using 2-opt
            # made a big difference in results
            child = two_opt(child, distances)

            children.append(child)

        # combine parents + children for next generation
        population = parents + children

        # keep only the best ones
        population = sorted(population, key=lambda p: cost(p, distances))
        population = population[:len(initial_population)]

    # return the best path we ended up with
    return best_path(population, distances)
