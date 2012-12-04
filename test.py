import unittest
import catalog, settings

class TestCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = catalog.Catalog()

    def test_login_successful(self):
        response = self.catalog.login()
        self.assertTrue(settings.LOGIN_SUCCESS in response.read())

    def test_search_barcode(self):
        barcode = "32405004460179"
        title = "Windows server 2008 R2 unleashed"

        page = self.catalog.search_barcode(barcode)

        # "2011" only appears in staff's record
        self.assertTrue("2011" in page)
        self.assertTrue(title in page)

    def test_is_logged_in(self):
        self.assertTrue(not self.catalog.is_logged_in())
        self.catalog.login()
        self.assertTrue(self.catalog.is_logged_in())

class TestItem(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
