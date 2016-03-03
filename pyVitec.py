from progress.bar import Bar
from _utils import *
import os

_name = "vitec"
_file = os.path.dirname(os.path.abspath(__file__)) + '/assest/url.txt'	

f = open(_file, 'r')

num_lines = sum(1 for line in f)
f.close()

# fucking, overcome data
f = open(_file, 'r')

_fs.mkdir(_name)

bar = Bar('Processing', max = num_lines)
for line in f:
	pathSave = os.path.join(_name, line.strip().split('/')[len(line.split('/')) - 1])
	# line is url content, but url redirect google site
	# HTTP Response 301
	_http.download(_http.get_redirected_url(line), pathSave)
	bar.next()
bar.finish()
f.close()
print 'Download complete!'
