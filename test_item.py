import unittest
import catalog, item, settings

class TestItem(unittest.TestCase):

    def setUp(self):
        self.page = open("bibrecord_example.html", "r").read()
        self.item = item.Item(self.page)

    def test_parse_html(self):
        bibdata = self.item.get_bibdata()
        self.assertEqual(bibdata['bibnumber'], ['B2915957x'])
        self.assertEqual(bibdata['Language'], ['eng'])
        self.assertEqual(bibdata['Note'], ['Includes index.'])
        self.assertEqual(bibdata['Standard No.'], 
            ['9780672330926 (hbk.)', '067233092X (hbk.)'])
        
if __name__ == '__main__':
    unittest.main()
