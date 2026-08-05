import subprocess


def collect():

    startup = {}


    try:

        result = subprocess.check_output(
        'reg query "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"',
        shell=True,
        text=True
        )


        startup["startup_registry"] = result


    except:

        startup["startup_registry"] = "No startup entries"


    return startup