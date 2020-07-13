import numpy as np
from MinStateHeap import MinStateHeap
import time
import commonFunction


# A* algorithm
def ComputePath():
    while goalState.gValue > openHeap.peek().fValue:
        # print(openHeap.toString())
        minState = openHeap.pop()  # Remove a state s with the smallest f-value g(s) + h(s) from openHeap
        # print(openHeap.toString())
        closedHeap.push(minState)
        actionList = commonFunction.generateActionList(minState, states, closedHeap)  # Generate action list for the state
        for action in actionList:
            searchedState = commonFunction.stateAfterMoving(minState, action, states)  # Get the state after taking a specific action
            if searchedState.searchValue < counter:
                searchedState.gValue = 99999
                searchedState.searchValue = counter
            if searchedState.gValue > minState.gValue + 1:
                searchedState.gValue = minState.gValue + 1  # Update the cost
                searchedState.treePointer = minState  # Build a forward link pointing to the last state

                # print("openHeap: %s" % openHeap.toString())  # print openHeap

                if openHeap.contains(searchedState):
                    # print("openHeap contains %d: %s" % (searchedState.fValue, searchedState.location))
                    openHeap.remove(searchedState)  # Remove existed state from opehHeap

                # insert succ(s, a) into OPEN with f-value g(succ(s, a)) + h(succ(s, a))
                searchedState.updateFValue()
                # print("searchedState.gValue = %d" % searchedState.gValue)
                # print("searchedState.hValue = %d" % searchedState.hValue)
                # print("searchedState.fValue = %d" % searchedState.fValue)
                # print("searchedState.location = %s" % searchedState.location)
                openHeap.push(searchedState)
                # print("openHeap: %s" % openHeap.toString())  # print openHeap
                # print("")


# main function
if __name__ == "__main__":
    counter = 0  # A star counter
    agentPath = []  # Path recorder
    timeStep = 0  # Time step counter
    numberOfExpandedCells = 0  # Number of Expanded Cells
    print("Initializing states...", end="")
    states = commonFunction.generateStates()    # initialize states
    print("done!")

    # initialize start state and goal state randomly
    print("Randomly setting start location and goal location...", end="")
    statesEdgeSize = len(states)  # Size of states list
    # print(statesEdgeSize)

    # Randomly set start location and goal location
    startLocation = np.random.randint(0, statesEdgeSize, 2)
    goalLocation = np.random.randint(0, statesEdgeSize, 2)
    # print(start, goal)
    # print(states[start[0]][start[1]].isBlocked)
    # print(states[goal[0]][goal[1]].isBlocked)

    # Check if the random start location and goal location is available
    # If not, re-generate a new random one
    while (states[startLocation[0]][startLocation[1]].actualBlockStatus == 1) | (
            states[goalLocation[0]][goalLocation[1]].actualBlockStatus == 1) | all(startLocation == goalLocation):
        startLocation = np.random.randint(0, statesEdgeSize, 2)
        goalLocation = np.random.randint(0, statesEdgeSize, 2)
        # print(start, goal)
        # print(states[start[0]][start[1]].isBlocked)
        # print(states[goal[0]][goal[1]].isBlocked)
    print("done!")

    # Respectively label the states at start location and at goal location as start state and goal state
    startState = states[startLocation[0]][startLocation[1]]
    goalState = states[goalLocation[0]][goalLocation[1]]

    commonFunction.checkNearbyBlock(startState, states)  # Check the status of nearby states

    agentPath.append(startLocation)  # Add the start location to the path
    print("Start location: %s" % startState.location)  # Print the start location
    print("Goal location: %s" % goalState.location)  # Print the goal location
    print("")

    # Compute and set heuristic value for all states
    for stateList in states:
        for state in stateList:
            state.hValue = commonFunction.heuristic(state, goalState)

    print("Starting iteration...")
    startTime = time.time()  # Record start time
    while startState != goalState:
        counter += 1

        startState.gValue = 0  # record cost for start state to reach start state, which is 0
        startState.searchValue = counter  #
        goalState.gValue = 99999  # record cost for goal state to reach start state, which uses 999 as infinity
        goalState.searchValue = counter  #

        # initialize open heap and closed heap
        openHeap = MinStateHeap()
        closedHeap = MinStateHeap()

        # calculate f value
        startState.updateFValue()
        # print("State f Value: %d" % startState.fValue)

        openHeap.push(startState)  # insert start state into open heap

        ComputePath()  # run A*

        # if open heap is empty, report that can't reach the target
        if openHeap.size() == 0:
            print("I cannot reach the target...o(╥﹏╥)o")
            exit()

        # A star search finds the start state and move start location according to the tree pointer
        # Track the tree pointers from goal state to start state
        while startState != goalState:
            timeStep += 1
            print("Time Step %d: " % timeStep)
            print("\tTree path: %s(goal)" % goalState.location, end="")
            nextState = goalState

            # Find the next state
            while (nextState.treePointer is not None) & (nextState != startState):
                if nextState.treePointer == startState:
                    break
                nextState = nextState.treePointer
                if nextState.discoveredBlockStatus == 1:
                    print("→%s(Blocked)" % nextState.location, end="")
                else:
                    print("→%s" % nextState.location, end="")
            print("→%s(agent)" % startState.location)
            if nextState.discoveredBlockStatus != 1:
                print("\tAgent Moves To: %s" % nextState.location)
                startState = nextState
                agentPath.append(startState.location)
                commonFunction.checkNearbyBlock(startState, states)
            else:
                print("\tAgent Stops: Next state %s is blocked" % nextState.location)
                break
            print("")
    endTime = time.time()  # Record end time
    print("I reached the target!╰(*°▽°*)╯")
    print("Search Statistics:")
    print("\tStart Location: %s" % startLocation)
    print("\tGoal Location: %s" % goalLocation)
    print("\tAgent Path: ", end="")
    for i in range(len(agentPath)):
        if i == 0:
            print(agentPath[0], end="")
            continue
        print("→%s" % agentPath[i], end="")
    print("\t")
    print("\tTotal Time Step: %d" % timeStep)
    print("\tActual Cost: %d" % (len(agentPath) - 1))
    print("\tTime Cost: %.10f seconds" % (endTime - startTime))
    exit()
