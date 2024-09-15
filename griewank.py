import math

# Constants
solution = [2.1176, -7.2032, -5.60033, -2.83838, 9.40210]
fitness_value = [1.060184, 1.029211, 1.160927, 1.245041, 1.002926]
optimal_function = 0.0

def griewank(solution: list) -> float:
    summation, product_notaion = 0.0, 1

    for num in solution:
        summation += num**2 / 4000
        product_notaion *= math.cos(num / math.sqrt((solution.index(num)+1)))
        
    return summation - product_notaion + 1

print(griewank(solution))

# Computes the Strength of all Fitness Value of each solution, not Strength of all Solutions.
def strength(solution: list, optimal) -> list:
    strength = []
    denominator = 0.0
    
    for num in solution:
        denominator += 1/abs(num - optimal)
        
    for num in solution:
        numerator = 1/abs(num - optimal)
        strength.append(numerator/ denominator)
    
    return strength

print(strength(fitness_value, optimal_function))