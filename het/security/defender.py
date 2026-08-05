import subprocess


def collect():

    data = {}


    try:

        result = subprocess.check_output(
            "powershell Get-MpComputerStatus",
            shell=True,
            text=True
        )


        data["defender_status"] = result


    except Exception as e:

        data["error"] = str(e)


    return data