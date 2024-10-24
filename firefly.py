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
dimension = 5
pop_size = 10

for j in range(pop_size):
    solution = []
    for i in range(dimension):
        solution.append(random_decision(-10, 10))

    population.append(solution)

fitness_values = []
for k in range(pop_size):
    fitness_values.append(griewank(population[k]))

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
print(f"{40 * "-"} Unsorted Population {40 * "-"}")
print(df)

sorted_firefly = df.sort_values("fitness")
print(f"\n{40 * "-"} Sorted Population {40 * "-"}")
print(sorted_firefly)

x_j_better = (list(sorted_firefly.iloc[0]))[0:dimension]
x_i_notbetter = (list(sorted_firefly.iloc[pop_size - 1]))[0:dimension]

print(f"\n{40*"-"} More Attractive {40*"-"}")
print(f"Firefly {sorted_firefly.iloc[0].name} : {x_j_better}")

print(f"\n{40*"-"} Less Attractive {40*"-"}")
print(f"Firefly {sorted_firefly.iloc[-1].name}: {x_i_notbetter}")

summation = 0 
attractiveness_param = 1    
light_absorption_coeff = 1     
levy_flight_param = 1       
t = 1
random_param = random.random() 

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
print(f"\n{40*"-"} (BEFORE) Less Attractive Firefly {40*"-"}")
print(f"Old Position : {x_i_notbetter}")
print(f"OLD Fitness Value : {griewank(x_i_notbetter)}")
print(f"\n{40*"-"} (AFTER) Less Attractive Firefly {40*"-"}")
print(f"New Position : {new_pos}")
print(f"NEW Fitness Value : {griewank(new_pos)}")