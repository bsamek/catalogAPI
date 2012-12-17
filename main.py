from flask import Flask
from flask import Response

from catalog import Catalog
from item import Item

app = Flask(__name__)
catalog = Catalog()

@app.route('/<barcode>.xml')
def lookup_xml(barcode):
    xml = Item(catalog.search_barcode(barcode)).bibdata_as_xml()
    return Response(xml, mimetype='text/xml')

@app.route('/<barcode>.txt')
def lookup_txt(barcode):
    text = Item(catalog.search_barcode(barcode)).bibdata_as_txt()
    return Response(text, mimetype='text/plain')

@app.route('/<barcode>.json')
def lookup_json(barcode):
    json = Item(catalog.search_barcode(barcode)).bibdata_as_json()
    return Response(json, mimetype='application/json')

if __name__ == "__main__":
    app.run()
    
