from Space import *
from Constants import *
import time

def set_color(sc: pygame.Surface, node: Node, color):
    if color == grey:
        node.set_color(color)
        node.draw(sc)
    elif node.color == orange or node.color == purple or node.color == blue:
        return
    else:
        node.set_color(color)
        node.draw(sc)
    pygame.display.flip()
    time.sleep(0.02)

def reconstruct_path(g: Graph, sc: pygame.Surface, father: list[int]):
    i = g.goal.value
    while i != -1:
        if father[i] == -1: break

        curr, parent = g.grid_cells[i], g.grid_cells[father[i]]
        curr_coordinate, parent_coordinate = (curr.x, curr.y), (parent.x, parent.y)
        
        pygame.draw.line(sc, green, curr_coordinate, parent_coordinate, 2)
        set_color(sc, curr, grey)
        i = father[i]

def DFS(g: Graph, sc: pygame.Surface):
    open_set: list[int] = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while len(open_set):
        curr = g.grid_cells[open_set.pop()]
        set_color(sc, curr, yellow)

        if g.is_goal(curr):
            break

        if curr.value in closed_set:
            continue
        else:
            closed_set.append(curr.value)
            set_color(sc, curr, blue)

        for child in g.get_neighbors(curr):
            if child.value not in closed_set:
                open_set.append(child.value)
                set_color(sc, child, red)

                father[child.value] = curr.value

    reconstruct_path(g, sc, father)


def BFS(g: Graph, sc: pygame.Surface):
    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    while len(open_set):
        curr = g.grid_cells[open_set.pop(0)]
        set_color(sc, curr, yellow)

        if g.is_goal(curr):
            break

        if curr.value in closed_set:
            continue
        else:
            closed_set.append(curr.value)
            set_color(sc, curr, blue)

        for child in g.get_neighbors(curr):
            if child.value not in closed_set:
                open_set.append(child.value)
                set_color(sc, child, red)

                father[child.value] = curr.value

    reconstruct_path(g, sc, father)


def UCS(g: Graph, sc: pygame.Surface):
    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

def AStar(g: Graph, sc: pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
