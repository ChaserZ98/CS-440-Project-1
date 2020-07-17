import repeatedForwardAStar as forwardAStar
import repeatedBackwardAStar as backwardAStar
import repeatedAdaptiveAStar as adaptiveAStar
import commonFunctions
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from gridWorldGenerator import generateGridWorld


# Visualize the path of the agent
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
                data_set[row_index][column_index] = 20  # Set the blocked cell to the darkest color

    plt.ion()   # Turn pyplot interactive mode on
    plt.figure(figsize=(8, 8))  # Initialize figure
    plt.title(AStarType, family="Comic Sans MS")    # Set title of the figure
    img_artist = plt.imshow(data_set, cmap=plt.cm.binary, vmin=0, vmax=20, interpolation='nearest', extent=(0, len(data_set), 0, len(data_set)))    # Initialize drawer
    plt.text(startLocation[1] + 0.1, len(data_set) - 0.9 - startLocation[0], 'S', fontdict={'size': 432/len(data_set), 'color': 'red'})     # Label start location
    plt.text(goalLocation[1] + 0.1, len(data_set) - 0.9 - goalLocation[0], 'G', fontdict={'size': 432/len(data_set), 'color': 'red'})       # Label goal location
    for index in range(len(agentPath)):
        if data_set[agentPath[index][0]][agentPath[index][1]] == 0:
            data_set[agentPath[index][0]][agentPath[index][1]] = 10
        else:
            # Deepen the color of the cells that have been passed
            data_set[agentPath[index][0]][agentPath[index][1]] += 1

        img_artist.set_data(data_set)   # Update the figure
        # plt.xticks([]), plt.yticks([])

        # plt.draw()
        plt.pause(0.01)     # Pause between each painting

    # Generate the optimal path
    i = 0
    while i < len(agentPath) - 1:
        location = agentPath[i]
        hasDuplicate = False
        for j in range(i + 1, len(agentPath)):
            if all(location == agentPath[j]):
                hasDuplicate = True
                del(agentPath[i + 1: j + 1])
                break
        if not hasDuplicate:
            i += 1
    # Erase all the path
    for row_index in range(len(data_set)):
        for column_index in range(len(data_set)):
            # Reset the color of all the unblocked cells
            if (data_set[row_index][column_index] > 0) & (data_set[row_index][column_index] < 20):
                data_set[row_index][column_index] = 0

    # Show the optimal path
    for index in range(len(agentPath)):
        data_set[agentPath[index][0]][agentPath[index][1]] = 10

    img_artist.set_data(data_set)   # Update the figure

    plt.text(3/8 * len(states), -len(states)/15, "Finished!", family="Comic Sans MS", fontdict={'size': 12})   # Notice that current drawing is finished
    plt.text(2/8 * len(states), -len(states)/10, "Total steps in optimal path: %d" % (len(agentPath) - 1), family="Comic Sans MS", fontdict={'size': 12})
    plt.ioff()  # Turn pyplot interactive mode off
    plt.show()
    # plt.savefig("pics/result/" + AStarType + "/step%d.png" % index)   # Save figure
    # np.savetxt("arrs/result/" + AStarType + "/step%d.txt" % index, data_set, fmt='%d')    # Save path as txt


if __name__ == '__main__':

    # mazeType = "backTrackerMazes"
    mazeType = "randGrid"   # Selected Maze Type
    mazeNum = 1     # Number of generated mazes
    mazeSize = 101   # The height and width of maze

    print("Checking grid world...", end="")
    if not os.path.exists("arrs/%s/00.txt" % mazeType):
        print("\033[1;33mDoes not detect grid world.\033[0m")
        print("Generating grid world...", end="")
        generateGridWorld(mazeNum, mazeSize)
        print("\033[1;32mDone!\033[0m")
    else:
        print("\033[1;32mGrid world detected!\033[0m")
        # Checking whether the existing maze satisfies the size requirement
        dataset = np.loadtxt('arrs/%s/00.txt' % mazeType, dtype=np.int32)
        print("Checking existing grid world...", end="")
        if len(dataset) != mazeSize:
            print("\033[1;33mError!\033[0m")
            print("\tError Type: \033[1;33mMaze Size Unmatched\033[0m")
            print("\tExpected maze size: \033[1;33m%d\033[0m" % mazeSize)
            print("\tExisting maze size: \033[1;33m%d\033[0m" % len(dataset))
            print("Regenerating the maze with correct size...", end="")
            generateGridWorld(mazeNum, mazeSize)
            print("\033[1;32mDone!\033[0m")
        else:
            print("\033[1;32mClear!\033[0m")

    # Initialize states from grid world
    print("Initializing states...", end="")
    states = commonFunctions.generateStates(mazeType)
    print("\033[1;32mDone!\033[0m")

    # Initialize start location and goal location
    print("Generating start location and goal location...", end="")
    startLocation = commonFunctions.generateUnblockedLocation(states)
    goalLocation = commonFunctions.generateUnblockedLocation(states)

    while (startLocation == goalLocation).all():
        goalLocation = commonFunctions.generateUnblockedLocation(states)
    print("\033[1;32mDone!\033[0m")
    print("Start Location: \033[1;32m%s\033[0m" % startLocation)
    print("Goal Location: \033[1;32m%s\033[0m" % goalLocation)
    print("")

    # Decide the type of tie breaker
    isLargerGFirst = False

    # A Star Search
    print("Repeated Forward A Star Smaller G First: ")
    agentPath = forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "Forward A Star Smaller G First")
        print("\tCosts for optimal path: %d" % (len(agentPath) - 1))
    print("")

    states = commonFunctions.generateStates(mazeType)  # Reset the states
    print("Repeated Forward A Star Bigger G First: ")
    agentPath = forwardAStar.repeatedForwardAStar(states, startLocation, goalLocation, not isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "Forward A Star Larger G First")
        print("\tCosts for optimal path: %d" % (len(agentPath) - 1))
    print("")

    states = commonFunctions.generateStates(mazeType)  # Reset the states
    print("Repeated Backward A Star: ")
    agentPath = backwardAStar.repeatedBackwardAStar(states, startLocation, goalLocation, isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "Backward A Star")
        print("\tCosts for optimal path: %d" % (len(agentPath) - 1))
    print("")

    states = commonFunctions.generateStates(mazeType)  # Reset the states
    print("Repeated Adaptive A Star: ")
    agentPath = adaptiveAStar.repeatedAdaptiveAStar(states, startLocation, goalLocation, isLargerGFirst)
    if agentPath is not False:
        visualizePath(mazeType, agentPath, "Adaptive A Star")
        print("\tCosts for optimal path: %d" % (len(agentPath) - 1))
    print("")
