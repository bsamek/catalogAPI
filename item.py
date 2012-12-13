"""This module provides the class Item, representing a bibliographic item."""

from bs4 import BeautifulSoup

class Item:
    """A bibliographic item. 
   
    fields:
    self.bibdata[] -- a list of bibliographic data 
    """

    def __init__(self, page):
        self.parse_html(page)

    def bibdata_as_text(self):
        """Get bibdata as text."""
        text = ""
        for item in self.bibdata:
            text += item[0]
            text += ": "
            text += item[1]
            text += "\n"

        return text

    def bibdata_as_csv(self):
        """Get bibdata as csv."""

    def bibdata_as_json(self):
        """Get bibdata as json."""

    def parse_html(self, page):
        """Parses HTML page of a bib record.

        Returns a 2-dimensional list."""

        self.bibdata = []

        # Build the BeautifulSoup tree
        soup = BeautifulSoup(page)

        # Get tables
        tables = soup('table')
        headers = tables[2]('th')
        top, middle, bottom = tables[3], tables[4], tables[5]

        # Parse headers 
        for header in headers:
            split = header.text.split(':')
            if len(split) > 1:
                self.bibdata.append([split[0], split[1].strip()])
            else:
                self.bibdata.append(['bibnumber', split[0]])

        # Parse top table
        for field in top('td'):
            self.bibdata.append([field.em.text, field.strong.text])

        # Parse middle table
        for field in zip(*[iter(middle('td'))]*2):
            self.bibdata.append([field[0].text, field[1].text])

        # Parse bottom table
        for field in zip(*[iter(bottom('td'))]*2):
            self.bibdata.append([field[0].text, field[1].text])

if __name__ == '__main__':
    item = Item(open("bibrecord_example.html", "r").read())
    print item.bibdata_as_text()
