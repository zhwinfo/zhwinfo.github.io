#!/usr/bin/env python3
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HOST = "0.0.0.0"
PORT = 5001

rooms_lock = threading.Lock()
rooms = {}  # room_id -> {"offer": dict or None, "answer": dict or None}

def get_room(room_id):
    with rooms_lock:
        if room_id not in rooms:
            rooms[room_id] = {"offer": None, "answer": None}
        return rooms[room_id]

def set_cors(handler):
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type")

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        set_cors(self)
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        path = parsed.path
        room_id = (qs.get("room", [""])[0]).strip()
        if path in ("/offer", "/answer", "/poll", "/status") and not room_id:
            self.send_response(400)
            set_cors(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "room required"}).encode("utf-8"))
            return

        if path == "/status":
            room = get_room(room_id)
            self.send_response(200)
            set_cors(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "hasOffer": bool(room["offer"]),
                "hasAnswer": bool(room["answer"])
            }).encode("utf-8"))
            return

        if path == "/poll":
            t = (qs.get("type", [""])[0]).strip()
            room = get_room(room_id)
            self.send_response(200)
            set_cors(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            if t == "offer" and room["offer"]:
                self.wfile.write(json.dumps(room["offer"]).encode("utf-8"))
            elif t == "answer" and room["answer"]:
                self.wfile.write(json.dumps(room["answer"]).encode("utf-8"))
            else:
                self.wfile.write(json.dumps({"ok": True, "empty": True}).encode("utf-8"))
            return

        self.send_response(404)
        set_cors(self)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "not found"}).encode("utf-8"))

    def do_POST(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        path = parsed.path
        room_id = (qs.get("room", [""])[0]).strip()
        if path in ("/offer", "/answer") and not room_id:
            self.send_response(400)
            set_cors(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "room required"}).encode("utf-8"))
            return

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length > 0 else b""
        try:
            body = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            body = {}

        if path == "/offer":
            if not body or "sdp" not in body or "type" not in body:
                self.send_response(400)
                set_cors(self)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "invalid offer"}).encode("utf-8"))
                return
            room = get_room(room_id)
            with rooms_lock:
                room["offer"] = body
                room["answer"] = None  # reset answer on new offer
            self.send_response(200)
            set_cors(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))
            return

        if path == "/answer":
            if not body or "sdp" not in body or "type" not in body:
                self.send_response(400)
                set_cors(self)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "invalid answer"}).encode("utf-8"))
                return
            room = get_room(room_id)
            with rooms_lock:
                room["answer"] = body
            self.send_response(200)
            set_cors(self)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))
            return

        self.send_response(404)
        set_cors(self)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "not found"}).encode("utf-8"))

def main():
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Signaling server listening on http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()

if __name__ == "__main__":
    main()

