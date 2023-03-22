from Space import *
from Constants import *
import time
import math


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
        if father[i] == -1:
            break

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
        elif curr.value in closed_set:
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
    open_set: list[int] = [g.start.value]
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
            if child.value not in closed_set and child.value not in open_set:
                open_set.append(child.value)
                set_color(sc, child, red)
                father[child.value] = curr.value
                
    reconstruct_path(g, sc, father)


def get_min_node(open_set: dict[int]):
    min = 100_000
    min_node = -1
    for i, v in open_set.items():
        if v < min:
            min = v
            min_node = i
    return min_node


def get_distance(curr: Node, goal: Node):
    return math.sqrt((curr.x - goal.x)**2 + (curr.y - goal.y)**2)


def UCS(g: Graph, sc: pygame.Surface):
    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    while len(open_set):
        min_node = get_min_node(open_set)
        curr = g.grid_cells[min_node]
        del open_set[min_node]
        set_color(sc, curr, yellow)

        if g.is_goal(curr):
            break
        elif curr.value in closed_set:
            continue
        else:
            closed_set.append(curr.value)
            set_color(sc, curr, blue)

        for child in g.get_neighbors(curr):
            if child.value not in closed_set and child.value not in open_set.keys():
                cost[child.value] = cost[curr.value] + get_distance(curr, child)
                open_set[child.value] = cost[child.value]
                set_color(sc, child, red)
                father[child.value] = curr.value
            elif child.value in open_set.keys() and cost[child.value] < open_set[child.value]:
                open_set[child.value] = cost[child.value]

    reconstruct_path(g, sc, father)


def mahattan_heurisitc(curr: Node, goal: Node):
    return abs(curr.x - goal.x) + abs(curr.y - goal.y)


def euclidean_heuristic(curr: Node, goal: Node):
    return math.sqrt((curr.x - goal.x)**2 + (curr.y - goal.y)**2)


def AStar(g: Graph, sc: pygame.Surface):

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    while len(open_set):
        min_node = get_min_node(open_set)
        curr = g.grid_cells[min_node]
        del open_set[min_node]
        set_color(sc, curr, yellow)

        if g.is_goal(curr):
            break

        if curr.value in closed_set:
            continue
        else:
            closed_set.append(curr.value)
            set_color(sc, curr, blue)

        for child in g.get_neighbors(curr):
            new_cost = cost[curr.value] + get_distance(curr, child)
            if new_cost < cost[child.value]:
                father[child.value] = curr.value
                cost[child.value] = new_cost
                f = cost[child.value] + mahattan_heurisitc(child, g.goal)
                if child.value not in open_set.keys():
                    open_set[child.value] = f
                    set_color(sc, child, red)

    reconstruct_path(g, sc, father)
