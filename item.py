"""This module provides the class Item, representing a bibliographic item."""

import json
from bs4 import BeautifulSoup

class Item:
    """A bibliographic item. 

    Item is initialized by passing it the HTML of a bibliographic
    record page from the staff OPAC. Initialization automatically
    calls parse_html(), which parses the HTML into the list
    bibdata. The bibdata can be returned in text, json or xml.

    fields:
    self.bibdata[] -- a list of bibliographic data 

    public methods:
    __init__(page) -- calls parse_html of page, sets self.bibdata
    bibdata_as_txt() -- returns bibdata as text
    bibdata_as_json() -- returns bibdata as json
    bibdata_as_xml() -- returns bibdata as xml

    """

    def __init__(self, page):
        """Parses page with parse_html."""
        self.parse_html(page)
        
    def bibdata_as_txt(self):
        """Get bibdata as text."""
        text = ""
        for field in self.bibdata:
            text += field[0]
            text += ": "
            text += field[1]
            text += "\n"

        return text

    def bibdata_as_json(self):
        """Get bibdata as json."""
        return json.dumps(self.bibdata)

    def bibdata_as_xml(self):
        """Get bibdata as XML."""
        soup = BeautifulSoup("<record></record>")

        for field in self.bibdata:
            tag = soup.new_tag("field", type=field[0])
            tag.string = field[1]
            soup.record.append(tag)

        return soup.prettify()


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
