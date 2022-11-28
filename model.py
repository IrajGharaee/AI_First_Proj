class Obj:
    row: int
    col: int
    type: int
    cost: int

    def __init__(self):
        pass

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

    def __init__(self, robot: Obj, butters: list[Obj], visited, parents) -> None:
        pass

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
