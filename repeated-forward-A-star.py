import numpy as np
from State import State
from MinStateHeap import MinStateHeap


def generateStates():
    txt_path = 'arrs/backTrackerMazes/01.txt'  # path maze data file
    f = open(txt_path)  # open file
    data_lists = f.readlines()  # read file data
    dataset = []

    # convert data in file to list
    for data in data_lists:
        data1 = data.strip('\n')
        data2 = data1.split(' ')
        dataset.append(data2)
    # convert list to states list and return
    return [[State(x, y, int(dataset[x][y])) for y in range(len(dataset[0]))] for x in range(len(dataset))]


# heuristic function (Manhattan distance)
def heuristic(s1: State, s2: State):
    return abs(s1.location[0] - s2.location[0]) + abs(s1.location[1] - s2.location[1])


# generate a list of possible actions for current state
# 1: right; 2: left; 3: up; 4: down
def generateActionList(state: State):
    possibleActions = []
    print("State location: %s" % state.location)
    x = state.location[0]
    y = state.location[1]

    #   Check possible actions
    #   Check right
    if x + 1 <= len(states) - 1:
        if states[x + 1][y].isBlocked == 0:
            possibleActions.append(1)
        else:
            print("\tState [%d %d] is blocked: states[%d][%d].isBlocked = %d" % (
                x + 1, y, x + 1, y, states[x + 1][y].isBlocked))
    #   Check left
    if x - 1 >= 0:
        if states[x - 1][y].isBlocked == 0:
            possibleActions.append(2)
        else:
            print("\tState [%d %d] is blocked: states[%d][%d].isBlocked = %d" % (
                x - 1, y, x - 1, y, states[x - 1][y].isBlocked))
    #   Check up
    if y + 1 <= len(states) - 1:
        if states[x][y + 1].isBlocked == 0:
            possibleActions.append(3)
        else:
            print("\tState [%d %d] is blocked: states[%d][%d].isBlocked = %d" % (
                x, y + 1, x, y + 1, states[x][y + 1].isBlocked))
    #   Check down
    if y - 1 >= 0:
        if states[x][y - 1].isBlocked == 0:
            possibleActions.append(4)
        else:
            print("\tState [%d %d] is blocked: states[%d][%d].isBlocked = %d" % (
                x, y - 1, x, y - 1, states[x][y - 1].isBlocked))
    print("\tPossible action: %s" % possibleActions)

    return possibleActions


# return a state after moving to a direction
def stateAfterMoving(state, action):
    x = state.location[0]
    y = state.location[1]
    # right
    if action == 1:
        return states[x + 1][y]
    # left
    elif action == 2:
        return states[x - 1][y]
    # up
    elif action == 3:
        return states[x][y + 1]
    # down
    elif action == 4:
        return states[x][y - 1]
    else:
        return None


# A* algorithm
def ComputePath():
    while goalState.gValue > openHeap.peek().fValue:
        # print(openHeap.toString())
        minState = openHeap.pop()  # Remove a state s with the smallest f-value g(s) + h(s) from openHeap
        # print(openHeap.toString())
        closedHeap.push(minState)
        actionList = generateActionList(minState)  # Generate action list for the state
        for action in actionList:
            searchedState = stateAfterMoving(minState, action)  # Get the state after taking a specific action
            # x = searchedState.location[0]
            # y = searchedState.location[1]
            # print(states[x][y].gValue)
            if searchedState.searchValue < counter:
                searchedState.gValue = 999
                searchedState.searchValue = counter
            if searchedState.gValue > minState.gValue + 1:
                searchedState.gValue = minState.gValue + 1
                searchedState.treePointer = minState

                # print("openHeap: %s" % openHeap.toString())  # print openHeap

                if openHeap.contains(searchedState):
                    print("openHeap contains %d: %s" % (searchedState.fValue, searchedState.location))
                    # To do
                    # remove it from OPEN

                # insert succ(s, a) into OPEN with f-value g(succ(s, a)) + h(succ(s, a))
                searchedState.hValue = heuristic(searchedState, goalState)
                searchedState.updateFValue()
                # print("searchedState.gValue = %d" % searchedState.gValue)
                # print("searchedState.hValue = %d" % searchedState.hValue)
                # print("searchedState.fValue = %d" % searchedState.fValue)
                # print("searchedState.location = %s" % searchedState.location)
                openHeap.push(searchedState)
                # print("openHeap: %s" % openHeap.toString())  # print openHeap
                # print("")
            # print(states[x][y].gValue)
            # print(searchedState.gValue)

        exit()  # TO DO

    return 0


# main function
if __name__ == "__main__":
    counter = 0  # A star counter
    print("Initializing states...", end="")
    states = generateStates()  # initialize states
    print("done!")

    print("Randomly setting start location and goal location...", end="")
    # initialize start state and goal state randomly
    statesEdgeSize = len(states) - 1
    # print(statesEdgeSize)
    startLocation = np.random.randint(0, statesEdgeSize, 2)
    goalLocation = np.random.randint(0, statesEdgeSize, 2)
    # print(start, goal)
    # print(states[start[0]][start[1]].isBlocked)
    # print(states[goal[0]][goal[1]].isBlocked)

    while (states[startLocation[0]][startLocation[1]].isBlocked == 1) | (
            states[goalLocation[0]][goalLocation[1]].isBlocked == 1) | all(startLocation == goalLocation):
        startLocation = np.random.randint(0, statesEdgeSize, 2)
        goalLocation = np.random.randint(0, statesEdgeSize, 2)
        # print(start, goal)
        # print(states[start[0]][start[1]].isBlocked)
        # print(states[goal[0]][goal[1]].isBlocked)
    print("done!")
    startState = states[startLocation[0]][startLocation[1]]
    goalState = states[goalLocation[0]][goalLocation[1]]
    print("Start location: %s" % startState.location)
    print("Goal location: %s" % goalState.location)

    while startState != goalState:
        counter += 1

        startState.gValue = 0  # record cost to start state, which is 0
        startState.searchValue = counter  #
        goalState.gValue = 999  # record cost to goal state, which uses 999 as infinity
        goalState.searchValue = counter  #

        # initialize open heap and closed heap
        openHeap = MinStateHeap()
        closedHeap = MinStateHeap()

        # calculate h and f value
        startState.hValue = heuristic(startState, goalState)
        startState.updateFValue()
        # print("State f Value: %d" % startState.fValue)

        openHeap.push(startState)  # insert start state into open heap

        ComputePath()  # run A*

        # if open heap is empty, report that can't reach the target
        if openHeap.size() == 0:
            print("I cannot reach the target.")
            exit()

        exit()  # temporary exit
