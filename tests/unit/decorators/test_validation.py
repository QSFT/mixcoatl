import os
import sys
os.environ['ES_SECRET_KEY'] = '12345'
os.environ['ES_ACCESS_KEY'] = 'abcdef'

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from mixcoatl.decorators.validations import required_attrs
from mixcoatl.decorators.validations import ValidationException

class MockValidating(object):

    def __init__(self, v = None):
        self.__somevar = v

    @property
    def somevar(self):
        return self.__somevar

    @required_attrs(['somevar'])
    def some_action(self):
        return self.somevar

class TestValidations(unittest.TestCase):

    def setUp(self):
        self.klass_a = MockValidating()
        self.klass_b = MockValidating('foo')

    def test_raises_validation_error(self):
        with self.assertRaises(ValidationException):
            self.klass_a.some_action()

    def test_passes_validation(self):
        assert self.klass_b.some_action() == 'foo'

