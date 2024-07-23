import network

from external.micropyserver import MicroPyServer
from external import utils

class HTTP_Server:
    def __init__(self):
        self._server = MicroPyServer()

        # Static files routes
        self._server.add_route("/", self._index_handler)
        self._server.add_route("/burgtor.css", self._index_css_handler)
        self._server.add_route("/burgtor.js", self._index_js_handler)

        # Open door route
        self._server.add_route("/open-door", self._open_door_handler, method="POST")

        # Read files
        self._filecontents = {}
        for filename in ["burgtor.html", "burgtor.css", "burgtor.js"]:
            with open(f"/Captive_Portal/{filename}", "r") as f:
                self._filecontents[filename] = f.read()

    def _index_handler(self, request):
        utils.send_response(self._server, self._filecontents["burgtor.html"])

    def _index_css_handler(self, request):
        utils.send_response(self._server, self._filecontents["burgtor.css"], content_type="text/css")

    def _index_js_handler(self, request):
        utils.send_response(self._server, self._filecontents["burgtor.js"], content_type="text/js")

    def _open_door_handler(self, request):
        # TODO
        utils.send_response(self._server, "", http_code=204)

    def start(self):
        self._server.start()

def main():
    # Open an access point
    network.hostname("burgtor")

    print("Creating a Hot Spot")
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    with open("/WIFI_SECRET", "r") as f:
        password = f.readline().split("\n")[0]

    print("You can connect with SSID 'Burgtor' and Password '" + password + "'")
    ap.config(essid="Burgtor", password=password)

    # Start the HTTP-Server
    http_server = HTTP_Server()
    http_server.start()

if __name__ == "__main__":
    main()
