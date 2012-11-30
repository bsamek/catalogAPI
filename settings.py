"""This module contains general settings for logging into the catalog and
parsing the result of a query."""

USERNAME = '2405'
PASSWORD = '2405'
USERNAME_LABEL = "code"
PASSWORD_LABEL = "pin"
LOGIN_URL = 'https://library.minlib.net/patroninfo/'
LOGIN_SUCCESS = ("You are logged in as </font><font color=\"purple\" "
                 "size=\"+1\">STAFF</font><font color=\"purple\">")
BARCODE_URL = "http://library.minlib.net/search/b?SEARCH="
ACCOUNT_URL = "https://library.minlib.net/patroninfo~S1/1000030/top/"
