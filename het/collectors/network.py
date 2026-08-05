import socket
import psutil


def collect():

    hostname = socket.gethostname()


    try:
        ip = socket.gethostbyname(hostname)

    except:
        ip = "Unknown"


    connections = psutil.net_connections()


    return {

        "hostname":
        hostname,

        "ip_address":
        ip,

        "active_connections":
        len(connections)

    }