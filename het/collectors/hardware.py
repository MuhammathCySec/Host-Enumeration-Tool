import psutil


def collect():

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("C:\\")


    return {

        "cpu_usage":
        f"{psutil.cpu_percent()}%",

        "cpu_cores":
        psutil.cpu_count(),

        "ram_total":
        f"{round(memory.total / (1024**3),2)} GB",

        "ram_used":
        f"{memory.percent}%",

        "disk_total":
        f"{round(disk.total / (1024**3),2)} GB",

        "disk_used":
        f"{disk.percent}%"

    }