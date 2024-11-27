from src.math_operations import add, sub

def test_add():
    assert add(2,5)==7
    assert add(8,4)==12

def test_sub():
    assert sub(3,1)==2
    assert sub(7,2)==5
    assert sub(1,2)==-1