import json
import os
from datetime import datetime


def generate(data):

    os.makedirs(
        "reports",
        exist_ok=True
    )


    filename = (
        "reports/"
        "HET_Report_"
        +
        datetime.now()
        .strftime("%Y%m%d_%H%M%S")
        +
        ".json"
    )


    with open(filename,"w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


    return filename