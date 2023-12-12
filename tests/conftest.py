import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(length=10, width=20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)
