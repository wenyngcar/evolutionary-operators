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