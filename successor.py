from model import State
from utils import Utils

class Successor:
    utils: Utils
    
    def __init__(self,utils):
        self.utils = utils
    
    def successor(self,state: State) -> list[State]:
        states = []
        for move in {(1,0),(-1,0),(0,1),(0,-1)} :
            r,b = self.check_location_free(state,move)
            if r:
                new_state = State(state)
                new_state.robot += move
                if b:
                    _x, _y = state.robot.get_location()
                    if self.utils.goals[_x][_y]:
                        new_state.butters.remove(b)
                        new_state.pass_butters.append(b+move)
                    else:
                        new_state.butters.remove(b)
                        new_state.butters.append(b + move)
                s = state.parent
                repeat = False
                while s:
                    if s == new_state:
                        repeat = True
                        break
                    s = s.parent
                if not repeat:
                    states.append(new_state)
        return states
    def check_location_free(self,state, move):
        _x, _y = state.robot.get_location()
        if 0 <= _x + move[0] < self.utils.n and 0 <= _y + move[1] < self.utils.m:
            if self.utils.blockages[ _x + move[0] ][ _y + move[1]]:
                return False,False
            for butter in state.butters:
                if butter == [ _x + move[0] , _y + move[1] ]:
                    if 0 <= _x + 2*move[0] < self.utils.n and 0 <= _y + 2*move[1] < self.utils.m:
                        if self.utils.blockages[_x + 2*move[0]][_y + 2*move[1]]:
                            return False,False
                        for b in state.butters:
                            if b == [ _x + 2*move[0] , _y + 2*move[1] ]:
                                return False,False
                        return True,butter
                    else:
                        return False,False
            for butter in state.pass_butters:
                if butter == [ _x + move[0] , _y + move[1] ]:
                    return False,False
            return True,False
        else:
            return False,False

