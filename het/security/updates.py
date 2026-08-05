import subprocess


def collect():

    data = {}


    try:

        result = subprocess.check_output(
            "powershell Get-HotFix",
            shell=True,
            text=True
        )


        data["installed_updates"] = result[:5000]


    except Exception as e:

        data["error"] = str(e)


    return data