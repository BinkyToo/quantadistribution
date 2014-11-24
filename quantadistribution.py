#!/usr/bin/env python2.6

import random

def draw(inputlist):                    # Draw a bar chart of the input list
    upperlimit = max(inputlist)         # Don't make the whole chart higher than necessary
    for threshold in reversed(range(0, upperlimit)):
        for entry in range(0, len(inputlist)):
            if inputlist[entry] > threshold:
                print "#",              # Draw one part of a bar
            else:
                print " ",              # Padding
        print ""                        # Move to a new line

def convertodistribution(inputlist):    # Find the frequency of each value in the input list
    output = []
    minimum = min(inputlist)            # Find top and bottom values, to avoid large empty tails...
    maximum = max(inputlist)            # ...on either side of the chart
    for value in range(minimum, maximum):
        frequency = 0
        for entry in inputlist:
            if entry == value:
                frequency += 1
        output.append(frequency)
    return output

atoms = []
totalatoms = 5000                       # How many items are the quanta distributed between?
iterations = 800000                     # How many times should the quanta be exchaged
averageenergy = 100                     # How many quanta does each item have before the first ittereation

index = 0
for index in range(0, totalatoms):
    atoms.append(averageenergy)         # Build list of atoms to work with

for itereation in range(0, iterations):
    toatom = random.randint(0, len(atoms))
    fromatom = random.randint(0, len(atoms))
    if atoms[fromatom-1] > 0:           # Can't take away energy that isn't there
        atoms[fromatom-1] -=1
        atoms[toatom-1] += 1

draw(convertodistribution(atoms))       # Print output

