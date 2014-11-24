#!/usr/bin/env python2.6

import random

def draw(inputlist):
    upperlimit = max(inputlist)
    for threshold in reversed(range(0, upperlimit)):
        for entry in range(0, len(inputlist)):
            if inputlist[entry] > threshold:
                print "#",
            else:
                print " ",
        print ""        #newline

def convertodistribution(inputlist):
    output = []
    minimum = min(inputlist)
    maximum = max(inputlist)
    for value in range(minimum, maximum):
        frequency = 0
        for entry in inputlist:
            if entry == value:
                frequency += 1
        output.append(frequency)
    return output

atoms = []
totalatoms = 5000
iterations = 800000
averageenergy = 100

toatom = 0
fromatom = 0

index = 0
for index in range(0, totalatoms):
    atoms.append(averageenergy)

iteration = 0
for itereation in range(0, iterations):
    toatom = random.randint(0, len(atoms))
    fromatom = random.randint(0, len(atoms))
    if atoms[fromatom-1] > 0:
        atoms[fromatom-1] -=1
        atoms[toatom-1] += 1

draw(convertodistribution(atoms))

