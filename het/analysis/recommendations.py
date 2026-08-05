def generate(analysis):

    recommendations = []


    findings = analysis.get(
        "findings",
        []
    )


    for item in findings:


        if "Firewall" in item:

            recommendations.append(
                "Enable Windows Firewall"
            )


        if "Defender" in item:

            recommendations.append(
                "Enable Windows Defender protection"
            )


        if "startup" in item.lower():

            recommendations.append(
                "Review startup programs"
            )


        if "Suspicious" in item:

            recommendations.append(
                "Investigate suspicious files"
            )


    if not recommendations:

        recommendations.append(
            "System security looks good"
        )


    return recommendations