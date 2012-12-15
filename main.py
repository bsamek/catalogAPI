from flask import Flask
from flask import Response

from catalog import Catalog
from item import Item

app = Flask(__name__)
catalog = Catalog()

@app.route('/<barcode>.xml')
def lookup(barcode):
    xml = Item(catalog.search_barcode(barcode)).bibdata_as_xml()
    return Response(xml, mimetype='text/xml')

if __name__ == "__main__":
    app.debug = True
    app.run()
    
