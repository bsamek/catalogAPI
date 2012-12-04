import unittest
import catalog, item, settings

class TestCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = catalog.Catalog()

if __name__ == '__main__':
    unittest.main()
