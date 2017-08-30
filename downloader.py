# -*- coding: utf-8 -*-
import sys
from HTMLParser import HTMLParser
import urllib, urllib2, cookielib
import os, time
import xml.dom.minidom


def download(url):
    #print "downloading file: " + url
    #request = urllib2.Request(url, self.login_data, self.headers)
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)  
        downloaded = response.read()
    except Exception, e:
        print e
        downloaded = None
    return downloaded

url_base = 'http://www.malariastamps.com/exhibits/exhibits_images/'

download_list = [
    # (title, author, directory, num)
    ('Exclusive Uses of the 50 Cent Prexie', '50CentPrexieUsages', 11),
    ('Burma: The First Two Issues', 'Burma', 128),
    ("The 1991 'F' Tulip Stamps and Their First Day Covers", 'dewey_f', 160),
    ('Japan United States Treaty Issues of 1960', 'wynns_japan', 16),
    ('The 5c George Washington Regular Issue of 1962: Usage and Rates', 'SteveDavis', 16),
    ("Queen Victoria's Diamond Jubilee Issues of British Guiana", "John Wynns", 'wynns_ex6', 32),
    ("The Ramayana", "Eli Moallem", "EliMoallem", 16),
    ("Haiti's Date Tree Issue, 1891-1892 A Study & Plating Guide ", "Peter Jeannopoulos", "Jeannopoulos/HaitiTree18911892", 80),
    ("Haiti's Centennial Issue of 1903", "Peter Jeannopoulos", "Jeannopoulos/Hait1903Centennial", 16),
    ("Haiti's 1c Royal Palm of 1892", "Peter Jeannopoulos", "Jeannopoulos/HaitiRoyalPalm1892", 16),
    ("Haiti's Earliest Air Mail, 1921-1925", "Peter Jeannopoulos", "Jeannopoulos/HaitiAirmail19211925", 16),
    ("Haiti's 1902 Provisional Issue", "Peter Jeannopoulos", "Jeannopoulos/Haiti1902", 80),
    ("Haiti's 50 cent Nord Alexis Stamp of 1904", "Peter Jeannopoulos", "Jeannopoulos/Haiti50", 16),
    ("The Lion - Most Symbolic Animal of All", "Greg Balagian", "TheLion", 112),
    ("Registration System Of The Orange Free State, 1856-1899", "Tim Bartshe", "Bartshe_Reg", 16),
    ("Orange Free State, 1 Shilling Brown of 1896", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ("", "", "", ),
    ]


exhibits_page = 'http://aape.org/exhibits.asp'
d = download(exhibits_page)
open("exhibits.asp", 'w').write(d)


