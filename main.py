from het.collectors import host
from het.collectors import hardware
from het.collectors import network
from het.reports import json_report


def main():

    print("""
====================================
       HET v1.0
 Host Enumeration Tool
 Windows Edition
====================================
""")


    print("[+] Collecting Host Information...")
    host_data = host.collect()


    print("[+] Collecting Hardware Information...")
    hardware_data = hardware.collect()


    print("[+] Collecting Network Information...")
    network_data = network.collect()


    report = {

        "host": host_data,
        "hardware": hardware_data,
        "network": network_data

    }


    print("[+] Generating JSON Report...")

    json_report.generate(report)


    print("""
====================================
 Scan Completed Successfully

 Report saved inside reports/
====================================
""")


if __name__ == "__main__":
    main()