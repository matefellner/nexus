"""
udp (user datagram protocol
"""

import logging
import socket
import time
import threading
import sys
import socket
import multiprocessing


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


# Socket
def make_socket(ip="localhost", port=2045, sender=False):
    proc = multiprocessing.current_process().name
    logging.info(f"{proc}: starting")
    address = (ip, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if sender:
        logging.info(f"{proc}: starting to send")
    else:
        logging.info(f"{proc}: binding to port")
        s.bind(address)

    with s:
        while True:
            if sender:
                logging.info(f"{proc}: sending...")
                s.sendto(b"Hello UDP", address)
                time.sleep(1)
            else:
                data, addr = s.recvfrom(1024)
                logging.info(f"{proc}: from {addr} = {data}")


def main():
    breadcaster = multiprocessing.Process(
        target=make_socket, kwargs={"sender": True}, daemon=True, name="Broadcaster"
    )
    listener = multiprocessing.Process(
        target=make_socket, kwargs={"sender": False}, daemon=True, name="Listener"
    )

    breadcaster.start()
    listener.start()

    timer = threading.Timer(5, sys.exit, [0])
    timer.start()


if __name__ == "__main__":
    main()
