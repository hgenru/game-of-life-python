from nose.tools import raises
from src.live import live


@raises(TypeError)
def test_should_raise_type_error_on_zero_none_shape():
    live([0])


@raises(TypeError)
def test_should_raise_type_error_on_zero_zero_shape():
    live([[]])
