from hello_world import hello_world
def test_hello_world():
    assert hello_world.hello() == "Hello, World!"

def test_hello_world_error():
    assert hello_world.hello().isnumeric() == False
