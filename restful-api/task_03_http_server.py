#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # ROOT ENDPOINT "/"
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
            return

        # "/data"
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "Holberton", "city": "San Francisco"}
            self.wfile.write(json.dumps(data).encode())
            return

        # "/status"
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # UNDEFINED ENDPOINTS
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Not Found")


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    server.serve_forever()

