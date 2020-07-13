import repeatedForwardAStar as forwardAStar
import repeatedBackwardAStar as backwardAStar
import repeatedAdaptiveAStar as adaptiveAStar

if __name__ == '__main__':
    isLargerGFirst = False
    forwardAStar.repeatedForwardAStar(isLargerGFirst)
    backwardAStar.repeatedBackwardAStar(isLargerGFirst)
    adaptiveAStar.repeatedAdaptiveAStar(isLargerGFirst)
