#file io 
#TODO add configurations to parameters
fileName = "fsa.txt"
class FmaData:
    def __init__(self, amountOfStates, alphabet, stateTransisitions, startState, acceptStates):
        self.amountOfStates = amountOfStates.strip()
        self.alphabet = alphabet.strip()
        self.stateTransisitions = stateTransisitions.strip()
        self.startState = startState.strip()
        self.acceptStates = acceptStates.strip()
    
    def getAmountOfStates(self):
        return self.amountOfStates

    def getAlphabet(self):
        alphaList = self.alphabet.split(',')
        return alphaList
    
    def getStateTransitions(self):
        transitionsList = self.stateTransisitions.split(',')
        return transitionsList

    def getStartState(self):
        return self.startState

    def getAcceptState(self):
        acceptStateList = self.acceptStates.split(',')
        return acceptStateList
#Parses the files 
class Parser:
    def __init__(self, fileName):
        self.fileName = fileName

    def parseData(self):
        currentFile = open(self.fileName,"r+")
        data = currentFile.readline()

        parserList = data.split(';')
        return parserList

#Parse the data and create the different transitions states with thier connected pathways 
parser = Parser(fileName)
parserList = parser.parseData() 

fmaData = FmaData(parserList[0], parserList[1], parserList[2], parserList[3],  parserList[4])

#The transitions that are attached to the different states 
class Transition:
    def __init__(self, transition):
        self.transition = transition
        holder = []
        for i in transition: 
            if i.isalpha() or i.isdigit():
                holder.append(i)
            
        self.start = holder[0]
        self.finish = holder[1]
        self.key = holder[2]

    def getStart(self):
        return self.start
    def getFinish(self):
        return self.finish
    def getKey(self):
        return self.key
#The different states for the given inputs 
class State: 
    def __init__(self, stateID):
        self.state = stateID
        self.transitions = []
    def getState(self):
        return self.state
    def placeTransition(self, transition):
        start = transition.getStart()
        if int(start) == self.state:
            self.transitions.append(transition)
    def getTransitions(self):
        return self.transitions
    def setCoordinates(self, x1, x2, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def getCoordinates(self):
        self.coordinates = [self.x1, self.y1, self.x2, self.y2]
        return self.coordinates
    def setID(self, ID):
        self.ID = ID
    def getID(self):
        return self.ID
    
        



#takes in all the transitions from the txt and returns a list of those transitions data types for extraction later by the function when the State classes are set up
def createTransitions(transitionsList):
    holder =[]
    for transition in transitionsList:
        data = Transition(transition)
        holder.append(data)
    return holder

def createStatesList(amountOfStates):
    stateList =[]
    i =0
    while (i < int(amountOfStates)):
        state = State(i)
        stateList.append(state)
        i+=1    
    return stateList


def placingData(transitionsList, stateList):
    for state in stateList:
        for transition in transitionsList:
            state.placeTransition(transition)
    return stateList



transitionsList = createTransitions(fmaData.getStateTransitions())
stateList = createStatesList(fmaData.getAmountOfStates())
stateList = placingData(transitionsList, stateList)

def generateLispCode():
    return 