from flask import Flask

from catalog import Catalog
from item import Item

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

@app.route('/barcode/<barcode>')
def lookup(barcode):
     catalog = Catalog()
     item = Item(catalog.search_barcode(barcode))
     return item.bibdata_as_text()
# 
# if __name__ == "__main__":
#     main("")

if __name__ == "__main__":
    app.run()
