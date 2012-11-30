import unittest
import catalog, settings

class TestCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = catalog.Catalog()

    def test_login_successful(self):
        response = self.catalog.login()
        self.assertTrue(settings.LOGIN_SUCCESS in response.read())

    def test_search_barcode(self):
        pass

if __name__ == '__main__':
    unittest.main()
