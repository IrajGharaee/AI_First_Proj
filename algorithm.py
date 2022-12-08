def dfs(root,s):
    stack = [root]
    state_set = set([])
    state_set.add(root)
    state = root
    while stack and state.butters:
        stack += s.successor(state, state_set)
        state = stack.pop()
    return state

def bfs(root,s):
    stack = [root]
    state_set = set([])
    state_set.add(root)
    state = root
    while stack and state.butters:
        stack += s.successor(state, state_set)
        state = stack.pop(0)
    return state

def ids(root,s):
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