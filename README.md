Scrapy Log Parser
=================

Command line script to extract then visualize spider tracks from scrapy logs

![Screenshot](https://github.com/josefmonje/Scrapy-Log-Parser/blob/master/images/Screenshot.png "Screenshot")

Usage:

`python scrapy_log_parser.py scrapy_debug.log`

log level must be set to DEBUG


Output:

`scrapy_debug_data.json`


In tree.html, change filename:

`d3.json("/scrapy_debug_data.json")`


Use `python -m "SimpleHTTPServer"`

for the ajax to work


This is just a quick and dirty solution I wrote up in a few minutes to help me in my project so pull requests are welcome!


credits to [http://blog.pixelingene.com](http://blog.pixelingene.com/2011/07/building-a-tree-diagram-in-d3-js/) for the tree demo
