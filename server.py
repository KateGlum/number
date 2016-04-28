# -*- coding: utf-8 -*-
# !/usr/bin/env python

from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ('', 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print("serving at port")
httpd.serve_forever()