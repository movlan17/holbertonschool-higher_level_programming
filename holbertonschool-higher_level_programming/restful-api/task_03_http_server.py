#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests for different endpoints."""

        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
            return

        # /status endpoint
        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # Undefined endpoints → 404
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

