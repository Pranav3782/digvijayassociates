import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(__file__), "www.digvijayassociates.com")

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def guess_type(self, path):
        # Ensure ASPX and HTML files are served with proper HTML mime type
        lower_path = path.lower()
        if lower_path.endswith('.aspx') or lower_path.endswith('.aspx.html') or lower_path.endswith('.html') or lower_path.endswith('.htm'):
            return 'text/html; charset=utf-8'
        if lower_path.endswith('.css'):
            return 'text/css; charset=utf-8'
        if lower_path.endswith('.js'):
            return 'application/javascript; charset=utf-8'
        if lower_path.endswith('.axd'):
            return 'application/javascript; charset=utf-8'
        return super().guess_type(path)

    def translate_path(self, path):
        # Resolve path
        translated = super().translate_path(path)
        # If requested path does not exist, check if an .html or .aspx.html version exists
        if not os.path.exists(translated):
            if os.path.exists(translated + ".html"):
                return translated + ".html"
            if translated.endswith(".aspx") and os.path.exists(translated + ".html"):
                return translated + ".html"
        return translated

    def end_headers(self):
        # Add CORS and caching headers for seamless local development
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run():
    if not os.path.isdir(DIRECTORY):
        print(f"Error: Target directory '{DIRECTORY}' not found.")
        sys.exit(1)

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(" DIGVIJAY ASSOCIATES - LOCAL WEBSITE SERVER")
        print("=" * 60)
        print(f" Serving folder: {DIRECTORY}")
        print(f" Local URL:       {url}")
        print(f" Press Ctrl+C to stop the server.")
        print("=" * 60)
        
        # Automatically launch default browser
        import threading
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run()
