import numpy as np


class State:
    def __init__(self, x, y, isBlocked):
        self.location = np.array([x, y])
        self.isBlocked = isBlocked
        self.searchValue = 0
        self.gValue = 0
        self.hValue = 0
        self.fValue = self.gValue + self.hValue
        self.treePointer = None

    def updateFValue(self):
        self.fValue = self.gValue + self.hValue

