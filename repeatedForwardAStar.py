from MinStateHeap import MinStateHeap
import time
import commonFunctions


# Forward A* algorithm
def ComputePath(openHeap, closedHeap, goalState, expandedStates, counter, states):
    while goalState.gValue > openHeap.peek().fValue:
        # print(openHeap.toString())
        minState = openHeap.pop()  # Remove a state s with the smallest f-value g(s) + h(s) from openHeap
        expandedStates.append(minState.location)
        # print(openHeap.toString())
        closedHeap.push(minState)
        actionList = commonFunctions.generateActionList(minState, states, closedHeap)  # Generate action list for the state
        for action in actionList:
            searchedState = commonFunctions.stateAfterMoving(minState, action, states)  # Get the state after taking a specific action
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
        if openHeap.isEmpty():
            break


# main function
def repeatedForwardAStar(states, startLocation, goalLocation, isLargerGFirst: bool):
    counter = 0  # A star counter
    agentPath = []  # Path recorder
    timeStep = 0  # Time step counter
    expandedStates = []  # Expanded states during the whole repeated A star search

    # Respectively label the states at start location and at goal location as start state and goal state
    startState = states[startLocation[0]][startLocation[1]]
    goalState = states[goalLocation[0]][goalLocation[1]]

    commonFunctions.checkNearbyBlock(startState, states)  # Check the status of nearby states

    agentPath.append(startLocation)  # Add the start location to the path
    # print("Start location: %s" % startState.location)  # Print the start location
    # print("Goal location: %s" % goalState.location)  # Print the goal location
    # print("")

    # Compute and set heuristic value for all states
    for stateList in states:
        for state in stateList:
            state.hValue = commonFunctions.heuristic(state, goalState)

    print("Iterating...")
    startTime = time.time()  # Record start time
    while startState != goalState:
        counter += 1

        startState.gValue = 0  # record cost for start state to reach start state, which is 0
        startState.searchValue = counter  #
        goalState.gValue = 99999  # record cost for goal state to reach start state, which uses 999 as infinity
        goalState.searchValue = counter  #

        # initialize open heap and closed heap
        openHeap = MinStateHeap(isLargerGFirst)
        closedHeap = MinStateHeap(isLargerGFirst)

        # calculate f value
        startState.updateFValue()
        # print("State f Value: %d" % startState.fValue)

        openHeap.push(startState)  # insert start state into open heap

        ComputePath(openHeap, closedHeap, goalState, expandedStates, counter, states)  # Run forwardA*

        # if open heap is empty, report that can't reach the target
        if openHeap.size() == 0:
            print("I cannot reach the target...o(╥﹏╥)o")
            return False

        # A star search finds the start state and move start location according to the tree pointer
        # Track the tree pointers from goal state to start state
        while startState != goalState:
            timeStep += 1
            # print("Time Step %d: " % timeStep)
            # print("\tTree path: %s(goal)" % goalState.location, end="")
            nextState = goalState

            # Find the next state
            while (nextState.treePointer is not None) & (nextState != startState):
                if nextState.treePointer == startState:
                    break
                nextState = nextState.treePointer
                # if nextState.discoveredBlockStatus == 1:
                #     print("→%s(Blocked)" % nextState.location, end="")
                # else:
                #     print("→%s" % nextState.location, end="")
            # print("→%s(agent)" % startState.location)
            if nextState.discoveredBlockStatus != 1:
                # print("\tAgent Moves To: %s" % nextState.location)
                startState = nextState
                agentPath.append(startState.location)
                commonFunctions.checkNearbyBlock(startState, states)
            else:
                # print("\tAgent Stops: Next state %s is blocked" % nextState.location)
                break
            # print("")
    expandedStates.append(goalState.location)
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
    print("")
    print("\tTotal Time Step: %d" % timeStep)
    print("\tActual Cost: %d" % (len(agentPath) - 1))
    print("\tNumber of A Star Iterations: %d " % counter)
    print("\tTime Cost: %.10f seconds" % (endTime - startTime))
    # print("\tExpanded Cells: ", end="")
    # for i in range(len(expandedStates)):
    #     if i == 0:
    #         print(expandedStates[0], end="")
    #         continue
    #     print(",%s" % expandedStates[i], end="")
    # print("")
    print("\tNumber of Expanded Cells: %d" % len(expandedStates))
    print("")
    return agentPath
