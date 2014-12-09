Scrapy-Log-Parser
=================

Command line script to extract then visualize spider tracks from scrapy logs


Usage:

`python scrapy_log_parser.py scrapy_debug.log`
log level=DEBUG


Output:

`scrapy_debug_data.json`


In tree.html, change filename:

`d3.json("/scrapy_debug_data.json")`


Use `python -m "SimpleHTTPServer"`

for the ajax to work


Pull requests are welcome!
