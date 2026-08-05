import psutil


def collect():

    process_list = []


    for p in psutil.process_iter(
        [
            "pid",
            "name",
            "username"
        ]
    ):

        try:
            process_list.append(
                p.info
            )

        except:
            pass


    return {

        "total_processes":
        len(process_list),

        "processes":
        process_list[:30]

    }