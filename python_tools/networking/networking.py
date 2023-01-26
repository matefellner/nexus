"""
tcp server
"""

import logging
import socket


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

# TCP Client
def download(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (server, port)
    logging.info(f"Connecting to: {server}:{port}")

    s.connect(address)
    logging.info("Connected")

    logging.info("Send")
    s.send(b"Hello\rn\n")

    logging.info("Recv")
    data = s.recv(1024)

    logging.info("Closing")
    s.close()

    logging.info(f"Data: {data}")


# TCP Server
def server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f"Bind: {ip}:{port}")
    s.bind(address)

    logging.info("Listening")
    s.listen(1)

    con, addr = s.accept()
    logging.info(f"Connected: {addr}")

    while True:
        data = con.recv(1024)
        if len(data) == 0:
            logging.info(f"Exiting")
            con.close()
            break
        logging.info(f"Data: {data}")

    logging.info("Closing the server")
    s.close()


# Check one port
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f"Checking {ip}:{port}")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        con = s.connect_ex((ip, port))
        logging.debug(f"Connection {ip}:{port} = {con}")
        s.close()

        if con == 0:
            ret = False
            logging.debug(f"In use {ip}:{port}")
        else:
            ret = True
            logging.debug(f"Usable {ip}:{port}")

    except Exception as ex:
        ret = False
        logging.debug(f"Error {ip}:{port} = {ex.msg}")
    finally:
        logging.debug(f"Returning {ip}:{port} = {ret}")
        return ret


# Checking a range
def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret


# see currently used ports:
# sudo lsof -i -P -n | grep LISTEN


def main():
    # download("voidrealms.com",80)
    # server("localhost", 2607)
    p = check_range("localhost", [2590, 2600])
    for k, v in p.items():
        logging.info(f"Port {k} = usable {v}")


if __name__ == "__main__":
    main()
