from het.collectors import host
from het.collectors import hardware
from het.collectors import network
from het.collectors import users
from het.collectors import processes
from het.collectors import services
from het.collectors import startup

from het.security import firewall
from het.security import defender
from het.security import updates
from het.security import ioc

from het.analysis import risk_score
from het.analysis import recommendations

from het.reports import html_report
from het.reports import report_manager



def run_scan():


    print("""
====================================
        HET v4.5

 Host Enumeration Tool

 Windows Edition
====================================
""")


    report = {}



    print("[+] Host Information")
    report["host"] = host.collect()



    print("[+] Hardware Information")
    report["hardware"] = hardware.collect()



    print("[+] Network Information")
    report["network"] = network.collect()



    print("[+] User Audit")
    report["users"] = users.collect()



    print("[+] Process Enumeration")
    report["processes"] = processes.collect()



    print("[+] Service Enumeration")
    report["services"] = services.collect()



    print("[+] Startup Programs")
    report["startup"] = startup.collect()



    print("[+] Firewall Audit")
    report["firewall"] = firewall.collect()



    print("[+] Defender Check")
    report["defender"] = defender.collect()



    print("[+] Update Check")
    report["updates"] = updates.collect()



    print("[+] IOC Scan")
    report["ioc"] = ioc.collect()




    print("[+] Running Security Analysis")



    analysis = risk_score.calculate(
        report
    )


    report["security_analysis"] = analysis




    report["recommendations"] = (
        recommendations.generate(
            analysis
        )
    )




    # ==============================
    # HTML REPORT GENERATION
    # ==============================


    print(
        "[+] Creating Report Folder"
    )



    report_folder = (
        report_manager.create_report_folder()
    )



    print(
        "[+] Creating HTML Report"
    )



    report_path = html_report.generate(
        report,
        report_folder
    )



    print(
    f"""

====================================
HET Report Generated Successfully

Report Location:

{report_path}

====================================

"""
    )



    print("""
====================================
HET Scan Completed Successfully
====================================

"""
    )



    return report