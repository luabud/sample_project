from this import d
import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(3) == 4


increment = 0.1

def set_height():
    pass

def set_length():
    pass

def turn():
    pass

def roll(l):
    for i in range(0,l):
        set_length(i+increment)

def jump(h):
    go_up(h)
    go_down(h)

def go_up(h):
    for i in range(0,h):
        set_height(i+increment)

def go_down(h):
    for i in range(h,0,-1):
        set_height(i+increment)

roll(2)
jump(30)
roll(4)
turn()