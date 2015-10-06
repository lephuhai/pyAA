import os
import requests
import urllib
import urllib2


def download(url, pathSave):
	d = urllib.URLopener()
	d.retrieve(url, pathSave)
	
def get_redirected_url(url):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url