import sys


def dfs(root, s):
    stack = [root]
    state_set = set([])
    state_set.add(root)
    state = root
    while stack and state.butters:
        stack += s.successor(state, state_set)
        state = stack.pop()
    return state


def bfs(root, s):
    stack = [root]
    state_set = set([])
    state_set.add(root)
    state = root
    while stack and state.butters:
        stack += s.successor(state, state_set)
        state = stack.pop(0)
    return state


def ids(root, s):
    depth = 0
    while True:
        stack = [root]
        state_set = set([])
        state_set.add(root)
        state = root
        while stack and state.butters:
            state = stack.pop()
            if state.depth <= depth:
                stack += s.successor(state, state_set)
            if not state.butters:
                return state
        depth += 1
        if depth > 100:
            return None


def ucs(root,s):
    states = set([root])
    state_set = set([])
    state_set.add(root)
    state = root
    while states and state.butters:
        state = min(states)
        states = states.union(set(s.successor(state, state_set)))
        states.remove(state)
    return state

def A_star(root, s):
    def find_best(utils):
        total_cost = sys.maxsize
        for _state in states:
            if _state.cost + _state.heuristic(utils) < total_cost:
                total_cost = _state.cost + _state.heuristic(utils)
                chosen_state = _state
        return chosen_state

    states = [root]
    state_set = set([])
    state_set.add(root)
    state = root
    while states and state.butters:
        state = states.pop(states.index(find_best(states)))
        states += s.successor(state, state_set)
    return state

def best_first_search(root, s, utils):
    def find_best():
        cost = sys.maxsize
        for _state in states:
            if _state.heuristic(utils) < cost:
                cost = _state.heuristic(utils)
                chosen_state = _state
        return chosen_state

    states = [root]
    state_set = set([])
    state_set.add(root)
    state = root
    while states and state.butters:
        state = states.pop(states.index(find_best(states)))
        states += s.successor(state, state_set)
    return state