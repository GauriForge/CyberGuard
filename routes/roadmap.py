from flask import Blueprint, render_template, redirect, url_for, session

roadmap_bp = Blueprint("roadmap", __name__)

CYBERSECURITY_ROADMAP = [
    {
        "id": 1,
        "title": "Computer Fundamentals",
        "level": "Beginner",
        "duration": "1–2 weeks",
        "description": "Understand how computers work before moving into networking and security.",
        "topics": [
            "Computer hardware and software",
            "CPU, RAM, storage and file systems",
            "Operating system fundamentals",
            "Files, folders, processes and services",
            "Command-line basics",
        ],
        "tasks": [
            "Identify your computer's operating system and system specifications.",
            "Create, move, copy and manage files using the command line.",
            "Explore running processes and installed applications.",
        ],
        "milestone": "Explain the basic components of a computer and how an operating system manages them.",
        "resources": [
            {
                "title": "GCFGlobal Computer Basics",
                "url": "https://edu.gcfglobal.org/en/computerbasics/",
            },
        ],
    },
    {
        "id": 2,
        "title": "Networking Fundamentals",
        "level": "Beginner",
        "duration": "2–3 weeks",
        "description": "Learn how computers communicate across local networks and the internet.",
        "topics": [
            "Network types: LAN, WAN and the internet",
            "IP addresses, subnet masks and gateways",
            "MAC addresses and ARP",
            "TCP/IP and the OSI model",
            "Ports and common protocols",
            "DNS, DHCP, HTTP and HTTPS",
            "Routers, switches and firewalls",
        ],
        "tasks": [
            "Use ipconfig or ip addr to inspect network settings.",
            "Use ping and nslookup to investigate connectivity and DNS.",
            "Identify common ports such as 22, 53, 80, 443 and 3389.",
        ],
        "milestone": "Explain how a browser request travels from your computer to a website.",
        "resources": [
            {
                "title": "Cisco Networking Basics",
                "url": "https://www.netacad.com/catalogs/learn/networking-basics",
            },
            {
                "title": "Cloudflare: What Is a Computer Network?",
                "url": "https://www.cloudflare.com/learning/network-layer/what-is-a-computer-network/",
            },
        ],
    },
    {
        "id": 3,
        "title": "Operating Systems and Linux",
        "level": "Beginner",
        "duration": "2–3 weeks",
        "description": "Develop practical familiarity with Linux and Windows, especially permissions, processes and system administration.",
        "topics": [
            "Linux distributions and the filesystem",
            "Navigation and file-management commands",
            "Users, groups and file permissions",
            "Processes, services and package management",
            "Windows users, services and Event Viewer",
            "Environment variables and shell basics",
        ],
        "tasks": [
            "Practise pwd, ls, cd, cat, grep, find and chmod in a safe environment.",
            "Create files and directories and inspect their permissions.",
            "Explore Windows Event Viewer or Linux system logs.",
        ],
        "milestone": "Navigate a Linux terminal, manage basic permissions and locate system logs.",
        "resources": [
            {
                "title": "Linux Journey",
                "url": "https://linuxjourney.com/",
            },
            {
                "title": "Ubuntu Command-Line Tutorials",
                "url": "https://ubuntu.com/tutorials/command-line-for-beginners",
            },
        ],
    },
    {
        "id": 4,
        "title": "Programming and Scripting",
        "level": "Beginner",
        "duration": "3–4 weeks",
        "description": "Learn enough programming to automate repetitive work and understand security tools.",
        "topics": [
            "Python variables and data types",
            "Conditions, loops and functions",
            "Lists, dictionaries and sets",
            "File handling and exception handling",
            "Regular expressions and JSON",
            "Basic Bash and PowerShell scripting",
        ],
        "tasks": [
            "Write a Python program that reads a text file.",
            "Build a simple log parser that counts repeated events.",
            "Create a script that checks a list of values and reports results.",
        ],
        "milestone": "Build a small Python utility and explain how it works.",
        "resources": [
            {
                "title": "Python Official Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
            },
            {
                "title": "PowerShell Documentation",
                "url": "https://learn.microsoft.com/en-us/powershell/",
            },
        ],
    },
    {
        "id": 5,
        "title": "Web Technologies and Databases",
        "level": "Beginner to Intermediate",
        "duration": "2–3 weeks",
        "description": "Understand websites, web servers and databases before studying web application vulnerabilities.",
        "topics": [
            "HTML, CSS and JavaScript fundamentals",
            "Client-server architecture",
            "HTTP requests, responses and headers",
            "Cookies, sessions and authentication",
            "SQL queries and database basics",
            "APIs and JSON",
        ],
        "tasks": [
            "Inspect request and response headers in browser developer tools.",
            "Create a basic webpage and connect it to a simple database in a practice project.",
            "Practise SELECT, INSERT, UPDATE and DELETE using sample data.",
        ],
        "milestone": "Explain how a web application communicates with a server and database.",
        "resources": [
            {
                "title": "MDN Web Docs",
                "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development",
            },
            {
                "title": "SQLBolt Interactive SQL Lessons",
                "url": "https://sqlbolt.com/",
            },
        ],
    },
    {
        "id": 6,
        "title": "Cybersecurity Fundamentals",
        "level": "Beginner",
        "duration": "2 weeks",
        "description": "Learn core security principles, common threats and the controls used to reduce risk.",
        "topics": [
            "Confidentiality, integrity and availability",
            "Threats, vulnerabilities and risk",
            "Authentication and access control",
            "Least privilege and defence in depth",
            "Encryption, hashing and digital signatures",
            "Social engineering and phishing",
            "Security policies and awareness",
        ],
        "tasks": [
            "Classify sample scenarios as threats, vulnerabilities or risks.",
            "Compare hashing with encryption.",
            "Create a checklist for securing a personal account.",
        ],
        "milestone": "Explain basic security principles and recommend suitable protective controls.",
        "resources": [
            {
                "title": "Cisco Introduction to Cybersecurity",
                "url": "https://www.netacad.com/courses/introduction-to-cybersecurity",
            },
            {
                "title": "CISA Cybersecurity Best Practices",
                "url": "https://www.cisa.gov/topics/cybersecurity-best-practices",
            },
        ],
    },
    {
        "id": 7,
        "title": "Security Tools and Practical Labs",
        "level": "Beginner to Intermediate",
        "duration": "Ongoing",
        "description": "Practise using common security tools in authorised labs and controlled environments.",
        "topics": [
            "Virtual machines and isolated lab environments",
            "Wireshark packet analysis",
            "Nmap basics and service discovery",
            "Linux security utilities",
            "Log inspection and basic analysis",
            "Safe handling of suspicious files",
        ],
        "tasks": [
            "Set up a virtual machine or an approved browser-based lab.",
            "Inspect a sample packet capture in Wireshark.",
            "Practise service discovery only on systems you own or have permission to test.",
        ],
        "milestone": "Complete a guided lab and document the objective, steps and findings.",
        "resources": [
            {
                "title": "TryHackMe",
                "url": "https://tryhackme.com/",
            },
            {
                "title": "Wireshark Documentation",
                "url": "https://www.wireshark.org/docs/",
            },
            {
                "title": "Nmap Reference Guide",
                "url": "https://nmap.org/book/man.html",
            },
        ],
    },
    {
        "id": 8,
        "title": "Network Security",
        "level": "Intermediate",
        "duration": "2–3 weeks",
        "description": "Understand network-based attacks and the defensive controls used to detect and prevent them.",
        "topics": [
            "Firewall rules and network segmentation",
            "Secure protocols and encrypted traffic",
            "Packet analysis and suspicious connections",
            "Common network attacks and their indicators",
            "IDS and IPS fundamentals",
            "VPNs and secure remote access",
        ],
        "tasks": [
            "Analyse a sample network capture for unusual connections.",
            "Draw a small network diagram with security boundaries.",
            "Recommend controls for a fictional network incident.",
        ],
        "milestone": "Identify basic network risks and explain how layered defences reduce them.",
        "resources": [
            {
                "title": "Cisco Networking Academy",
                "url": "https://www.netacad.com/",
            },
            {
                "title": "Cloudflare Learning Center",
                "url": "https://www.cloudflare.com/learning/",
            },
        ],
    },
    {
        "id": 9,
        "title": "Web Application Security",
        "level": "Intermediate",
        "duration": "3–4 weeks",
        "description": "Study common web vulnerabilities, how they occur and how to prevent them.",
        "topics": [
            "Input validation and output encoding",
            "SQL injection and parameterised queries",
            "Cross-site scripting (XSS)",
            "Broken access control",
            "Authentication and session weaknesses",
            "Cross-site request forgery (CSRF)",
            "Security misconfiguration",
        ],
        "tasks": [
            "Complete beginner web-security exercises in an authorised lab.",
            "Review a sample application for common security weaknesses.",
            "Write a short report explaining a vulnerability and its mitigation.",
        ],
        "milestone": "Explain common web vulnerabilities and demonstrate their mitigations in a safe practice environment.",
        "resources": [
            {
                "title": "OWASP Top 10",
                "url": "https://owasp.org/www-project-top-ten/",
            },
            {
                "title": "PortSwigger Web Security Academy",
                "url": "https://portswigger.net/web-security",
            },
        ],
    },
    {
        "id": 10,
        "title": "Security Monitoring and Incident Response",
        "level": "Intermediate",
        "duration": "2–3 weeks",
        "description": "Learn how defenders detect suspicious activity, investigate alerts and respond to incidents.",
        "topics": [
            "System and authentication logs",
            "Indicators of compromise",
            "Alert triage and incident classification",
            "Evidence preservation",
            "Containment, eradication and recovery",
            "Incident documentation",
        ],
        "tasks": [
            "Analyse sample logs and identify suspicious events.",
            "Build a timeline for a fictional cyber incident.",
            "Write a basic incident report with findings and recommendations.",
        ],
        "milestone": "Investigate a fictional incident and present evidence-based conclusions.",
        "resources": [
            {
                "title": "CISA Cyber Threats and Advisories",
                "url": "https://www.cisa.gov/topics/cyber-threats-and-advisories",
            },
            {
                "title": "NIST Cybersecurity Resources",
                "url": "https://www.nist.gov/cybersecurity",
            },
        ],
    },
    {
        "id": 11,
        "title": "Digital Forensics and Threat Analysis",
        "level": "Intermediate to Advanced",
        "duration": "Ongoing",
        "description": "Develop skills in evidence handling, forensic reasoning and understanding attacker behaviour.",
        "topics": [
            "Evidence integrity and chain of custody",
            "File metadata and forensic timelines",
            "Basic disk and memory forensics concepts",
            "Malware behaviour and safe analysis principles",
            "Threat intelligence fundamentals",
            "MITRE ATT&CK framework",
        ],
        "tasks": [
            "Create an evidence log for a fictional investigation.",
            "Map observed behaviours from a sample incident to relevant MITRE ATT&CK techniques.",
            "Summarise findings without making unsupported conclusions.",
        ],
        "milestone": "Produce a structured investigation summary with evidence, timeline and limitations.",
        "resources": [
            {
                "title": "NIST Digital Forensics Publications",
                "url": "https://www.nist.gov/forensic-science",
            },
            {
                "title": "MITRE ATT&CK",
                "url": "https://attack.mitre.org/",
            },
        ],
    },
    {
        "id": 12,
        "title": "Advanced Practice and Specialisation",
        "level": "Intermediate to Advanced",
        "duration": "Ongoing",
        "description": "Build depth in a chosen security domain after establishing the core foundations.",
        "topics": [
            "Blue Team and security operations",
            "Penetration testing and Red Team fundamentals",
            "Application security",
            "Cloud security",
            "Digital forensics and incident response",
            "Governance, risk and compliance",
        ],
        "tasks": [
            "Choose one specialisation and complete a guided learning path.",
            "Build a project demonstrating a relevant security skill.",
            "Document your methodology, findings and defensive recommendations.",
        ],
        "milestone": "Complete a focused portfolio project and explain your technical decisions.",
        "resources": [
            {
                "title": "NIST Cybersecurity Framework",
                "url": "https://www.nist.gov/cyberframework",
            },
            {
                "title": "OWASP Projects",
                "url": "https://owasp.org/projects/",
            },
            {
                "title": "Cisco Networking Academy",
                "url": "https://www.netacad.com/",
            },
        ],
    },
    {
        "id": 13,
        "title": "Projects and Career Preparation",
        "level": "All Levels",
        "duration": "Ongoing",
        "description": "Turn your learning into demonstrable work and prepare for entry-level cybersecurity opportunities.",
        "topics": [
            "Practical cybersecurity projects",
            "Git and GitHub portfolio",
            "Technical reports and documentation",
            "Resume and interview preparation",
            "Certification planning",
            "Continuous learning and ethical practice",
        ],
        "tasks": [
            "Publish a well-documented project that contains no secrets or sensitive data.",
            "Write a report describing the problem, approach and outcome.",
            "Prepare to explain your projects and fundamental security concepts in an interview.",
        ],
        "milestone": "Present a portfolio of projects that demonstrates your skills and responsible practice.",
        "resources": [
            {
                "title": "GitHub Skills",
                "url": "https://skills.github.com/",
            },
            {
                "title": "Cisco Networking Academy",
                "url": "https://www.netacad.com/",
            },
        ],
    },
]

STUDY_TIPS = [
    "Follow the stages in order; networking and operating-system knowledge make later security topics easier.",
    "Practise regularly instead of only watching videos or reading notes.",
    "Keep notes of commands, concepts, mistakes and their solutions.",
    "Use only systems and labs you own or have explicit permission to test.",
    "Complete the practical tasks and milestone for each stage before moving forward.",
    "Revisit earlier topics whenever a later concept is unclear.",
]


@roadmap_bp.route("/roadmap")
def roadmap():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    return render_template(
        "roadmap.html",
        roadmap=CYBERSECURITY_ROADMAP,
        stages=CYBERSECURITY_ROADMAP,
        study_tips=STUDY_TIPS,
    )