"""
This module tests username and password from login page bu using pytest.
"""
import pytest


@pytest.mark.parametrize("username, password", [("admin", "admin"), ("admin", "sudip")])
def test_method(username, password):
    assert username == password
