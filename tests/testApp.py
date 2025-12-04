from src.app import add

def testAdd():
    assert add(1, 2) == 3

def testAdd2():
    assert add(1, 3) != 3