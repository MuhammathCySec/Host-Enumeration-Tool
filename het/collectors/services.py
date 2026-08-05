import subprocess


def collect():

    try:

        services = subprocess.check_output(
            "sc query state= all",
            shell=True,
            text=True
        )


        return {

            "windows_services":
            services[:8000]

        }


    except Exception as e:

        return {

            "error":
            str(e)

        }