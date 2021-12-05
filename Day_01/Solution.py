import math

modules = []
with open("Day_01/input.txt") as txt:
    for line in txt:
        modules.append(int(line))


#
# The `modules` variable is an array of integers, for example:
#
#       modules[0] = 103450
#       modules[1] = 53774
#       modules[2] = 124794
#       ...
#
# Each integer represents the mass of that module.

# >>>
# Fuel required to launch a given module is based on its mass. Specifically,
# to find the fuel required for a module, take its mass, divide by three,
# round down, and subtract 2.
#
# For example:
#
#   For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#   For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#   For a mass of 1969, the fuel required is 654.
#   For a mass of 100756, the fuel required is 33583.
#
# The Fuel Counter-Upper needs to know the total fuel requirement. To find
# it, individually calculate the fuel needed for the mass of each module
# (your puzzle input), then add together all the fuel values.
#
# What is the sum of the fuel requirements for all of the modules on your
# spacecraft?
# <<<
#

def SolvePart1(modules):
    Fuel = 0
    for module in modules:
        Fuel += math.floor(module/3)-2
    return Fuel



def computefuel(mass):
    return math.floor(mass/3)-2

def SolvePart2(modules):
    TotalFuel = 0
    for module in modules:
        Fuel = computefuel(module)
        while Fuel > 0:
            TotalFuel += Fuel
            Fuel = computefuel(Fuel)
    return TotalFuel



print("Part 1: " + str(SolvePart1(modules)))
print("Part 2: " + str(SolvePart2(modules)))