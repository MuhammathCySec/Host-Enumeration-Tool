import subprocess


def collect():

    data = {}

    try:

        result = subprocess.check_output(
            "netsh advfirewall show allprofiles",
            shell=True,
            text=True
        )

        data["firewall_status"] = result


    except Exception as e:

        data["error"] = str(e)


    return data