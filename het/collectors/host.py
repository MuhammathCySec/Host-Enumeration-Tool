import platform
import socket
import getpass
import psutil
from datetime import datetime


def collect():

    return {

        "computer_name":
        socket.gethostname(),

        "username":
        getpass.getuser(),

        "operating_system":
        platform.system(),

        "windows_version":
        platform.version(),

        "architecture":
        platform.architecture()[0],

        "processor":
        platform.processor(),

        "boot_time":
        datetime.fromtimestamp(
            psutil.boot_time()
        ).strftime("%Y-%m-%d %H:%M:%S")

    }