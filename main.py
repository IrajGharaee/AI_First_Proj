from utils import Utils
from successor import Successor
from model import objects
import os
clear = lambda: os.system('cls')

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

print("DFS")
while state:
    utils.print_matrix(state)
    state = state.parent

s = Successor(utils)
stack = [utils.root]
state = stack.pop()
state_set = set([])
state_set.add(state)
while True:
    stack += s.successor(state,state_set)
    if not stack or not state.butters:
        break
    state = stack.pop(0)







print("BFC")
while state:
    utils.print_matrix(state)
    state = state.parent



s = Successor(utils)
states = [utils.root]
state = stack.pop()
state_set = set([])
state_set.add(state)
while True:
    stack += s.successor(state,state_set)
    if not state or not state.butters:
        break
    state = states.pop(states.index(max(states)))

print("UCS")
while state:
    utils.print_matrix(state)
    state = state.parent