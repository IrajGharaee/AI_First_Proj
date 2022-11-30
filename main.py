from utils import Utils
from successor import Successor
from model import objects
from algorithm import dfs,bfs,ucs,ids
import os

clear = lambda: os.system('cls')
n, m = input('').split()
matrix = [input().split() for i in range(int(n))]
utils = Utils(matrix)
s = Successor(utils)

state_dfs = dfs(utils.root,s)
state_bfs = bfs(utils.root,s)
state_ids = ids(utils.root,s)
state_ucs = ucs(utils.root,s)

clear()

while state_ucs:
    utils.print_matrix(state_ucs)
    state_ucs = state_ucs.parent