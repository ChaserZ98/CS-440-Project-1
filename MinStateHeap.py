from State import State


# compare the priority of two states by a specific sign
def comparePriority(s1: State, sign: str, s2: State, isLargerGFirst: bool):
    if isLargerGFirst is True:
        # use tie breaker that prioritize the state with larger G value
        if sign == "==":
            return priorityWithLargerG(s1) == priorityWithLargerG(s2)
        elif sign == ">":
            return priorityWithLargerG(s1) > priorityWithLargerG(s2)
        elif sign == "<":
            return priorityWithLargerG(s1) < priorityWithLargerG(s2)
        elif sign == ">=":
            return priorityWithLargerG(s1) >= priorityWithLargerG(s2)
        elif sign == "<=":
            return priorityWithLargerG(s1) <= priorityWithLargerG(s2)
    else:
        # use tie breaker that prioritize the state with smaller G value
        if sign == "==":
            return priorityWithSmallerG(s1) == priorityWithSmallerG(s2)
        elif sign == ">":
            return priorityWithSmallerG(s1) > priorityWithSmallerG(s2)
        elif sign == "<":
            return priorityWithSmallerG(s1) < priorityWithSmallerG(s2)
        elif sign == ">=":
            return priorityWithSmallerG(s1) >= priorityWithSmallerG(s2)
        elif sign == "<=":
            return priorityWithSmallerG(s1) <= priorityWithSmallerG(s2)


# Tie breaker that prioritizes state with larger g value
def priorityWithLargerG(s: State):
    return 999 * s.fValue - s.gValue


# Tie breaker that prioritizes state with smaller g value
def priorityWithSmallerG(s: State):
    return 999 * s.fValue + s.gValue


class MinStateHeap(object):
    def __init__(self, isLargerGFirst: bool):
        self.data = []  # heap list
        self.count = len(self.data)  # number of elements
        self.isLargerGFirst = isLargerGFirst

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def push(self, item):
        # insert item into heap
        self.data.append(item)
        self.count += 1
        self.shiftUp(self.count)

    def shiftUp(self, count):
        # Move state up to a proper location by priority to maintain the MinStateHeap
        while count > 1 and comparePriority(self.data[int(count / 2) - 1], ">", self.data[count - 1], self.isLargerGFirst):
            self.data[int(count / 2) - 1], self.data[count - 1] = self.data[count - 1], self.data[int(count / 2) - 1]
            count = int(count / 2)

    def peek(self):
        # Get the state with highest priority
        return self.data[0]

    def pop(self):
        # Pop the state with highest priority
        if self.count > 0:
            ret = self.data[0]
            self.data[0], self.data[self.count - 1] = self.data[self.count - 1], self.data[0]
            self.data.pop()
            self.count -= 1
            self.shiftDown(1)
            return ret

    def remove(self, state):
        # remove a specific state from heap
        if self.data.index(state) == 0:
            self.pop()
            return True
        else:
            if self.count > 0:
                while state in self.data:
                    stateIndex = self.data.index(state)
                    self.data[stateIndex], self.data[self.count - 1] = self.data[self.count - 1], self.data[stateIndex]
                    # print(self.toString())
                    del (self.data[self.count - 1])
                    # print(self.toString())
                    self.count -= 1
                    # print(self.toString())
                    self.shiftDown(stateIndex + 1)
            else:
                return False

    def shiftDown(self, count):
        # Move state down to a proper location by priority to maintain the MinStateHeap
        while 2 * count <= self.count:
            # browse children
            j = 2 * count
            # print(self.toString())
            if j + 1 <= self.count:
                # browse right child
                # print(priorityWithSmallerG(self.data[j]))
                # print(priorityWithSmallerG(self.data[j - 1]))
                # print(self.toString())
                if comparePriority(self.data[j], "<", self.data[j - 1], self.isLargerGFirst):
                    j += 1
            # print(priorityWithSmallerG(self.data[j]))
            # print(priorityWithSmallerG(self.data[j - 1]))
            # print(self.toString())
            if comparePriority(self.data[count - 1], "<=", self.data[j - 1], self.isLargerGFirst):
                # if smaller than children, then break
                break
            self.data[count - 1], self.data[j - 1] = self.data[j - 1], self.data[count - 1]
            count = j
            # print(self.toString())

    def toString(self):
        result = "["
        for i in range(len(self.data)):
            result += ("%d: %s" % (priorityWithSmallerG(self.data[i]), self.data[i].location))
            if i != len(self.data) - 1:
                result += ", "
        result += "]"
        return result

    def contains(self, s: State):
        if s in self.data:
            return True
        else:
            return False
