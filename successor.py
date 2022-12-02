from model import State
from utils import Utils

class Successor:
    utils: Utils
    
    def __init__(self,utils):
        # initialization
        self.utils = utils

    # input state and set of state seen before
    # output states of expand state
    # order O(k^2)
    def successor(self,state: State,state_set) -> list[State]:
        states = [] # output
        for move in {(1,0),(-1,0),(0,1),(0,-1)} : # move left right top down O(1)
            # r := true of robot can move
            # b := true if exist robot after robot and butter moved
            r,b = self.check_location_free(state,move) # O(
            if r:
                # move robot
                _x, _y = state.robot.get_location()
                new_state = State(state) # copy of state
                new_state.robot += move # move robot
                new_state.cost += self.utils.costs[_x + move[0]][_y + move[1]] # set cost
                new_state.depth += 1 # set depth
                if b: # move butter
                    if self.utils.goals[_x + 2*move[0]][_y + 2*move[1]]: # if the butter moves into the target
                        new_state.butters.remove(b)
                        new_state.pass_butters.append( b + move )
                    else:
                        new_state.butters.remove(b)
                        new_state.butters.append(b + move)
                if new_state not in state_set : # if this state has not seen till now ( check cycle loop )
                    states.append(new_state)
        state_set.add(state)
        return states

    # if k := number of butter
    # order is O(k^2)
    def check_location_free(self,state, move):
        _x, _y = state.robot.get_location()
        if 0 <= _x + move[0] < self.utils.n and 0 <= _y + move[1] < self.utils.m: # if robot can move
            if self.utils.blockages[ _x + move[0] ][ _y + move[1]]: # if location blockage O(1)
                return False,False
            # O(k^2)
            for butter in state.butters: # O(k)
                if butter == [ _x + move[0] , _y + move[1] ]: # if butter in front of the robot
                    if 0 <= _x + 2*move[0] < self.utils.n and 0 <= _y + 2*move[1] < self.utils.m: # if butter can move
                        if self.utils.blockages[_x + 2*move[0]][_y + 2*move[1]]: # if location blockage O(1)
                            return False,False
                        for b in state.butters: # if butter in front of the butter O(k)
                            if b == [ _x + 2*move[0] , _y + 2*move[1] ]:
                                return False,False
                        for b in state.pass_butters: # if butter in front of the butter O(k)
                            if b == [ _x + 2*move[0] , _y + 2*move[1] ]:
                                return False,False
                        return True,butter # robot and butter moved
                    else:
                        return False,False
            # O(k)
            for butter in state.pass_butters: # if butter in goal and butter in front of the robot O(k)
                if butter == [ _x + move[0] , _y + move[1] ]:
                    return False,False
            return True,False # move robot
        else:
            return False,False
