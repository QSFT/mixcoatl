import os
import sys
os.environ['ES_SECRET_KEY'] = '12345'
os.environ['ES_ACCESS_KEY'] = 'abcdef'

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from mixcoatl.decorators.lazy import lazy_property
from mixcoatl.resource import Resource

class MockResource(Resource):
    path = 'mock/Resource'
    collection_name = 'resources'
    primary_key = 'resource_id'

    def __init__(self, resource_id = None, *args, **kwargs):
        Resource.__init__(self)
        self.__resource_id = resource_id

    def load(self):
        #privprefix = '_'+self.__class__.__name__
        #setattr(self,privprefix+'__attr_a', 'foo')
        #setattr(self,privprefix+'__attr_b', 'bar')
        self.__attr_a = 'foo'
        self.__attr_b = 'bar'
        self.loaded = True

    @property
    def resource_id(self):
        return self.__resource_id

    @lazy_property
    def attr_a(self):
        return self.__attr_a

    @lazy_property
    def attr_b(self):
        return self.__attr_b

    @attr_b.setter
    def attr_b(self, bid):
        self.__attr_b = bid

class TestLazyProps(unittest.TestCase):

    def setUp(self):
        self.mock_resource = MockResource()
        self.mock_resource_with_id = MockResource(12345)

    def test_mock_resource_no_id(self):
        assert self.mock_resource.resource_id is None

    def test_mock_resource_immutable_attr(self):
        with self.assertRaises(TypeError):
            self.mock_resource.attr_a = '12345'

    def test_mock_resource_mutable_attr(self):
        self.mock_resource.attr_b = '9876'
        assert self.mock_resource.attr_b == '9876'

    def test_mock_resource_with_id(self):
        assert self.mock_resource_with_id.resource_id == 12345

    def test_mock_resource_with_id_getter_attr_a(self):
        assert self.mock_resource_with_id.attr_a == 'foo'

    def test_mock_resource_with_id_immutable(self):
        with self.assertRaises(TypeError):
            self.mock_resource_with_id.attr_a = '12345'

    def test_mock_resource_with_id_getter_attr_b(self):
        assert self.mock_resource_with_id.attr_b == 'bar'

    def test_mock_resource_with_id_setter_attr_b(self):
        assert self.mock_resource_with_id.attr_b == 'bar'
        self.mock_resource_with_id.attr_b = 'snarf'
        assert self.mock_resource_with_id.attr_b == 'snarf'