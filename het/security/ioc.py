import os


def collect():

    suspicious_locations = [

        "C:\\Users\\Public",

        "C:\\Windows\\Temp",

        "C:\\Temp"

    ]


    findings = []

    errors = []


    for location in suspicious_locations:

        if os.path.exists(location):

            try:

                files = os.listdir(location)


                for file in files:

                    findings.append(
                        os.path.join(location, file)
                    )


            except PermissionError:

                errors.append(
                    f"Access denied: {location}"
                )


            except Exception as e:

                errors.append(
                    str(e)
                )


    return {

        "locations_checked":
        suspicious_locations,

        "findings":
        findings[:50],

        "errors":
        errors

    }