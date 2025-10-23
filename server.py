from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class BankingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Welcome to Pure Python Bank!"}).encode())
        else:
            self.send_error(404, "Endpoint not found")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        if self.path == "/login":
            # Placeholder logic
            if data.get("username") == "admin" and data.get("password") == "pass":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode())
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(json.dumps({"status": "unauthorized"}).encode())
        else:
            self.send_error(404, "Endpoint not found")

def run():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, BankingHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()