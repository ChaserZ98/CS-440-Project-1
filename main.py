import repeatedForwardAStar as forwardAStar
import repeatedBackwardAStar as backwardAStar
import repeatedAdaptiveAStar as adaptiveAStar
import commonFunctions
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
import time


def visualizePath(agentPath, AStarType):
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

    data_set = np.loadtxt('arrs/backTrackerMazes/01.txt', dtype=np.int32)
    for row_index in range(len(data_set)):
        for column_index in range(len(data_set)):
            if data_set[row_index][column_index] == 1:
                data_set[row_index][column_index] = 20

    plt.ion()
    plt.figure()
    img_artist = plt.imshow(data_set, cmap=plt.cm.binary, interpolation='nearest', extent=(0, 100, 0, 100))
    for index in range(len(agentPath)):
        if data_set[agentPath[index][0]][agentPath[index][1]] == 0:
            data_set[agentPath[index][0]][agentPath[index][1]] = 10
        else:
            data_set[agentPath[index][0]][agentPath[index][1]] += 1

        img_artist.set_data(data_set)
        plt.xticks([]), plt.yticks([])

        plt.draw()
        plt.pause(0.001)
    plt.title("Finished!")
    plt.ioff()
    plt.show()
    # plt.savefig("pics/result/" + AStarType + "/step%d.png" % index)
    # np.savetxt("arrs/result/" + AStarType + "/step%d.txt" % index, data_set, fmt='%d')


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
    agentPath = forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    visualizePath(agentPath, "forwardAStar")
    # print(agentPath)

    states = commonFunctions.generateStates()  # Reset the states
    print("Repeated Backward A Star: ")
    agentPath = backwardAStar.repeatedBackwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    visualizePath(agentPath, "backwardAStar")
    #
    states = commonFunctions.generateStates()  # Reset the states
    print("Repeated Adaptive A Star: ")
    agentPath = adaptiveAStar.repeatedAdaptiveAStar(states, startLocation, goalLocation, isLargerGFirst)
    visualizePath(agentPath, "adaptiveAStar")
