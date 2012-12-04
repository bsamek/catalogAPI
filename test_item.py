import unittest
import catalog, item, settings

class TestCatalog(unittest.TestCase):

    def setUp(self):
        self.page = open("bibrecord_example.html", "r").read()
        self.item = item.Item()

    def test_returns_dictionary(self):
        bibdata = self.item.get_bibdata()
        self.assertIsInstance(bibdata, dict)

    def test_bibnumber_in_dictionary(self):
        bibdata = self.item.get_bibdata()
        self.assertEqual(bibdata["bibnumber"], "B2915957x")

if __name__ == '__main__':
    unittest.main()
