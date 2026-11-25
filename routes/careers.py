from flask import Blueprint, render_template, redirect, url_for, session

careers_bp = Blueprint("careers", __name__)

CYBERSECURITY_CAREERS = [
    {
        "id": "soc-analyst",
        "title": "SOC Analyst",
        "category": "Blue Team",
        "level": "Entry Level",
        "description": (
            "Monitors security alerts, reviews system and network logs, "
            "and investigates suspicious activity to identify potential threats."
        ),
        "skills": [
            "Log analysis",
            "Networking fundamentals",
            "SIEM fundamentals",
            "Incident triage",
        ],
        "learning_path": (
            "Start with networking, Linux, Windows logs, and cybersecurity "
            "fundamentals. Then practise alert investigation and log analysis."
        ),
    },
    {
        "id": "cybersecurity-analyst",
        "title": "Cybersecurity Analyst",
        "category": "Defensive Security",
        "level": "Entry Level",
        "description": (
            "Assesses security risks, investigates suspicious events, "
            "and helps organisations improve their security controls."
        ),
        "skills": [
            "Threat identification",
            "Security monitoring",
            "Risk assessment",
            "Security documentation",
        ],
        "learning_path": (
            "Build knowledge of operating systems, networking, security "
            "principles, vulnerabilities, and incident investigation."
        ),
    },
    {
        "id": "penetration-tester",
        "title": "Penetration Tester",
        "category": "Red Team",
        "level": "Beginner to Advanced",
        "description": (
            "Tests authorised systems and applications to identify "
            "security weaknesses and explain how they can be corrected."
        ),
        "skills": [
            "Networking and Linux",
            "Web application security",
            "Scripting",
            "Vulnerability assessment",
        ],
        "learning_path": (
            "Learn networking, Linux, Python, and web technologies first. "
            "Practise only in authorised labs before progressing to structured penetration testing."
        ),
    },
    {
        "id": "security-engineer",
        "title": "Security Engineer",
        "category": "Security Engineering",
        "level": "Intermediate",
        "description": (
            "Designs, implements, and maintains security controls that "
            "protect an organisation's systems, networks, and information."
        ),
        "skills": [
            "Networking",
            "Operating systems",
            "Firewalls and access control",
            "Automation and troubleshooting",
        ],
        "learning_path": (
            "Build strong system and network administration skills, then "
            "learn security architecture, defensive tools, and automation."
        ),
    },
    {
        "id": "incident-responder",
        "title": "Incident Responder",
        "category": "Blue Team",
        "level": "Intermediate",
        "description": (
            "Investigates security incidents, determines their scope, "
            "supports containment and recovery, and documents lessons learned."
        ),
        "skills": [
            "Log analysis",
            "Incident handling",
            "Evidence preservation",
            "Clear technical reporting",
        ],
        "learning_path": (
            "Learn system logs, networking, security monitoring, and incident "
            "response procedures. Practise investigating simulated incidents."
        ),
    },
    {
        "id": "digital-forensics-investigator",
        "title": "Digital Forensics Investigator",
        "category": "Digital Forensics",
        "level": "Intermediate",
        "description": (
            "Examines digital evidence from computers, devices, and other "
            "sources to reconstruct events and support investigations."
        ),
        "skills": [
            "Evidence handling",
            "File systems and metadata",
            "Forensic timelines",
            "Investigation documentation",
        ],
        "learning_path": (
            "Study operating systems, file systems, networking, and evidence "
            "integrity before practising with forensic training datasets."
        ),
    },
    {
        "id": "application-security-engineer",
        "title": "Application Security Engineer",
        "category": "Application Security",
        "level": "Intermediate",
        "description": (
            "Helps development teams identify and prevent vulnerabilities "
            "through secure design, code reviews, and security testing."
        ),
        "skills": [
            "Programming",
            "Web application architecture",
            "Secure coding",
            "OWASP vulnerabilities",
        ],
        "learning_path": (
            "Learn programming, databases, HTTP, and web development. "
            "Then study secure coding and practise in web-security labs."
        ),
    },
    {
        "id": "cloud-security-engineer",
        "title": "Cloud Security Engineer",
        "category": "Cloud Security",
        "level": "Intermediate",
        "description": (
            "Protects cloud infrastructure, identities, applications, and "
            "data by configuring appropriate security controls."
        ),
        "skills": [
            "Cloud fundamentals",
            "Identity and access management",
            "Network security",
            "Monitoring and configuration security",
        ],
        "learning_path": (
            "Learn networking, Linux, virtualisation, and access control. "
            "Then study a cloud platform and practise in its approved learning environment."
        ),
    },
    {
        "id": "threat-intelligence-analyst",
        "title": "Threat Intelligence Analyst",
        "category": "Threat Intelligence",
        "level": "Intermediate",
        "description": (
            "Researches threat actors, attack techniques, and indicators "
            "to help security teams understand and anticipate threats."
        ),
        "skills": [
            "Research and analysis",
            "Threat intelligence sources",
            "MITRE ATT&CK",
            "Analytical reporting",
        ],
        "learning_path": (
            "Build security fundamentals, learn common attack techniques, "
            "and practise analysing public threat reports and intelligence sources."
        ),
    },
    {
        "id": "malware-analyst",
        "title": "Malware Analyst",
        "category": "Malware Analysis",
        "level": "Advanced",
        "description": (
            "Studies suspicious software to understand its behaviour, "
            "identify indicators, and support detection and response."
        ),
        "skills": [
            "Python and programming fundamentals",
            "Operating systems",
            "Static and dynamic analysis concepts",
            "Reverse-engineering fundamentals",
        ],
        "learning_path": (
            "Learn programming, operating systems, and system internals first. "
            "Progress through controlled malware-analysis training environments."
        ),
    },
    {
        "id": "security-architect",
        "title": "Security Architect",
        "category": "Security Architecture",
        "level": "Advanced",
        "description": (
            "Designs security architectures and safeguards that align with "
            "an organisation's technology, risks, and business requirements."
        ),
        "skills": [
            "Security architecture",
            "Network and cloud security",
            "Risk management",
            "Identity and access management",
        ],
        "learning_path": (
            "Gain broad experience in systems, networks, cloud, and security "
            "engineering before progressing to architecture and risk-based design."
        ),
    },
    {
        "id": "grc-analyst",
        "title": "GRC Analyst",
        "category": "Governance, Risk and Compliance",
        "level": "Entry Level to Intermediate",
        "description": (
            "Supports security policies, risk assessments, audits, and "
            "compliance activities to help organisations manage cybersecurity risk."
        ),
        "skills": [
            "Risk assessment",
            "Security policies",
            "Documentation",
            "Compliance frameworks",
        ],
        "learning_path": (
            "Learn cybersecurity fundamentals and risk concepts, then explore "
            "security frameworks, policy development, and audit documentation."
        ),
    },
    {
        "id": "purple-team-specialist",
        "title": "Purple Team Specialist",
        "category": "Purple Team",
        "level": "Advanced",
        "description": (
            "Connects offensive testing with defensive monitoring to help "
            "teams improve detection, response, and security coverage."
        ),
        "skills": [
            "Attack techniques",
            "Detection engineering",
            "Log analysis",
            "Collaborative testing",
        ],
        "learning_path": (
            "First understand both offensive security and defensive operations. "
            "Then practise mapping simulated attack behaviours to detection opportunities."
        ),
    },
]


@careers_bp.route("/careers")
def explore_careers():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    categories = sorted({
        career["category"] for career in CYBERSECURITY_CAREERS
    })

    return render_template(
        "careers.html",
        careers=CYBERSECURITY_CAREERS,
        categories=categories,
    )