import numpy as np
from heapq import heapify, heappush, heappop
from State import State


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


# A* algorithm
def ComputePath():
    # To be done
    minState = heappop(openHeap)    # remove a state s with the smallest f-value g(s) + h(s) from openHeap
    while states[goal[0]][goal[1]].gValue > minState.fValue:
        heappush(closedHeap, minState)
        actionList = generateActionList(minState)
        for action in actionList:
            print(action)
        exit()  # TO DO
        # actionList = generateActionList(minState)

    return 0


# main function
if __name__ == "__main__":
    counter = 0  # A star counter
    states = generateStates()  # initialize states

    # initialize start state and goal state randomly
    statesEdgeSize = len(states) - 1
    # print(statesEdgeSize)
    start = np.random.randint(0, statesEdgeSize, 2)
    goal = np.random.randint(0, statesEdgeSize, 2)
    # print(start, goal)
    # print(states[start[0]][start[1]].isBlocked)
    # print(states[goal[0]][goal[1]].isBlocked)

    while (states[start[0]][start[1]].isBlocked == 1) | (states[goal[0]][goal[1]].isBlocked == 1) | all(start == goal):
        start = np.random.randint(0, statesEdgeSize, 2)
        goal = np.random.randint(0, statesEdgeSize, 2)
        # print(start, goal)
        # print(states[start[0]][start[1]].isBlocked)
        # print(states[goal[0]][goal[1]].isBlocked)
    print("Start location: %s" % start)
    print("Goal location: %s" % goal)

    while any(start != goal):
        counter += 1

        states[start[0]][start[1]].gValue = 0  # record cost to start state, which is 0
        states[start[0]][start[1]].searchValue = counter  #
        states[goal[0]][goal[1]].gValue = 999  # record cost to goal state, which uses 999 as infinity
        states[goal[0]][goal[1]].searchValue = counter  #

        # initialize open heap and closed heap
        openHeap = []
        heapify(openHeap)
        closedHeap = []
        heapify(closedHeap)

        # calculate h and f value
        states[start[0]][start[1]].hValue = heuristic(states[start[0]][start[1]], states[goal[0]][goal[1]])
        states[start[0]][start[1]].updateFValue()
        print("Start f Value: %d" % states[start[0]][start[1]].fValue)

        heappush(openHeap, states[start[0]][start[1]])  # insert start state into open heap

        ComputePath()  # run A*

        # if open heap is empty, report that can't reach the target
        if len(openHeap) == 0:
            print("I cannot reach the target.")
            exit()

        exit()  # temporary exit
