import repeatedForwardAStar as forwardAStar
import repeatedBackwardAStar as backwardAStar
import repeatedAdaptiveAStar as adaptiveAStar
import commonFunctions
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import time


def visualizePath(mazeType: str, agentPath, AStarType):
    if not os.path.exists("pics/result"):
        os.mkdir("pics/result")
    if not os.path.exists("arrs/result"):
        os.mkdir("arrs/result")
    if os.path.exists("pics/result/" + AStarType):
        shutil.rmtree("pics/result/" + AStarType)
    if os.path.exists("arrs/result/" + AStarType):
        shutil.rmtree("arrs/result/" + AStarType)
    os.mkdir("pics/result/" + AStarType)
    os.mkdir("arrs/result/" + AStarType)

    data_set = np.loadtxt('arrs/%s/00.txt' % mazeType, dtype=np.int32)
    for row_index in range(len(data_set)):
        for column_index in range(len(data_set)):
            if data_set[row_index][column_index] == 1:
                data_set[row_index][column_index] = 20

    plt.ion()
    plt.figure(figsize=(8, 8))
    plt.title(AStarType, family="Comic Sans MS")
    img_artist = plt.imshow(data_set, cmap=plt.cm.binary, vmin=0, vmax=20, interpolation='nearest', extent=(0, len(data_set), 0, len(data_set)))
    plt.text(startLocation[1] + 0.1, len(data_set) - 0.9 - startLocation[0], 'S', fontdict={'size': 432/len(data_set), 'color': 'red'})
    plt.text(goalLocation[1] + 0.1, len(data_set) - 0.9 - goalLocation[0], 'G', fontdict={'size': 432/len(data_set), 'color': 'red'})
    for index in range(len(agentPath)):
        if data_set[agentPath[index][0]][agentPath[index][1]] == 0:
            data_set[agentPath[index][0]][agentPath[index][1]] = 10
        else:
            data_set[agentPath[index][0]][agentPath[index][1]] += 1

        img_artist.set_data(data_set)
        plt.xticks([]), plt.yticks([])

        # plt.draw()
        plt.pause(0.01)
    plt.text(42, -5, "Finished!", family="Comic Sans MS")
    plt.ioff()
    plt.show()
    # plt.savefig("pics/result/" + AStarType + "/step%d.png" % index)
    # np.savetxt("arrs/result/" + AStarType + "/step%d.txt" % index, data_set, fmt='%d')


if __name__ == '__main__':

    # mazeType = "backTrackerMazes"
    mazeType = "randGrid"

    # Initialize states from grid world
    print("Initializing states...", end="")
    states = commonFunctions.generateStates(mazeType)
    print("done!")

    # Initialize start location and goal location
    print("Generating start location and goal location...", end="")
    startLocation = commonFunctions.generateUnblockedLocation(states)
    goalLocation = commonFunctions.generateUnblockedLocation(states)
    while (startLocation == goalLocation).all():
        goalLocation = commonFunctions.generateUnblockedLocation(states)
    print("done!")
    print("Start Location: %s" % startLocation)
    print("Goal Location: %s" % goalLocation)
    print("")

    # Decide the type of tie breaker
    isLargerGFirst = False

    # A Star Search
    print("Repeated Forward A Star Smaller G First: ")
    agentPath = forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "adaptiveAStar")

    states = commonFunctions.generateStates(mazeType)  # Reset the states
    print("Repeated Forward A Star Bigger G First: ")
    agentPath = forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, not isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "adaptiveAStar")

    states = commonFunctions.generateStates(mazeType)  # Reset the states
    print("Repeated Backward A Star: ")
    agentPath = backwardAStar.repeatedBackwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "adaptiveAStar")

    states = commonFunctions.generateStates(mazeType)  # Reset the states
    print("Repeated Adaptive A Star: ")
    agentPath = adaptiveAStar.repeatedAdaptiveAStar(states, startLocation, goalLocation, isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "adaptiveAStar")
