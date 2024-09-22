import griewank

solution = [2.1176, -7.2032, -5.60033, -2.83838, 9.40210]
optimal_function = 0.0


print(griewank.griewank(solution))
print(griewank.strength(solution, optimal_function))