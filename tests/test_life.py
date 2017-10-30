from nose.tools import raises
from src.life import life


@raises(TypeError)
def test_should_raise_type_error_on_zero_none_shape():
    life([0])


@raises(TypeError)
def test_should_raise_type_error_on_zero_zero_shape():
    life([[]])
