from model import State

def successor(state: State) -> list[State]:
    loc_x, loc_y = State.robot.get_location()

    for i in {(1,0),(-1,0),(0,1),(0,-1)} :
        pass