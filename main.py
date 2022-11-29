from utils import Utils
from successor import Successor

n, m = input('').split()
matrix = [input().split() for i in range(int(n))]
utils = Utils(matrix)
s = Successor(utils)
stack = [utils.root]
state = stack.pop()
while True:
    print(state)
    stack+=s.successor(state)
    if not stack or not state.butters:
        break
    state = stack.pop()

