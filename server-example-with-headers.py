#!/usr/bin/python3

from http import server

PORT = 8080


class CookieHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        if 'Host' in self.headers and \
                self.headers['Host'].startswith("localhost"):
            self.send_header('Set-Cookie', 'auth=1234; Domain=sub.localhost')

        self.end_headers()

        if 'Origin' in self.headers and \
                self.headers['Origin'].startswith('fadeevab.com'):
            self.wfile.write(b'I believe this request is from fadeevab.com!\n')

        self.wfile.write(b'Hello, world!\n')


httpd = server.HTTPServer(('127.0.0.1', PORT), CookieHandler)
httpd.serve_forever()
