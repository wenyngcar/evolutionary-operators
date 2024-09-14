import math

# Constants
solution = [2.1176, -7.2032, -5.60033, -2.83838, 9.40210]
optimal_function = 0

def griewank(solution: list):
    summation, product_notaion = 0, 1
    for x in solution:
        summation += x**2 / 4000
        product_notaion *= math.cos(x / math.sqrt((solution.index(x)+1)))
        
    return summation - product_notaion + 1

print(griewank(solution))
    

    
     