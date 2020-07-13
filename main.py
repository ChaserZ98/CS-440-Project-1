import repeatedForwardAStar as forwardAStar
import repeatedBackwardAStar as backwardAStar
import repeatedAdaptiveAStar as adaptiveAStar
import commonFunctions

if __name__ == '__main__':

    # Initialize states from grid world
    print("Initializing states...", end="")
    states = commonFunctions.generateStates()
    print("done!")

    # Initialize start location and goal location
    print("Generating start location and goal location...", end="")
    startLocation = commonFunctions.generateUnblockedLocation(states)
    goalLocation = commonFunctions.generateUnblockedLocation(states)
    while (startLocation == goalLocation).all():
        goalLocation = commonFunctions.generateUnblockedLocation(states)
    print("done!")

    # Decide the type of tie breaker
    isLargerGFirst = False

    # A Star Search
    print("Repeated Forward A Star: ")
    forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, isLargerGFirst)

    states = commonFunctions.generateStates()   # Reset the states
    print("Repeated Backward A Star: ")
    backwardAStar.repeatedBackwardAStar(states, startLocation, goalLocation, isLargerGFirst)

    states = commonFunctions.generateStates()   # Reset the states
    print("Repeated Adaptive A Star: ")
    adaptiveAStar.repeatedAdaptiveAStar(states, startLocation, goalLocation, isLargerGFirst)
