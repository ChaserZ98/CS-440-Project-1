import repeatedForwardAStar as forwardAStar
import repeatedBackwardAStar as backwardAStar
import repeatedAdaptiveAStar as adaptiveAStar
import commonFunctions

if __name__ == '__main__':
    print("Initializing states...", end="")
    states = commonFunctions.generateStates()  # initialize states
    print("done!")
    print("Generating start location and goal location...", end="")
    startLocation = commonFunctions.generateUnblockedLocation(states)
    goalLocation = commonFunctions.generateUnblockedLocation(states)
    while (startLocation == goalLocation).all():
        goalLocation = commonFunctions.generateUnblockedLocation(states)
    print("done!")
    isLargerGFirst = False
    forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    backwardAStar.repeatedBackwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    adaptiveAStar.repeatedAdaptiveAStar(states, startLocation, goalLocation, isLargerGFirst)
