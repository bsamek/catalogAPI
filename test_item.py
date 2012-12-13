import unittest
import catalog, item, settings

class TestItem(unittest.TestCase):

    def setUp(self):
        self.page = open("bibrecord_example.html", "r").read()
        self.item = item.Item(self.page)

    def test_parse_html(self):
        def findl(k):
            return [x[1] for x in self.item.bibdata if x[0] == k]
        self.assertEqual(findl('bibnumber')[0], unicode('B2915957x'))
        self.assertEqual(findl('Language')[0], unicode('eng'))
        self.assertEqual(findl('Note')[0], unicode('Includes index.'))

        self.assertEqual(findl('Misc.')[0], unicode('SKY'))
        self.assertEqual(findl('Misc.')[1], unicode('20110202000000.0'))
        
if __name__ == '__main__':
    unittest.main()
