from model import State
from utils import Utils


class Successor:
    utils: Utils
    
    def __init__(self,utils):
        self.utils = utils
    
    def successor(self,state: State) -> list[State]:
        states = []
        for move in {(1,0),(-1,0),(0,1),(0,-1)} :
            if self.check_location_free(state,move):
                # print(state)
                new_state = State(states)
                # print(new_state)
                new_state.robot += move
                states.append(new_state)
        return states
    def check_location_free(self,state, move):
        _x, _y = state.robot.get_location()
        if 0 <= _x + move[0] < self.utils.n and 0 <= _y + move[1] < self.utils.m:
            if self.utils.blockages[ _x + move[0] ][ _y + move[1]]:
                return False
            for butter in state.butters:
                if butter == [ _x + move[0] , _y + move[1] ]:
                    if 0 <= _x + 2*move[0] < self.utils.n and 0 <= _y + 2*move[1] < self.utils.m:
                        if self.utils.blockages[_x + 2*move[0]][_y + 2*move[1]]:
                            return False
                        for b in state.butters:
                            if b == [ _x + 2*move[0] , _y + 2*move[1] ]:
                                return False
                    else:
                        return False
            for butter in state.pass_butters:
                if butter == [ _x + move[0] , _y + move[1] ]:
                    return False
            s = state.parent
            while s:
                # print(s)
                # print(state)
                # print(s==state)
                if s == state:
                    return False
                s = s.parent
            return True
        else:
            return False

