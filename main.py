import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from random import randint, choice
from sklearn.model_selection import train_test_split


def plot_population_hist(population):

    plt.hist(population, bins=range(300), range=300)
    plt.show()


def create_persons(no_of_population, initial_coins=20):
    population = [initial_coins for i in range(no_of_population)]

    plot_population_hist(population)

    return population

"""
def play_turn(population):

    # We would split population into 2 halves and match them with each other respectively for coin toss
    index_of_population_a, index_of_population_b = train_test_split(range(len(population)),
                                                                    test_size=.5,
                                                                    random_state=randint(0,10000))
    # print(index_of_population_a, index_of_population_b)


    # Well ideally we can just say that those who are on a side wins, and those on b sides looses
    # and make our distribution. after all the split was made randomly,
    # but still lets make a coin toss each time for both sides players

    for a, b in zip(index_of_population_a, index_of_population_b):

        # if any one of a or b is poor(zero coin) to play, toss does not happen.
        # they will stay poor all along for our 1st economy


        # if 0 'a' wins, if 1 'b' wins
        toss_result = randint(0,1)

        if (population[a] == 0) and (population[b] == 0):
            continue

        elif population[a] == 0:
            if toss_result:
                # a wins, and b gives 1 coin to a
                population[a] = population[a] + 1
                population[b] = population[b] - 1
            else:
                continue

        elif population[b] == 0:
            if toss_result:
                continue
            else:
                # a wins, and b gives 1 coin to a
                population[a] = population[a] + 1
                population[b] = population[b] - 1
        else:
            if toss_result:
                # a wins, and b gives 1 coin to a
                population[a] = population[a] + 1
                population[b] = population[b] - 1
            else:
                # b wins and a gives 1 coin to b
                population[a] = population[a] - 1
                population[b] = population[b] + 1

    return population
"""

def play_turn(population):

    # We would split population into 2 halves and match them with each other respectively for coin toss
    index_of_population_a, index_of_population_b = train_test_split(range(len(population)),
                                                                    test_size=.5,
                                                                    random_state=randint(0,10000))

    for a, b in zip(index_of_population_a, index_of_population_b):

        # if any one of a or b is poor(zero coin) to play, toss does not happen.
        # they will stay poor all along for our 1st economy

        # if 0 'a' wins, if 1 'b' wins
        toss_result = randint(0, 1)

        if (population[a] == 0) and (population[b] == 0):
            continue

        elif population[a] == 0:
            if toss_result:
                # a wins, and b gives 1 coin to a
                population[a] = population[a] + 1
                population[b] = population[b] - 1
            else:
                continue

        elif population[b] == 0:
            if toss_result:
                continue
            else:
                # a wins, and b gives 1 coin to a
                population[a] = population[a] + 1
                population[b] = population[b] - 1
        else:
            if toss_result:
                # a wins, and b gives 1 coin to a
                population[a] = population[a] + 1
                population[b] = population[b] - 1
            else:
                # b wins and a gives 1 coin to b
                population[a] = population[a] - 1
                population[b] = population[b] + 1

    return population


if __name__ == "__main__":

    no_of_population = 10000
    no_of_turns = 10000

    population = create_persons(no_of_population)

    for i in range(no_of_turns):

        population = play_turn(population)

        if i % 100 == 0:
            plot_population_hist(population)
            #input("Enter : ")