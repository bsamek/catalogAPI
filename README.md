catalogAPI
==========
This provides an API for the Minuteman Library Network catalog.

Try it out:

pip install Flask BeautifulSoup4  
python main.py  

You can then query a barcode number and get text, json, or xml back by
visiting one of these:

localhost:5000/<barcode>.txt  
localhost:5000/<barcode>.json  
localhost:5000/<barcode>.xml  

For example, visiting http://localhost:5000/32405004416247.txt will return:

bibnumber: B29547350  
Last updated: 03-18-13  
Created: 11-10-11  
Revision: 17  
Language: eng  
Skip: 0  
Location: multi  
Cat. Date: 12-27-11  
Bib Level: m  
Material Type: a  
Bib Code 3: -  
Country: mnu  
MARC Leader: 00000cam  2200361 a 4500  
Author: Walker, Sally M.  
Title: Put inclined planes to the test / by Sally M. Walker and Roseann Feldmann.  
Publication Info.: Minneapolis, MN : Lerner Publications Co., c2012.  
[more lines follow]  
