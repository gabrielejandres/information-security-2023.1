import sys

sys.path.append('../')
from src.utils import *

def test_get_unicode():
    assert get_unicode("CRIPTOGRAFIA_128") == [67, 82, 73, 80, 84, 79, 71, 82, 65, 70, 73, 65, 95, 49, 50, 56]

def test_format_to_hex():
    assert format_to_hex(67) == "43"