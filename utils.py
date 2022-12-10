from model import Obj
from model import State
from model import objects
from model import MAX_VALUE


class Utils:
    root: State # root state ( matrix input )
    costs: list[int] # matrix n*m of cost of each element
    goals: list[Obj] # matrix n*m of goals ( if element not goal element is none )
    blockages: list[Obj] # matrix n*m of blockages ( if element not block element is none )
    goals_list : list[Obj]

    def __init__(self, matrix):
        # initialization
        self.model_matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.goals = [[None]*self.m for i in range(self.n)] # O(n*m)
        self.blockages = [[None]*self.m for i in range(self.n)] # O(n*m)
        self.costs = [[0]*self.m for i in range(self.n)] # O(n*m)
        self.root = State()
        # create model matrix ( fill root state , goals , blocks , costs )
        self.goals_list = []
        self.create_model() # O(n*m)


    def create_model(self): # O(n*m)
        # iterate over the array row
        for i in range(self.n): # O(n)
            # iterate over each element row(i)
            for j in range(self.m): # O(m)
                m = self.model_matrix[i][j] # consider m:M_ij
                if "r" in m: # if robot in m
                    self.root.robot = Obj(i, j, objects["r"])
                    m = m.replace("r", "")
                if "b" in m: # if butter in m
                    if "p" in m: # if butter and point ( goal ) in m
                        self.root.pass_butters.append(Obj(i, j, objects["b"]))
                        self.goals.append(Obj(i, j, objects["p"]))
                        m = m.replace("p", "")
                        m = m.replace("b", "")
                    else: # if only butter in m
                        self.root.butters.append(Obj(i, j, objects["b"]))
                        m = m.replace("b", "")
                if "p" in m: # if point ( goal ) in m
                    self.goals[i][j] = Obj(i, j, objects["p"])
                    self.goals_list.append(Obj(i, j, objects["p"]))
                    m = m.replace("p", "")
                if "x" in m: # if m is blockage
                    self.blockages[i][j] = Obj(i, j, objects["x"])
                    self.costs[i][j] = MAX_VALUE # add cost maximum
                    m = m.replace("x", "")
                else: # add cost element
                    self.costs[i][j] = int(m)

    def update_model(self, matrix=None): # update model new matrix : O(n*m)
        if not matrix:  # O(1)
            self.model_matrix = matrix
            self.n = len(matrix)
            self.m = len(matrix[0])
        self.create_model() # O(n*m)


    def print_matrix(self, _state): # print matrix from state  O(n*m)

        matrix = [row.copy() for row in self.costs] # copy matrix cost
        matrix[_state.robot.row][_state.robot.col] = str(matrix[_state.robot.row][_state.robot.col]) + objects[
            _state.robot.type_obj] # add robot state
        for obj in _state.butters: # add butter state . if k:= count butters O(k)
            matrix[obj.row][obj.col] = str(matrix[obj.row][obj.col]) + objects[obj.type_obj]
        for obj in _state.pass_butters: # add butter in goals state . if k:= count butters O(k)
            matrix[obj.row][obj.col] = str(matrix[obj.row][obj.col]) + objects[obj.type_obj]
        for i in range(self.n): # add blockage and goals O(n*m)
            for j in range(self.m):
                if MAX_VALUE == self.costs[i][j]: # blockage
                    matrix[i][j] = "x"
                if self.goals[i][j]: # point ( goal )
                    matrix[i][j] = str(matrix[i][j] ) + "p"

        for row in matrix:
            for a in row:
                print(a, end="\t")
            print()
        print()