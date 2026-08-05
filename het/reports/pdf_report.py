from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet



def generate(data):


    filename = (
        "reports/HET_Report.pdf"
    )


    doc = SimpleDocTemplate(
        filename
    )


    styles = getSampleStyleSheet()


    content = []


    content.append(
        Paragraph(
            "HET - Host Enumeration Tool",
            styles["Title"]
        )
    )


    content.append(
        Spacer(1,20)
    )


    analysis = data.get(
        "security_analysis",
        {}
    )


    content.append(
        Paragraph(
            f"""
Security Score:
{analysis.get('security_score')}/100

Risk Level:
{analysis.get('risk_level')}
""",
            styles["Normal"]
        )
    )


    content.append(
        Spacer(1,20)
    )


    content.append(
        Paragraph(
            "Findings:",
            styles["Heading2"]
        )
    )


    for item in analysis.get(
        "findings",
        []
    ):

        content.append(
            Paragraph(
                item,
                styles["Normal"]
            )
        )


    doc.build(content)


    return filename