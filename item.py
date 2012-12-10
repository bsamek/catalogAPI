"""This module provides the class Item, representing a bibliographic item."""

from bs4 import BeautifulSoup

class Item:
    """A bibliographic item."""

    def __init__(self, page):
        self.parse_html(page)

    def get_bibdata(self):
        """Pretty print the bib data"""
        return {}

    def parse_html(self, page):
        self.bibdata = []

        """Parses HTML page of a bib record.

        Returns a 2-dimensional list."""

        # Build the BeautifulSoup tree
        soup = BeautifulSoup(page)

        # Get tables
        tables = soup('table')
        full = tables[2]
        top, middle, bottom = tables[3], tables[4], tables[5]

        # Parse the headers 
        headers = full('th')
        for header in headers:
            split = header.text.split(':')
            if len(split) > 1:
                self.bibdata.append([split[0], split[1].strip()])
            else:
                self.bibdata.append(['bibnumber', split[0]])

        print self.bibdata



