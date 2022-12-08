from utils import Utils
from successor import Successor
from model import objects
from algorithm import dfs,bfs,ucs,ids
import os
import time

"""
6 10
1r 1 1 1 x x 1 1 1 1
1 x 1 1 2 2 1 1 1 1
x 1 1 2b 2 2 2b 1 x x
x 1 1 x x 2 2 1 1p x
1 1 1 1 2 2 1 1 1 1
1 1 1 1 x 1p x 1 1 1
"""

clear = lambda: os.system('cls')
n, m = input('').split()
matrix = [input().split() for i in range(int(n))]
utils = Utils(matrix)
s = Successor(utils)

# state_dfs = dfs(utils.root,s)
# state_bfs = bfs(utils.root,s)
# state_ids = ids(utils.root,s)
state_ucs = ucs(utils.root,s)

state = state_ucs
states = []
while state:
    states.append(state)
    state = state.parent

while states:
    utils.print_matrix(states.pop())
    time.sleep(2)