from progress.bar import Bar
import urllib
import os
import urllib2

_name = "vitec"

def mkdir(_name):
	if os.path.exists(_name) == False:
		os.mkdir(_name)
		print "\nThe directory was created successfully."

def download(path, fileName):
	fileSave = os.path.join(_name, fileName)
	d = urllib.URLopener()
	d.retrieve(path, fileSave)
	

def get_redirected_url(url):
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    return request.url
	

f = open(os.path.dirname(os.path.abspath(__file__)) + '/assest/url.txt', 'r')

num_lines = sum(1 for line in f)
f.close()

# fucking async
f = open(os.path.dirname(os.path.abspath(__file__)) + '/assest/url.txt', 'r')

mkdir(_name)

bar = Bar('Processing', max = num_lines)
for line in f:
	# line is url content, but url redirect google site
	# HTTP Response 301
	download(get_redirected_url(line), line.strip().split('/')[len(line.split('/')) - 1])
	bar.next()
bar.finish()
print 'Download complete!'