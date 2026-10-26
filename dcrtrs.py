"""HTML module."""

from http.server import BaseHTTPRequestHandler, HTTPServer


def wrap(tag):
    """Wrap content with some tag."""

    def wrap(fn):
        def wrap(*args):
            body = fn(*args)
            bodyHandled = map(lambda str: (" " * 2) + str, body.split("\n"))

            return f"<{tag}>\n{'\n'.join(bodyHandled)}\n</{tag}>"

        return wrap

    return wrap


@wrap("html")
@wrap("body")
@wrap("div")
def render(pattern, data):
    """Render data."""
    return pattern.format(**data)


class HTMLServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(render("{body}", {"body": "contents"}).encode("utf8"))
        # self.wfile.close()


try:
    server = HTTPServer(("", 8000), HTMLServer)
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
