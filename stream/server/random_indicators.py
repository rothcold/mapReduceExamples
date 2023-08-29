#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
import random

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 9999  # Port to listen on (non-privileged ports are > 1023)

indicators = [
    {"name": "Temperature", "min": -20.0, "max": 50.0},
    {"name": "Humidity", "min": 0.0, "max": 100.0},
    {"name": "Power", "min": 0.0, "max": 20000.0},
]


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Listening {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                msg = ""
                for indicator in indicators:
                    value = (
                        random.random() * (indicator["max"] - indicator["min"])
                        + indicator["min"]
                    )
                    msg += "%s: %d\n" % (indicator["name"], value)
                conn.send(msg.encode())
                time.sleep(1)


if __name__ == "__main__":
    main()
