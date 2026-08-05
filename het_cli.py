import argparse
import os
import webbrowser


from het.core.scanner import run_scan as run_scan_engine



VERSION = "4.5"



def banner():

    print("""
====================================
       HET v4.5

 Host Enumeration Tool

 Windows Security Assessment
====================================
""")


def scan():

    banner()

    print("[+] Starting HET Scan\n")

    run_scan_engine()



def report():

    report_file = (
        "reports/HET_Report.html"
    )


    if os.path.exists(report_file):

        print(
            "[+] Opening HET Report..."
        )

        webbrowser.open(
            os.path.abspath(report_file)
        )


    else:

        print(
            "[!] No report found."
        )

        print(
            "Run: het scan first"
        )



def modules():

    print("""
====================================
        HET Modules
====================================


Collectors:

 ✓ Host Information
 ✓ Hardware Information
 ✓ Network Information
 ✓ User Audit
 ✓ Process Enumeration
 ✓ Service Enumeration
 ✓ Startup Programs


Security:

 ✓ Firewall Audit
 ✓ Defender Check
 ✓ Update Checker
 ✓ IOC Scanner


Analysis:

 ✓ Risk Score
 ✓ Recommendations


Reports:

 ✓ JSON Report
 ✓ HTML Report
 ✓ PDF Report

====================================
""")



def info():

    print("""
====================================
HET - Host Enumeration Tool

Version:
4.5

Platform:
Windows

Purpose:
Security Assessment
Host Enumeration
System Auditing

====================================
""")



def version():

    print(f"""
HET - Host Enumeration Tool

Version:
{VERSION}

Platform:
Windows
""")



def main_cli():


    parser = argparse.ArgumentParser(

        prog="het",

        description=
        "Host Enumeration Tool"

    )


    parser.add_argument(

        "command",

        nargs="?"

    )


    args = parser.parse_args()



    if args.command == "scan":

        scan()


    elif args.command == "report":

        report()


    elif args.command == "modules":

        modules()


    elif args.command == "info":

        info()


    elif args.command == "version":

        version()


    else:

        parser.print_help()



if __name__ == "__main__":

    main_cli()