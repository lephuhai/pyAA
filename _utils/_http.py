import os
import requests
import urllib
import urllib2
import mimetypes


def download(url, pathSave):
	d = urllib.URLopener()
	d.retrieve(url, pathSave)
	
def get_redirected_url(url):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url
    
def isFile(url):
	"""Return boolean, using check must be URL isFile or whatever"""
	if mimetypes.guess_type(url, strict=True)[0] == None:
		return False
	else:
		return True
