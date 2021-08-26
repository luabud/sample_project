import inc_dec    

def test_add_zero():
    assert inc_dec.add_zero(1) == 1
    
def test_increment():
    assert inc_dec.increment(3) == 4

def test_decrement():
    assert inc_dec.decrement(5) == 3

