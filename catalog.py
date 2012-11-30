"""This module provides a class Catalog, representing the OPAC.""" 

import urllib, urllib2, cookielib
import settings

class Catalog:
    """This class handles queries to the OPAC."""

    def __init__(self):
        """Init login URL, credentials, cookies, and URL opener."""

        # Login URL and settings
        self.loginurl = settings.LOGIN_URL
        self.credentials = {
                settings.USERNAME_LABEL: settings.USERNAME,
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

        # Check if already logged in
        self.is_logged_in()

        # Open the page
        self.opener.open(self.loginurl)

        # Create request object
        request = urllib2.Request(self.loginurl, 
                urllib.urlencode(self.credentials))

        # Log in
        return self.opener.open(request)

    def is_logged_in(self):
        """Check if logged in to catalog."""

        # Get account page
        page = self.opener.open(settings.ACCOUNT_URL).read()

        # Check account page text for login name
        return settings.LOGIN_SUCCESS in page

    def search_barcode(self, barcode):
        """Search for item by barcode and return HTML."""

        # Ensure you are logged in
        self.login()

        # Search for barcode
        page = self.opener.open(
                settings.BARCODE_URL + barcode).read()
        
        return page

