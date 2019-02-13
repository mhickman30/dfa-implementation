# Author: Matt Hickman
# Program: Programming Assignment 1: Implement a DFA
# Due Date: Tuesday, February 12, 2019 at 11:59 PM

# Import the system library
import sys

# Check to make sure that there is at least one
if len(sys.argv) > 1:
    # Open the file
    file_object = open(sys.argv[1], "r")
    # Extract the data for number of states
    numStates =  int(file_object.readline())
    # Extract the data for alphabet
    alphabet = file_object.readline()
    # Make the alphabet into a list
    alphabetList = list(alphabet)

    # Initialize an empty dictionary for all the transition matrix
    transitions = dict()

    # Iterate through the transitions
    for i in range(numStates * (len(alphabetList) - 1)):
            # Get current transition line
            transitionLine = file_object.readline()
            # Split string by white space
            transitionLineSplit = transitionLine.split()
            # Add each entry of the transitionline to the transition dictionary with proper formatiing
            transitions[(int(transitionLineSplit[0]), transitionLineSplit[1].strip('\''))] = int(transitionLineSplit[2])

    # Set start state to an int
    startState = int(file_object.readline())

    # Set accept states to a list of ints
    acceptStates = file_object.readline()
    acceptStatesList = list(acceptStates)
    filteredAcceptStatesList = acceptStates.split()

    # Create empty test case array
    testCases = []
    # Iterate through the remaining lines of the file object and add them to the test case array
    i = 1
    for line in file_object:
        testCases.append(line)
        i+= 1

    # Initailze counter and start to iterate through each test case, checking to see if
    # the end state matches an accept state and printing result
    counter = 0
    for case in testCases:
        # Initialize the current case as the test case that the counter is on
        currentCase = testCases[counter]
        # Initialize a list of all the characters to be inputed for this test case
        caseInputs = list(currentCase)
        # Iterate through each input of test case and move to next state
        currentState = startState # make sure to always start at the start state
        for i in range(len(caseInputs) - 1):
                currentState = transitions.get((currentState, caseInputs[i]))

        # Set final state equal to the last current state
        finalState = currentState

        # Initialize an accept variable
        accept = 0
        # Iterate through all accept states and see if they match the final state
        for i in range(len(filteredAcceptStatesList)):
            if finalState == int(filteredAcceptStatesList[i]):
                # If it matches set the accept flag to 1
                accept = 1

        # If the accept flag was triggered then print accept if not then print reject
        if accept == 1:
            print("Accept")
            counter += 1
        else:
            print("Reject")
            counter += 1

    # Close file
    file_object.close()
