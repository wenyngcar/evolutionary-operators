import math
import random

lower_bound = -32.768
upper_bound = 32.768
optimal_function = 0.0

# -------------------------- FUNCTIONS ----------------------------------------

def random_decision(lb, ub):
    return (lb + (ub - lb) * random.random())

def ackley(solution: list):
    dimension = len(solution)
    a = 20
    b = 0.2
    c = 2 * math.pi
    part1 = -b * math.sqrt(1/dimension * sum(x**2 for x in solution))
    part2 = 1 / dimension * sum(math.cos(c * x) for x in solution)

    return -a * math.exp(part1) - math.exp(part2) + a + math.exp(1)

# Recombination
def uniform_crossover(parent1, parent2):
    dimension = len(parent1)
    coin_bias = 0.50
    child1 = []
    child2 = []
    for i in range(dimension):
        random1 = random.random()
        random2 = random.random()
        child1.append(parent1[i]) if random1 < coin_bias else child1.append(parent2[i])
        child2.append(parent1[i]) if random2 < coin_bias else child2.append(parent2[i])

    return child1, child2
    
# Mutation
def inverse_mutation(solution):
    dimension = len(solution)
    index1 = random.randint(0, dimension - 1)
    index2 = random.randint(0, dimension - 1)
    while index1 == index2:
        index2 = random.randint(0, dimension - 1)
    
    if index2 < index1:
        temp = index1
        index1 = index2
        index2 = temp

    section = solution[index1:index2 + 1]
    reverse = section[::-1]
    solution[index1:index2 + 1] = reverse

    return solution

def strength(solution: list, optimal) -> list:
    strength = []
    denominator = 0.0
    
    for num in solution:
        denominator += 1/abs(num - optimal)
        
    for num in solution:
        numerator = 1/abs(num - optimal)
        strength.append(numerator/ denominator)
    
    return strength

def generate_wheel(strength: list) -> list:
    wheel = []
    start = 0.0
    end = strength[0]
    pair = [start, end]
    wheel.append(pair)

    for num in strength:
        pair = []
        if num != 0:
            start = end
            end = start + num
            pair.append(start)
            pair.append(end)
            wheel.append(pair)
    
    return wheel

def select_parent(random_number: float, wheel: list):
    for i in range(len(wheel)):
        if random_number > wheel[i][0] and random_number < wheel[i][1]:
            return i + 1
        else: continue

def solution_fitness(solution:list):
    dimension = len(solution)
    return [ackley(solution[i]) for i in range(dimension)]

# -------------------------- END OF FUNCTIONS ----------------------------------------

population = []
solution = []
dimension = 5
pop_size = 10

# generate population
for j in range(pop_size):
    solution = []
    for i in range(dimension):
        solution.append(random_decision(upper_bound, lower_bound))
    population.append(solution)

sol_fit = solution_fitness(population)

print("-" * 120)
print("After generation of population")
for i in range(pop_size):
    print(f"solution {i+1}: {population[i]}")
    print(f"fitness of solution {i + 1}: {sol_fit[i]}")

for_roulette = strength(sol_fit, optimal_function)

percent = generate_wheel(for_roulette)
parent1 = select_parent(random.random(), percent)
parent2 = select_parent(random.random(), percent)
print("-" * 120)
print(f"Selected Parents")
print(f"Selected_parent1: {parent1}")
print(f"fitness of Selected_parent1: {sol_fit[parent1 - 1]}")
print(f"Selected_parent2: {parent2}")
print(f"fitness of Selected_parent2: {sol_fit[parent2 - 1]}")

offspring1, offspring2 = uniform_crossover(population[parent1 - 1], population[parent2 - 1])
print("-" * 120)
print("After Recombination")
print(f"baby 1: {offspring1}")
print(f"fitness of baby 1 : {ackley(offspring1)}")
print(f"baby 2: {offspring2}")
print(f"fitness of baby2 : {ackley(offspring2)}")

print("-" * 120)
print("After Mutation")
population[parent1 - 1] = inverse_mutation(population[parent1 - 1])
population[parent2 - 1] = inverse_mutation(population[parent2 - 1])
print(f"Mutated_baby 1 : {population[parent1 - 1]}")
print(f"fitness of Mutated_baby 1 : {ackley(population[parent1 - 1])}")
print(f"Mutated_baby 2 : {population[parent2 - 2]}")
print(f"fitness of Mutated_baby 2 : {ackley(population[parent2 - 1])}")