from model import Obj
from model import State
from model import objects
from model import MAX_VALUE

n, m = input('').split()
n = int(n)
m = int(m)

M1 = []
M2 = []
goals = []
butters = []
blockages = []
robot =

state_root = State(None)

for i in range(n):
    row = input('')
    row_M1 = []
    row_M2 = []
    j = 0
    for m in row.split():
        if "r" in m:
            state_root.robot = Obj(i, j, objects["r"])
            m.replace("r", "")
        if "b" in m:
            if "p" in m:
                state_root.goals_have_butter.append(Obj(i, j, objects["b"]))
                goals.append(Obj(i, j, objects["p"]))
                m.replace("p", "")
                m.replace("b", "")
            else:
                state_root.butters.append(Obj(i, j, objects["b"]))
                m.replace("b", "")
        if "p" in m:
            state_root.goals_have_butter.append(Obj(i, j, objects["p"]))
            goals.append(Obj(i, j, objects["p"]))
            m.replace("p", "")


