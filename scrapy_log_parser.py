import sys
import json

data = {}
args = sys.argv

url_marker = 'DEBUG: Crawled (200) <GET '
ref_marker = '> (referer: '

def recurse(url, ref, data):
    if type(data) == type({}):
        if 'name' in data.keys() and data['name'] == ref:
            # data['contents'] = []
            content = {'name': url}
            data['contents'].append(content)
        if 'contents' in data.keys():
            for content in data['contents']:
                recurse(url, ref, content)
        else:
            data['name'] = url
            data['contents'] = []

if len(args) == 1:
    print 'usage: python ', args[0], ' [scrapy logfile (DEBUG level)]'

if len(args) > 1:
    for arg in args[1:]:
        with open(arg) as input_file:
            for line in input_file:
                if url_marker in line and ref_marker in line:
                    url = line.split(url_marker)[1].split('>')[0]
                    ref = line.split(ref_marker)[1].split(')')[0]
                    recurse(url, ref, data)
        filename = arg.split('.log')[0] + '_data.json'
        with open(filename, 'w') as output_file:
            output_file.write(json.dumps(data))
