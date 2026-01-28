import os
import sys
from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

    #dones
    