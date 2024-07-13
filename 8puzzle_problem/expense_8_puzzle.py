from datetime import datetime
from collections import deque
from queue import PriorityQueue
import heapq
import sys

class CreateNode:
    def __init__(self, state, parent, action, cost, tile, deep):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.tile = tile
        self.deep = deep
        self.score = self.heuristic()


    def __lt__(self, other):
        if search == "a*":
          return (self.cost + self.score) < (other.cost + other.score)
        elif search == "greedy":
          return (self.score < other.score)
        elif search == "ucs":
            return (self.cost < other.cost)

    def __eq__(self, other):
      if search != "ucs":
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def heuristic(self):
        return sum(1 for i, row in enumerate(self.state) for j, val in enumerate(row) if val != 0 and val != 3 * i + j + 1)

    def __repr__(self):
        return f"{self.state}"

def get_position(state):
    #Returns the row and column position of the 0.
    for i, x in enumerate(state):
            if 0 in x:
                return i, x.index(0)

def possible_actions(state):
    #Returns the possible moves that can be made from the current state.
    r, c = get_position(state)
    actions = []
    if r > 0:
        actions.append('Down')
    if r < 2:
        actions.append('Up')
    if c > 0:
        actions.append('Right')
    if c < 2:
        actions.append('Left')
    return actions


def apply_action(state, action):
    #Returns the new state that results from applying the given action.
    new_state = [row[:] for row in state]
    row, col = get_position(new_state)

    if action == 'Right':
        new_state[row][col], new_state[row][col - 1] = new_state[row][col - 1], new_state[row][col]
    elif action == 'Left':
        new_state[row][col], new_state[row][col + 1] = new_state[row][col + 1], new_state[row][col]
    elif action == 'Down':
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]
    elif action == 'Up':
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]

    return (new_state, new_state[row][col])
# Bfs Search
def bfs_search(initial_state, goal_state):
    nodes_pooped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    new_cost = 0
    new_deep = 0
    start_node = CreateNode(initial_state, None, None, 0, 0, 0)
    fringe = deque()
    fringe.append(start_node)
    explored = set()
    if dump_flag == "true":
        trace_file = "trace_" + datetimestamp
        with open(f'{trace_file}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Command-Line Arguments : ['{start_file} ', '{goal_file} ', ' {method} ', '{dump_flag}']\n")
            f.write(f"Method Selected: {search} \n")
            f.write(f"Running {search} \n")

    while fringe:
            max_fringe_size = max(len(fringe), max_fringe_size)
            node = fringe.popleft()
            nodes_pooped += 1
            new_deep = node.deep
            if node.state == goal_state:
                solution = []
                while node.parent is not None:
                    solution.append(str(node.tile)+" "+node.action)
                    new_cost += node.tile
                    node = node.parent
                solution.reverse()
                return (solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
            explored.add(str(node.state))
            nodes_expanded = max(nodes_expanded, len(explored))
            nodes_generated_each_level = 0
            for action in possible_actions(node.state):
                 child_state, tile_position = apply_action(node.state, action)
                 if str(child_state) not in explored:
                     child_node = CreateNode(child_state, node, action, node.cost + tile_position, tile_position, node.deep+1)
                     fringe.append(child_node)
                     nodes_generated += 1
                     nodes_generated_each_level += 1
            if dump_flag == "true":
                with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                   f.write(f"Generating successors to < state = : {node}, action = Move {node.tile} {node.action}, cost = {node.cost}, d = {node.deep}, parent = {node.parent} \n")
                   f.write(f"{nodes_generated_each_level} successors generated \n")
                   f.write(f"Closed: {explored} \n")
                   f.write(f"Fringe: {fringe} \n")

    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)

#dfs Search
def dfs_search(initial_state, goal_state):
    nodes_pooped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    new_cost = 0
    new_deep = 0
    start_node = CreateNode(initial_state, None, None, 0, 0, 0)
    fringe = deque()
    fringe.append(start_node)
    explored = set()
    if dump_flag == "true":
        trace_file = "trace_" + datetimestamp
        with open(f'{trace_file}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Command-Line Arguments : ['{start_file} ', '{goal_file} ', ' {method} ', '{dump_flag}']\n")
            f.write(f"Method Selected: {search} \n")
            f.write(f"Running {search} \n")

    while fringe:
        max_fringe_size = max(len(fringe), max_fringe_size)
        node = fringe.pop()
        nodes_pooped += 1
        new_deep = node.deep
        if node.state == goal_state:
            solution = []
            while node.parent is not None:
                solution.append(str(node.tile)+" "+node.action)
                new_cost += node.tile
                node = node.parent
            solution.reverse()
            return (solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
        explored.add(str(node.state))
        nodes_expanded = max(nodes_expanded, len(explored))
        nodes_generated_each_level = 0
        for action in possible_actions(node.state):
            child_state, tile_position = apply_action(node.state, action)
            if str(child_state) not in explored:
                child_node = CreateNode(child_state, node, action, node.cost + tile_position, tile_position,node.deep+1)
                fringe.append(child_node)
                nodes_generated += 1
                nodes_generated_each_level +=1
        if dump_flag == "true":
            with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                f.write(f"Generating successors to < state = : {node}, action = Move {node.tile} {node.action}, cost = {node.cost}, d = {node.deep}, parent = {node.parent} \n")
                f.write(f"{nodes_generated_each_level} successors generated \n")
                f.write(f"Closed: {explored} \n")
                f.write(f"Fringe: {fringe} \n")
    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
#dls search
def dls_search(initial_state, goal_state, max_limit):
    nodes_pooped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    new_cost = 0
    new_deep = 0
    start_node = CreateNode(initial_state, None, None, 0, 0, 0)
    fringe = [(start_node, 0)]
    explored = set()
    if dump_flag == "true":
        trace_file = "trace_" + datetimestamp
        with open(f'{trace_file}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Command-Line Arguments : ['{start_file} ', '{goal_file} ', ' {method} ', '{dump_flag}']\n")
            f.write(f"Method Selected: {search} \n")
            f.write(f"Running {search} \n")

    while fringe:
        max_fringe_size = max(len(fringe), max_fringe_size)
        node, depth = fringe.pop()
        nodes_pooped += 1
        new_deep = node.deep
        if node.state == goal_state:
            solution = []
            while node.parent is not None:
                solution.append(str(node.tile) + " " + node.action)
                new_cost += node.tile
                node = node.parent
            solution.reverse()
            return (solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
        elif depth < max_limit:
            explored.add(str(node.state))
            nodes_expanded = max(nodes_expanded, len(explored))
            nodes_generated_each_level = 0
            for action in possible_actions(node.state):
              child_state, tile_position = apply_action(node.state, action)
              if str(child_state) not in explored:
                  child_node = CreateNode(child_state, node, action, node.cost + tile_position, tile_position,node.deep+1)
                  fringe.append((child_node, depth+1))
                  nodes_generated += 1
                  nodes_generated_each_level += 1
            if dump_flag == "true":
                with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                   f.write(f'Current_depth Level : {depth} \n')
                   f.write(f"Generating successors to < state = : {node}, action = Move {node.tile} {node.action}, cost = {node.cost}, d = {node.deep}, parent = {node.parent} \n")
                   f.write(f"{nodes_generated_each_level} successors generated \n")
                   f.write(f"Closed: {explored} \n")
                   f.write(f"Fringe: {fringe} \n")
    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
#ids search
def ids_search(initial_state, goal_state, max_depth):
    for level in range(max_depth):
        res, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = dls_search(initial_state, goal_state, level)
        if res:
            return (res, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth)
    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth)
#astar search
def astar_search(initial_state, goal_state):
    nodes_pooped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    new_cost = 0
    new_deep = 0
    start_node = CreateNode(initial_state, None, None, 0, 0,0)
    fringe = [start_node]
    heapq.heapify(fringe)
    explored = set()
    if dump_flag == "true":
        trace_file = "trace_" + datetimestamp
        with open(f'{trace_file}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Command-Line Arguments : ['{start_file} ', '{goal_file} ', ' {method} ', '{dump_flag}']\n")
            f.write(f"Method Selected: {search} \n")
            f.write(f"Running {search} \n")
    while fringe:
        max_fringe_size = max(len(fringe), max_fringe_size)
        node = heapq.heappop(fringe)
        nodes_pooped += 1
        new_deep = node.deep
        if node.state == goal_state:
            solution = []
            while node.parent is not None:
                solution.append(str(node.tile)+" "+node.action)
                new_cost += node.tile
                node = node.parent
            solution.reverse()
            return (solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
        explored.add(str(node.state))
        nodes_expanded = max(nodes_expanded, len(explored))
        nodes_generated_each_level = 0
        for action in possible_actions(node.state):
            child_state, tile_position = apply_action(node.state, action)
            if str(child_state) not in explored:
                child_node = CreateNode(child_state, node, action, node.cost + tile_position, tile_position,node.deep+1)
                heapq.heappush(fringe, child_node)
                nodes_generated += 1
                nodes_generated_each_level += 1
        if dump_flag == "true":
            with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                f.write(f"Generating successors to < state = : {node}, action = Move {node.tile} {node.action}, cost = {node.cost}, g(n) = {node.score}, f(n) ={node.cost}, d = {node.deep}, parent = {node.parent} \n")
                f.write(f"{nodes_generated_each_level} successors generated \n")
                f.write(f"Closed: {explored} \n")
                f.write(f"Fringe: {fringe} \n")
    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
#greedy search
def greedy_search(initial_state, goal_state):
    nodes_pooped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    new_cost = 0
    new_deep = 0
    start_node = CreateNode(initial_state, None, None, 0, 0,0)
    fringe = [start_node]
    heapq.heapify(fringe)
    explored = set()
    if dump_flag == "true":
        trace_file = "trace_" + datetimestamp
        with open(f'{trace_file}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Command-Line Arguments : ['{start_file} ', '{goal_file} ', ' {method} ', '{dump_flag}']\n")
            f.write(f"Method Selected: {search} \n")
            f.write(f"Running {search} \n")

    while fringe:
        max_fringe_size = max(len(fringe), max_fringe_size)
        node = heapq.heappop(fringe)
        nodes_pooped += 1
        new_deep = node.deep
        if node.state == goal_state:
            solution = []
            while node.parent is not None:
                solution.append(str(node.tile)+" "+node.action)
                new_cost += node.tile
                node = node.parent
            solution.reverse()
            return (solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
        explored.add(str(node.state))
        nodes_expanded = max(nodes_expanded,len(explored))
        nodes_generated_each_level = 0
        for action in possible_actions(node.state):
            child_state, tile_position = apply_action(node.state, action)
            if str(child_state) not in explored:
                child_node = CreateNode(child_state, node, action, node.cost + tile_position, tile_position,node.deep+1)
                heapq.heappush(fringe, child_node)
                nodes_generated += 1
                nodes_generated_each_level += 1
        if dump_flag == "true":
            with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                f.write(f"Generating successors to < state = : {node}, action = Move {node.tile} {node.action}, cost = {node.cost}, g(n) = {node.score}, d = {node.deep}, parent = {node.parent} \n")
                f.write(f"{nodes_generated_each_level} successors generated \n")
                f.write(f"Closed: {explored} \n")
                f.write(f"Fringe: {fringe} \n")
    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
#ucs search
def ucs_search(initial_state, goal_state):
    nodes_pooped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    new_cost = 0
    new_deep = 0
    start_node = CreateNode(initial_state, None, None, 0, 0,0)
    fringe = PriorityQueue()
    fringe.put(start_node)
    explored = set()
    if dump_flag == "true":
        trace_file = "trace_" + datetimestamp
        with open(f'{trace_file}.txt', 'w', encoding='utf-8') as f:
            f.write(f"Command-Line Arguments : ['{start_file} ', '{goal_file} ', ' {method} ', '{dump_flag}']\n")
            f.write(f"Method Selected: {search} \n")
            f.write(f"Running {search} \n")
    while fringe:
        max_fringe_size = max(fringe.qsize(), max_fringe_size)
        node = fringe.get()
        nodes_pooped += 1
        new_deep = node.deep
        if node.state == goal_state:
            solution = []
            while node.parent is not None:
                solution.append(str(node.tile)+" "+node.action)
                new_cost += node.tile
                node = node.parent
            solution.reverse()
            return (solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)
        explored.add(str(node.state))
        nodes_expanded = max(nodes_expanded, len(explored))
        nodes_generated_each_level = 0
        for action in possible_actions(node.state):
            child_state, tile_position = apply_action(node.state, action)
            child_node = CreateNode(child_state, node, action, node.cost + tile_position, tile_position, node.deep + 1)
            if str(child_state) not in explored:
                 fringe.put(child_node)
                 nodes_generated += 1
                 nodes_generated_each_level += 1
        if dump_flag == "true":
            with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                f.write(f"Generating successors to < state = : {node}, action = Move {node.tile} {node.action}, cost = {node.cost}, d = {node.deep}, parent = {node.parent} \n")
                f.write(f"{nodes_generated_each_level} successors generated \n")
                f.write(f"Closed: {explored} \n")
                f.write(f"Fringe: {fringe} \n")
    return (None, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, new_cost, new_deep)

def file_list_convertor(file_name, list_name):
    #converts the input file into a list
    file = open(file_name, "r+")
    for row in list(file):
        if (row != 'END OF FILE'):
            row_list = [int(i) for i in row.split()]
            list_name.append(row_list)
    return list_name

if __name__ == "__main__":
    initial_state = []
    goal_state = []
    max_depth = 1000
    start_file = ""
    goal_file = ""

    timestamp = datetime.now()
    datetimestamp = timestamp.strftime("%Y%m%d_%H%M%S")

    if len(sys.argv) < 3:
        print("Please enter start and goal file information")
    else:
       start_file = sys.argv[1]
       goal_file = sys.argv[2]

    if len(sys.argv) >= 4:
        method = str(sys.argv[3])
    else:
       method = "a*"
    if len(sys.argv) >= 5:
        dump_flag = str(sys.argv[4])
    else:
        dump_flag = "false"

    if method not in ["bfs","dfs","ucs","ids","dls","greedy","a*"]:
        search = "a*"
    else:
        search = method

    if search == "dls":
       limit = int(input("Enter the depth limit: "))

    initial_state = file_list_convertor(start_file,initial_state)
    goal_state  = file_list_convertor(goal_file,goal_state)
    if start_file != "" and goal_file != "":
        if search == "bfs":
           solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = bfs_search(initial_state, goal_state)
        elif search == "dfs":
            solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = dfs_search(initial_state, goal_state)
        elif search == "dls":
            solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = dls_search(initial_state,goal_state, limit)
        elif search == "ids":
            solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = ids_search(initial_state, goal_state, max_depth)
        elif search == "a*":
            solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = astar_search(initial_state, goal_state)
        elif search == "greedy":
            solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = greedy_search(initial_state, goal_state)
        elif search == "ucs":
            solution, nodes_pooped, nodes_expanded, nodes_generated, max_fringe_size, cost, depth = ucs_search(initial_state, goal_state)
        if dump_flag == "true":
            trace_file = "trace_" + datetimestamp
            with open(f'{trace_file}.txt', 'a', encoding='utf-8') as f:
                f.write(f"Nodes Popped: {nodes_pooped} \n")
                f.write(f"Nodes Expanded: {nodes_expanded} \n")
                f.write(f"Nodes Generated: {nodes_generated} \n")
                f.write(f"Max Fringe Size: {max_fringe_size} \n")

        print("Nodes Popped: ", nodes_pooped)
        print("Nodes Expanded: ", nodes_expanded)
        print("Nodes Generated: ", nodes_generated)
        print("Max Fringe Size: ", max_fringe_size)
        if solution:
          print(f"Solution Found at depth {depth} with cost of {cost}")
          print("Steps:")
          for move in solution:
            print("      Move", move)
        else:
            print("No Solution found")
    else:
        print("start and goal files are missing !!")