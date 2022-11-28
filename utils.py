from model import Obj
from model import State
from model import objects
from model import MAX_VALUE


class Utils:
    root: State
    costs: list
    goals: list[Obj]
    blockages: list[Obj]

    def __init__(self, matrix):
        self.model_matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.create_model()

    def create_model(self):
        for i in range(self.n):
            for j in range(self.m):
                m = self.model_matrix[i][j]
                row_cost = []
                if "r" in m:
                    self.root.robot = Obj(i, j, objects["r"])
                    m = m.replace("r", "")
                if "b" in m:
                    if "p" in m:
                        self.root.pass_butters.append(Obj(i, j, objects["b"]))
                        Utils.goals.append(Obj(i, j, objects["p"]))
                        m = m.replace("p", "")
                        m = m.replace("b", "")
                    else:
                        self.root.butters.append(Obj(i, j, objects["b"]))
                        m = m.replace("b", "")
                if "p" in m:
                    Utils.goals.append(Obj(i, j, objects["p"]))
                    m = m.replace("p", "")
                if "x" in m:
                    Utils.blockages.append(Obj(i, j, objects["x"]))
                    row_cost.append(MAX_VALUE)
                    m = m.replace("x", "")
                else:
                    row_cost.append(int(m))
                Utils.costs.append(row_cost)

    def update_model(self, matrix=None):
        if not matrix:
            self.model_matrix = matrix
            self.n = len(matrix)
            self.m = len(matrix[0])
        self.create_model()
