Scrapy-Log-Parser
=================

Command line script to extract then visualize spider tracks from scrapy logs


usage:
    `python scrapy_log_parser.py scrapy_debug.log (log level DEBUG)`

output:
    `scrapy_debug_data.json`

in tree.html, change filename:
    `d3.json("/scrapy_debug_data.json")`

use `python -m "SimpleHTTPServer"` for the ajax to work.

pull requests are welcome!
