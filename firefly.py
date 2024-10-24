import math
import random
import pandas as pd

def random_decision(lb, ub):
    return (lb + (ub - lb) * random.random())

def griewank(solution: list) -> float:
    summation, product_notaion = 0.0, 1

    for num in solution:
        summation += num**2 / 4000
        product_notaion *= math.cos(num / math.sqrt((solution.index(num)+1)))
        
    return summation - product_notaion + 1

population = []
solution = []
dimension = 5
pop_size = 10

for j in range(pop_size):
    solution = []
    for i in range(dimension):
        solution.append(random_decision(-10, 10))

    population.append(solution)
    print(f"solution {j+1} at t=1: {population[j]}")

fitness_values = []
for k in range(pop_size):
    fitness_values.append(griewank(population[k]))
    print(f"fitness values: {k+1} : {fitness_values[k]}")

solfit = []
dec_var = []

for i in range(dimension):
    dec_var.append(str(i + 1))

for i in range(pop_size):
    temp = []
    temp = population[i]

    temp.append(fitness_values[i])
    solfit.append(temp)

dec_var.append("fitness")
df = pd.DataFrame(solfit)
df.columns = dec_var
print("Unsorted Population")
print(df)

sorted_firefly = df.sort_values("fitness")
print("Sorted Population")
print(sorted_firefly)

x_j_better = (list(sorted_firefly.iloc[0]))[0:dimension]
x_i_notbetter = (list(sorted_firefly.iloc[pop_size - 1]))[0:dimension]

print(f"More Attractive : {x_j_better}")
print(f"Less Attractive : {x_i_notbetter}")

summation = 0 # T
attractiveness_param = 1    # Attractiveness param
light_absorption_coeff = 1     # Light Absorption Coeff
levy_flight_param = 1       
t = 1
random_param = random.random() # Levy Flight Param

for k in range(dimension):
    summation = summation + ((x_j_better[k] - x_i_notbetter[k]) * (x_j_better[k] - x_i_notbetter[k]))

r2 = summation

second_partial = attractiveness_param * math.exp(-light_absorption_coeff *r2)

second_term = [second_partial * (a - b) for a, b in zip(x_j_better, x_i_notbetter)]

if (random.random() - 0.50) < 0: sign = -1
else: sign = 1

third_partial1 = random_param * sign
third_term = [third_partial1 * i * t**(-levy_flight_param) for i in x_i_notbetter]

new_pos = [a + b + c for a, b, c in zip(x_i_notbetter, second_term, third_term)]
print(f"Old Position : {x_i_notbetter}")
print(f"OLD Fitness Value : {griewank(x_i_notbetter)}")
print(f"New Position : {new_pos}")
print(f"NEW Fitness Value : {griewank(new_pos)}")