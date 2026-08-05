# HET - Host Enumeration Tool

![HET Banner](docs/screenshots/het-banner.png)

## 🛡️ Project Introduction

**HET (Host Enumeration Tool)** is a Windows-based security assessment and host enumeration framework designed to collect system information, perform security checks, analyze risks, and generate professional security reports.

HET is built for cybersecurity students, security analysts, and blue-team enthusiasts to understand how security assessment tools work internally.

The tool performs automated host discovery, security auditing, IOC checking, risk scoring, and report generation through an easy-to-use command-line interface.

---

# 🚀 Features

## 🔎 Host Information Collection

HET collects detailed information about the target system:

- Operating System details
- Computer name
- Username information
- System uptime
- Hardware information
- CPU details
- RAM information
- Disk information


---

## 🌐 Network Enumeration

Network analysis includes:

- IP address information
- Network adapters
- Network configuration
- Basic connectivity information


---

## 👥 User Audit

Collects:

- Local users
- User account information
- Account status


---

## ⚙️ Process & Service Enumeration

HET analyzes:

- Running processes
- Process IDs
- Running services
- Startup programs


---

## 🔐 Security Audit

Security checks include:

- Windows Firewall status
- Microsoft Defender status
- Installed Windows updates
- Basic security configuration checks


---

## 🕵️ IOC Scanner

Basic Indicator of Compromise detection:

- Suspicious file locations
- Temporary directory analysis
- Potential suspicious artifacts


---

## 📊 Risk Assessment Engine

HET automatically calculates:

- Security score
- Risk level
- Security findings
- Recommendations


Example:


Security Score: 90/100

Risk Level:
LOW RISK

Recommendations:
✓ Firewall enabled
✓ Defender active
⚠ Review startup programs


---

## 📄 Professional Reports

HET generates:

- JSON Report
- HTML Security Dashboard
- PDF Security Report


Reports include:

- Scan timestamp
- Report ID
- System details
- Network information
- Security findings
- Recommendations


---

# 🖥️ Screenshots

## HET CLI Interface

![HET Scan](docs/screenshots/het-scan.png)


## Security Report Dashboard

![HTML Report](docs/screenshots/het-report.png)


## PDF Security Report

![PDF Report](docs/screenshots/het-pdf.png)


---

# 📥 Installation

## Requirements

- Windows 10 / Windows 11
- Python 3.10+
- Administrator privileges recommended


---

## Clone Repository

```bash
git clone https://github.com/MuhammathCySec/Host-Enumeration-Tool.git

cd Host-Enumeration-Tool
Install Dependencies
pip install -r requirements.txt
Install HET Command Line Tool
pip install -e .

Verify installation:

het version

Expected:

HET - Host Enumeration Tool

Version:
4.5

Platform:
Windows
⚡ Usage
Run Full Security Scan
het scan

HET will perform:

Host Enumeration
        |
        ↓
Security Audit
        |
        ↓
IOC Scan
        |
        ↓
Risk Analysis
        |
        ↓
Report Generation
Open Latest Report
het report

Opens:

reports/HET_Report.html
Show Available Modules
het modules

Displays:

Collectors
Security Modules
Analysis Engine
Report Generator
Show Tool Information
het info
Show Version
het version
🏗️ Architecture

HET follows a modular security framework design.

                    HET CLI

                      |

                      ↓

              Core Scanner Engine

                      |

        --------------------------------

        |              |               |

        ↓              ↓               ↓


   Collectors     Security        Analysis


        |              |               |

        ↓              ↓               ↓


 Host Data     Firewall        Risk Score

 Network       Defender        Recommendations

 Users         IOC


                      |

                      ↓


              Report Generator


        ----------------------------

        |            |             |

        ↓            ↓             ↓


       JSON        HTML          PDF

📂 Project Structure
Host-Enumeration-Tool/

│
├── het_cli.py
├── pyproject.toml
│
├── het/
│
│   ├── collectors/
│   │
│   ├── security/
│   │
│   ├── analysis/
│   │
│   ├── reports/
│   │
│   ├── core/
│   │
│   └── utils/
│
├── reports/
│
├── docs/
│
└── README.md
🛣️ Future Roadmap
HET v5.0
Plugin System

Allow users to create custom modules:

plugins/

├── malware_scanner.py

├── password_audit.py

└── custom_checks.py
HET v5.5

Additional security modules:

YARA malware scanning
Hash reputation checking
VirusTotal API integration
Event log analysis
Browser security analysis
HET v6.0

Multi-platform support:

Windows
Linux
macOS
HET v7.0

Enterprise features:

Central dashboard
Agent-based scanning
Network-wide assessment
SIEM integration
👨‍💻 Author
Muhammath

Cybersecurity Student | Blue Team Enthusiast

Interested in:

Security Operations (SOC)
Threat Detection
Host Analysis
Security Automation
⚠️ Disclaimer

HET is developed for educational purposes, authorized security assessments, and defensive security research only.

Do not use this tool on systems without proper permission.
