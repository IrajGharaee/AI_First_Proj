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

    def __str__(self) -> str:
        pass


class State:
    robot: Obj
    butters: list[Obj]
    goals_have_butter: list[Obj]

    def __init__(self, parent) -> None:
        self.parent = parent

    def __eq__(self, o: object) -> bool:
        if self.robot != o.robot:
            return False

        counter = 0
        for butter in self.butters:
            for butter_o in o.butters:
                if butter.__eq__(butter_o):
                    counter += 1

        for butter in self.goals_have_butter:
            for butter_o in o.goals_have_butter:
                if butter.__eq__(butter_o):
                    counter += 1

        return counter == len(self.butters) + len(self.goals_have_butter)

    def __str__(self) -> str:
        pass


objects = {
    "p": 0,
    "r": 1,
    "b": 2,
    "x": 3,
}



MAX_VALUE = 10 ^ 10
