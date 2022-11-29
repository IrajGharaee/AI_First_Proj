from utils import Utils
from successor import Successor

n, m = input('').split()
matrix = [input().split() for i in range(int(n))]
utils = Utils(matrix)
s = Successor(utils)
stack = [utils.root]
state = stack.pop()
state_set = set([])
state_set.add(state)
while True:
    stack += s.successor(state,state_set)
    if not stack or not state.butters:
        break
    state = stack.pop()


while state:
    print(state)
    state = state.parent



