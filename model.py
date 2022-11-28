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


class State:
    robot: Obj
    butters: list[Obj]
    pass_butters: list[Obj]

    def __init__(self, state=None) -> None:
        if not state:
            self.parent = None
        else:
            self.parent = state
            self.robot = state.robot.copy()
            self.butters = [butter.copy() for butter in state.butters]
            self.pass_butters = [goal.copy() for goal in state.pass_butters]

    def __eq__(self, o: object) -> bool:
        if self.robot != o.robot:
            return False
        counter = 0
        for butter in self.butters:
            for butter_o in o.butters:
                if butter.__eq__(butter_o):
                    counter += 1
        for butter in self.pass_butters:
            for butter_o in o.pass_butters:
                if butter.__eq__(butter_o):
                    counter += 1
        return counter == len(self.butters) + len(self.pass_butters)

    def copy(self):
        return State(self)


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

