from utils import Utils
from successor import Successor
from algorithm import dfs,bfs,ucs,ids,best_first_search,A_star


"""
6 10
1r 1 1 1 x x 1 1 1 1
1 x 1 1 2 2 1 1 1 1
x 1 1 2b 2 2 2b 1 x x
x 1 1 x x 2 2 1 1p x
1 1 1 1 2 2 1 1 1 1
1 1 1 1 x 1p x 1 1 1
"""

n, m = input('').split()
matrix = [input().split() for i in range(int(n))]
utils = Utils(matrix)
s = Successor(utils)

# state_dfs = dfs(utils.root,s)
state_bfs = bfs(utils.root,s)
# state_ids = ids(utils.root,s)
# state_ucs = ucs(utils.root,s)
# state_A_star = A_star(utils.root,s,utils)
# state_best_first_search = best_first_search(utils.root,s,utils)

state = state_bfs
states = []
while state:
    states.append(state)
    state = state.parent

while states:
    print(states.pop().move,end="")
    # utils.print_matrix(states.pop())
    # time.sleep(2)