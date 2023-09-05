import pytest
import time

# marking/test_marking.py

@pytest.fixture
def value(request):
    marker = request.node.get_closes_marker("override_value")
    if marker is not None:
        return marker.args[0]
    return 42

def test_the_answer(value):
    assert value == 42

@pytest.override_answer
def test_override_answer(value=23):
    assert 

@pytest.fixture
def is_marker_present(request: pytest.FixtureRequest):
    marker = request.function.get_closest_marker
    return marker



@pytest.mark.slow
@pytest.mark.webtest
def test_slow_api():
    time.sleep(1)

@pytest.mark.webtest
def test_api():
    pass

def test_fast():
    pass
