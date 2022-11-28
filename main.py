from utils import Utils
from successor import Successor

n, m = input('').split()
matrix = [input().split() for i in range(int(n))]
utils = Utils(matrix)
s = Successor(utils)
states = s.successor(utils.root)
stack = states
state = stack.pop()
while len(state.butters) > 0:
    # print("s:",state.robot)
    states = s.successor(utils.root)
    stack = stack + states
    state = stack.pop()
