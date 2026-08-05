def calculate(report):

    score = 100

    findings = []


    # Firewall Check

    firewall = str(
        report.get("firewall", {})
    )


    if "OFF" in firewall.upper():

        score -= 20

        findings.append(
            "Windows Firewall is disabled"
        )

    else:

        findings.append(
            "Firewall appears enabled"
        )


    # Defender Check

    defender = str(
        report.get("defender", {})
    )


    if "False" in defender:

        score -= 20

        findings.append(
            "Windows Defender protection issue"
        )

    else:

        findings.append(
            "Windows Defender detected"
        )


    # Startup Check

    startup = str(
        report.get("startup", {})
    )


    if len(startup) > 500:

        score -= 10

        findings.append(
            "Multiple startup entries found"
        )


    # IOC Check

    ioc = report.get(
        "ioc",
        {}
    )


    if len(
        ioc.get("findings", [])
    ) > 10:

        score -= 20

        findings.append(
            "Suspicious files detected"
        )


    if score < 0:

        score = 0


    return {

        "security_score":
        score,

        "risk_level":
        get_level(score),

        "findings":
        findings

    }



def get_level(score):

    if score >= 80:

        return "LOW RISK"


    elif score >= 50:

        return "MEDIUM RISK"


    else:

        return "HIGH RISK"