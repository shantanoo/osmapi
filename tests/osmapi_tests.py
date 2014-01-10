from nose.tools import *  # noqa
import unittest
import mock
import osmapi


class TestOsmApi(unittest.TestCase):
    def setUp(self):
        self.api = osmapi.OsmApi(
            api="api06.dev.openstreetmap.org"
        )

    def _http_get_mock(self, filename):
        with open(filename) as file:
            self.api._http_request = mock.Mock(
                return_value=file.read()
            )

    def teardown(self):
        pass

    def test_constructor(self):
        assert_true(isinstance(self.api, osmapi.OsmApi))

    def test_Capabilities(self):
        self._http_get_mock(self._testMethodName + ".xml")

        result = self.api.Capabilities()
        assert_equals(result, {
            u'area': {u'maximum': 0.25},
            u'changesets': {u'maximum_elements': 50000.0},
            u'status': {
                u'api': u'mocked',
                u'database': u'online',
                u'gpx': u'online'
            },
            u'timeout': {u'seconds': 300.0},
            u'tracepoints': {u'per_page': 5000.0},
            u'version': {u'maximum': 0.6, u'minimum': 0.6},
            u'waynodes': {u'maximum': 2000.0}
        })

    def test_NodeGet(self):
        self._http_get_mock(self._testMethodName + ".xml")

        result = self.api.NodeGet(123)
        assert_equals(result, {
            u'id': 123,
            u'changeset': 15293,
            u'uid': 605,
            u'timestamp':
            u'2012-04-18T11:14:26Z',
            u'lon': -1.4857118,
            u'visible': True,
            u'version': 8,
            u'user': u'freundchen',
            u'lat': 51.8753146,
            u'tag': {
                u'amenity': u'school',
                u'foo': u'bar',
                u'name':
                u'Berolina & Schule'
            },
        })
