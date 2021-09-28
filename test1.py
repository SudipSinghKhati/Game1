import pytest


@pytest.fixture
def tester():
    name = "sudip"
    contact = 9865623115
    return [name, contact]


def testing_1(tester):
    first_name = "sudip"
    assert tester[0] == first_name


def testing_2(tester):
    contact_num = 9865623115
    assert tester[1] == contact_num
