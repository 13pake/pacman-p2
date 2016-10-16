# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# from eightpuzzle import path


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    """for i in range(len(successors)):
        location_state = successors[i][0]
        action = successors[i][1]
        action_cost = successors[i][2]
        print"Child ", i, " :\n "
        print"\tstate: ", location_state
        print "\taction: ", action
        print "\taction cost: ", action_cost"""
        #Child: coordinate, history, path_cost
        # (state, history, path_cost)
        # Project 1: ((x,y), hist, pc)
        # Project 2: (?, hist, pc)
    
    stack = util.Stack()
    start = problem.getStartState()
    visited = []
    visited.append(start)
#     path = []
    stack.push((start, [], 0))
    
    while not stack.isEmpty():
        (node, path, cost) = stack.pop()
        successors = problem.getSuccessors(node)
        for i in range(len(successors)):
            if not visited.__contains__(successors[i][0]):
                if problem.isGoalState(successors[i][0]):
                    return path + [successors[i][1]]
                else:
                    stack.push((successors[i][0], path + [successors[i][1]], cost + successors[i][2]))
                    visited.append(node)
    return []


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    start = problem.getStartState()
    visited = []
    visited.append(start)
    queue.push((start, [], 0))
     
    while not queue.isEmpty():
        (node, path, cost) = queue.pop()
        for successor, action, stepCost in problem.getSuccessors(node):
            if not visited.__contains__(successor):
                if problem.isGoalState(successor):
                    return path + [action]
                else:
                    queue.push((successor, path + [action], cost + stepCost))
                    visited.append(node)
    return []
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    p_queue = util.PriorityQueue()
    start = problem.getStartState()
    visited = []
    visited.append(start)
    p_queue.push((start, []), 0)
    
    while not p_queue.isEmpty():
        node, path = p_queue.pop()
        for successor, action, stepCost in problem.getSuccessors(node):
            
            if not visited.__contains__(successor):
                new_path = path + [action]
                
                if problem.isGoalState(successor):
                    return new_path
                else:
                    p_queue.push((successor, new_path), problem.getCostOfActions(new_path))
                    visited.append(node)
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = []
    p_queue = util.PriorityQueue()
    start = problem.getStartState()
      
    g = 0
    h = heuristic(start, problem)
    f = g + h
     
    p_queue.push((start, [], g), f)
      
    while not p_queue.isEmpty():
         current, path, g = p_queue.pop()
         if problem.isGoalState(current):
             return path
         if current not in visited:
             visited.append(current)
             for successor, action, next_cost in problem.getSuccessors(current):
                 if successor not in visited:
                     g = g + next_cost
                     h = heuristic(successor, problem)
                     f = g + h
                     p_queue.push((successor, path + [action], g), f)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
