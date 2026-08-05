import subprocess
import getpass


def collect():

    data = {}

    data["current_user"] = getpass.getuser()


    try:
        users = subprocess.check_output(
            "net user",
            shell=True,
            text=True
        )

        data["local_users"] = users

    except Exception as e:
        data["local_users"] = str(e)



    try:
        logged = subprocess.check_output(
            "query user",
            shell=True,
            text=True
        )

        data["logged_in_users"] = logged

    except:
        data["logged_in_users"] = "Not available"


    return data