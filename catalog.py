"""This module provides a class Catalog, representing the OPAC.""" 

import urllib, urllib2, cookielib
import settings

class Catalog:
    """This class handles queries to the OPAC."""

    def __init__(self):
        self.loginurl = settings.URL
        self.credentials = {settings.USERNAME_LABEL: settings.USERNAME,
                settings.PASSWORD_LABEL: settings.PASSWORD}

        # Make the cookie jar
        self.cookies = cookielib.CookieJar()

        # Build URL opener
        self.opener = urllib2.build_opener(
                urllib2.HTTPRedirectHandler(),
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.HTTPCookieProcessor(self.cookies))

    def login(self):
        """Log into the OPAC."""

        # Open the page
        self.opener.open(self.loginurl)

        # Create request object
        request = urllib2.Request(self.loginurl, 
                urllib.urlencode(self.credentials))

        # Log in
        return self.opener.open(request)

    def search_barcode(self, barcode):
        """Search for item by barcode and return HTML."""
        pass

