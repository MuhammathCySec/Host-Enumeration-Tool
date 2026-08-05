import os
from datetime import datetime


def create_report_folder():

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    folder = os.path.join(
        "reports",
        timestamp
    )

    os.makedirs(
        folder,
        exist_ok=True
    )

    return folder