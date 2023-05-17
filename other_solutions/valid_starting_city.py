# We want to traverse the most gas-scarce portion 
# of the journey last. We can do this by starting
# in the city DIRECTLY AFTER the most scarce portion.
# This city will be the solution because we have been 
# guaranteed enough gas to complete the journey.

# Time: O(n) | Space: O(1)

def validStartingCity(distances, fuel, mpg):
    currentFuel = 0
    minFuel = float("inf")
    bestIdx = 0
    for i in range(len(distances)):
        currentFuel += (fuel[i] * mpg) - distances[i]
        if currentFuel < minFuel:
            minFuel = currentFuel
            bestIdx = (i + 1) % len(distances)
    return bestIdx