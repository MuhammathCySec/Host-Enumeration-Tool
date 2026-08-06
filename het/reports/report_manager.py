import os
from datetime import datetime


def create_report_folder():

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    # Get HET project root
    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )


    reports_dir = os.path.join(
        base_dir,
        "reports"
    )


    folder = os.path.join(
        reports_dir,
        timestamp
    )


    os.makedirs(
        folder,
        exist_ok=True
    )


    return folder
