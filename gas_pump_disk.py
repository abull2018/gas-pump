import core

message = '\n{}, {}, {}'.format(gas_type, amount, price)
with open('log.txt', 'a') as file:
    file.write(message)


def in_the_log():
    left =[]
    with open('log.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2].replace('$', ''))])
    return left

def inside_tank():
    left = []
    with open('tank.txt', 'r') as file:
        file.readline()
        lines = file.readlines()
    for line in lines:
        split_string = line.strip().split(', ')
        left.append([split_string[0], float(split_string[1]), float(split_string[2])])
    return left

with open('tank.txt', 'w') as file:
        file.write(message)


with open('tank.txt', 'w') as file:
        file.write(message)


