import sys


class Obj:
    row: int
    col: int
    type_obj: int

    def __init__(self, row, col, type_obj) -> None:
        self.col = col
        self.row = row
        self.type_obj = type_obj

    def __eq__(self, o: object) -> bool:
        if type(o) == Obj:
            return self.row == o.row and self.col == o.col
        if type(o) in [list, set, tuple]:
            return self.row == o[0] and self.col == o[1]
        else:
            raise Exception("Object not define")

    def copy(self):
        return Obj(self.row, self.col, self.type_obj)

    def get_location(self):
        return self.row, self.col
    
    def __str__(self):
        return "{ row:" + str(self.row) + ", col:"+ str(self.col) + ", type:" + objects[self.type_obj] + "}"
    
    def __add__(self, o):
        copy = self.copy()
        if type(o) == Obj:
            copy.row += o.row
            copy.col += o.col
            return copy
        if type(o) in [list, set, tuple]:
            copy.row += o[0]
            copy.col += o[1]
            return copy
        else:
            raise Exception("Object not define")

    def __hash__(self):
        return hash(self.row) + hash(self.col) + hash(self.col*self.row) + hash(str(self.row)) + hash(str(self.col)) + hash(str(self.col*self.row))

class State:
    robot: Obj
    butters: list[Obj]
    pass_butters: list[Obj]
    cost: int

    def __init__(self, state=None) -> None:
        if not state:
            self.parent = None
            self.butters = []
            self.pass_butters = []
            self.cost = 0
        else:
            self.parent = state
            self.robot = state.robot.copy()
            self.butters = [butter.copy() for butter in state.butters]
            self.pass_butters = [goal.copy() for goal in state.pass_butters]
            self.cost = state.cost

    def __eq__(self, o: object) -> bool:
        if self.robot != o.robot:
            return False
        counter = 0
        for butter in self.butters:
            for butter_o in o.butters:
                if butter == butter_o:
                    counter += 1
        for butter in self.pass_butters:
            for butter_o in o.pass_butters:
                if butter == butter_o:
                    counter += 1
        return counter == len(self.butters) + len(self.pass_butters)
    
    def __gt__(self, other):
        if type(other) == State:
            return self.cost >= other.cost
        else:
            raise Exception("Object not define")
        
    def __lt__(self, other):
        if type(other) == State:
            return self.cost <= other.cost
        else:
            raise Exception("Object not define")

    def copy(self):
        return State(self)
    
    def __str__(self):
        return self.robot.__str__()

    def __hash__(self):
        h1 = hash(self.robot)
        h2 = hash(self.robot)
        for obj in self.butters + self.pass_butters:
            h1 += hash(obj)
            h2 *= hash(obj)
        return h1 + h2
            
            



objects = {
    "p": 0,
    "r": 1,
    "b": 2,
    "x": 3,
    0: "p",
    1: "r",
    2: "b",
    3: "x",
}

MAX_VALUE = sys.maxsize

