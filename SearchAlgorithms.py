from Space import *
from Constants import *

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')


def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
