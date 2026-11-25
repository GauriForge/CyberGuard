# ========================================
# CyberGuard - Attack Category Data
# ========================================

CATEGORIES = {

    # 1. Social Engineering
    "social-engineering": {
        "name": "Social Engineering",
        "description": (
            "Social engineering attacks manipulate people into revealing "
            "information, granting access, or performing actions that "
            "compromise security."
        ),
        "topics": [
            "Impersonation",
            "Pretexting",
            "Tailgating / Piggybacking",
            "Shoulder Surfing",
            "Eavesdropping",
            "Dumpster Diving",
            "Quid Pro Quo",
            "Baiting",
            "Scare Tactics / Intimidation",
            "Phishing",
            "Email Spoofing",
            "Fake Websites",
            "Malicious Pop-ups",
            "Malicious Links",
            "Fake Login Pages",
            "Tech Support Scam",
            "Business Email Compromise (BEC)",
            "Social Media Scams"
        ]
    },

    # 2. Phishing & Phishing Variants
    "phishing-variants": {
        "name": "Phishing & Phishing Variants",
        "description": (
            "Phishing attacks use deceptive communications, websites, "
            "and messages to trick users into revealing sensitive information."
        ),
        "topics": [
            "Phishing",
            "Email Phishing",
            "Spear Phishing",
            "Whaling",
            "Smishing",
            "Vishing",
            "Clone Phishing",
            "Pharming",
            "QR Phishing / Quishing",
            "Angler Phishing",
            "Search Engine Phishing"
        ]
    },

    # 3. Password & Credential Attacks
    "password-credential-attacks": {
        "name": "Password & Credential Attacks",
        "description": (
            "These attacks target passwords and authentication credentials "
            "through guessing, cracking, theft, or abuse."
        ),
        "topics": [
            "Brute Force Attack",
            "Dictionary Attack",
            "Password Spraying",
            "Credential Stuffing",
            "Rainbow Table Attack",
            "Password Cracking",
            "Default Password Attack",
            "Credential Theft",
            "Credential Harvesting",
            "MFA Fatigue / MFA Push Bombing",
            "Pass-the-Hash",
            "Pass-the-Ticket"
        ]
    },

    # 4. Malware
    "malware": {
        "name": "Malware",
        "description": (
            "Malware is malicious software designed to damage systems, "
            "steal information, gain unauthorized access, or disrupt operations."
        ),
        "topics": [
            "Computer Virus",
            "Worm",
            "Trojan",
            "Ransomware",
            "Spyware",
            "Adware",
            "Rootkit",
            "Botnet",
            "Remote Access Trojan (RAT)",
            "Keylogger",
            "Fileless Malware",
            "Bootkit",
            "Scareware",
            "Cryptojacking Malware",
            "Wiper Malware"
        ]
    },

    # 5. Spyware & Surveillance
    "spyware-surveillance": {
        "name": "Spyware & Surveillance",
        "description": (
            "Spyware and surveillance attacks secretly monitor users, "
            "devices, applications, or sensitive activities."
        ),
        "topics": [
            "Tracking Spyware",
            "System Monitoring Spyware",
            "Banking Spyware",
            "Keylogging Spyware",
            "Browser Spyware",
            "Mobile Spyware"
        ]
    },

    # 6. Network Attacks
    "network-attacks": {
        "name": "Network Attacks",
        "description": (
            "Network attacks target network communication, protocols, "
            "traffic, devices, and infrastructure."
        ),
        "topics": [
            "Man-in-the-Middle (MITM)",
            "Denial-of-Service (DoS)",
            "Distributed Denial-of-Service (DDoS)",
            "Packet Sniffing",
            "Network Eavesdropping",
            "ARP Spoofing",
            "DNS Spoofing",
            "IP Spoofing",
            "DHCP Spoofing",
            "MAC Spoofing",
            "TCP SYN Flood",
            "DNS Cache Poisoning",
            "Network Scanning / Reconnaissance"
        ]
    },

    # 7. Wireless Attacks
    "wireless-attacks": {
        "name": "Wireless Attacks",
        "description": (
            "Wireless attacks target Wi-Fi, Bluetooth, wireless "
            "communication, and wireless network infrastructure."
        ),
        "topics": [
            "Evil Twin Attack",
            "Rogue Access Point",
            "Wi-Fi Eavesdropping",
            "Wi-Fi Deauthentication",
            "Wi-Fi Password Cracking",
            "Wireless Jamming",
            "Bluetooth Attacks"
        ]
    },

    # 8. Web & Application Attacks
    "web-application-attacks": {
        "name": "Web & Application Attacks",
        "description": (
            "These attacks exploit weaknesses in websites, web applications, "
            "servers, and application logic."
        ),
        "topics": [
            "SQL Injection",
            "Cross-Site Scripting (XSS)",
            "Cross-Site Request Forgery (CSRF)",
            "Server-Side Request Forgery (SSRF)",
            "Command Injection",
            "Path Traversal",
            "File Inclusion",
            "Remote Code Execution (RCE)",
            "Clickjacking",
            "Insecure Deserialization",
            "HTTP Request Smuggling",
            "XML External Entity (XXE)",
            "Server-Side Template Injection (SSTI)"
        ]
    },

    # 9. Identity, Access & Session Attacks
    "identity-access-session": {
        "name": "Identity, Access & Session Attacks",
        "description": (
            "These attacks target authentication, authorization, identities, "
            "sessions, tokens, and access controls."
        ),
        "topics": [
            "Identity Theft",
            "Account Takeover",
            "Session Hijacking",
            "Session Fixation",
            "Privilege Escalation",
            "Access Control Bypass",
            "Token Theft",
            "Authentication Bypass",
            "Credential Reuse",
            "MFA Bypass"
        ]
    },

    # 10. Data & Information Attacks
    "data-information-attacks": {
        "name": "Data & Information Attacks",
        "description": (
            "These attacks involve unauthorized access, disclosure, theft, "
            "manipulation, leakage, or destruction of information."
        ),
        "topics": [
            "Data Breach",
            "Data Exfiltration",
            "Data Leakage",
            "Information Disclosure",
            "Database Theft",
            "Data Manipulation",
            "Data Destruction",
            "DNS Information Leakage"
        ]
    },

    # 11. Insider & Supply-Chain Attacks
    "insider-supply-chain": {
        "name": "Insider & Supply-Chain Attacks",
        "description": (
            "These attacks involve malicious or compromised insiders, "
            "third parties, dependencies, vendors, and software supply chains."
        ),
        "topics": [
            "Malicious Insider",
            "Negligent Insider",
            "Compromised Insider Account",
            "Supply Chain Attack",
            "Third-Party Compromise",
            "Software Supply Chain Attack",
            "Dependency Confusion",
            "Malicious Software Update"
        ]
    },

    # 12. Physical & Device-Based Attacks
    "physical-device-attacks": {
        "name": "Physical & Device-Based Attacks",
        "description": (
            "These attacks exploit physical access, devices, hardware, "
            "removable media, and physical security weaknesses."
        ),
        "topics": [
            "Malicious USB / USB Drop Attack",
            "Device Theft",
            "Hardware Keylogging",
            "Evil Maid Attack",
            "Physical Tampering",
            "Skimming",
            "Card Cloning"
        ]
    },

    # 13. Mobile & IoT Attacks
    "mobile-iot-attacks": {
        "name": "Mobile & IoT Attacks",
        "description": (
            "These attacks target smartphones, mobile applications, SIM cards, "
            "IoT devices, and connected systems."
        ),
        "topics": [
            "Mobile Malware",
            "SIM Swapping",
            "Malicious Mobile Applications",
            "Mobile Phishing",
            "IoT Malware",
            "IoT Device Hijacking",
            "IoT Botnet Attacks",
            "IoT Credential Attacks"
        ]
    },

    # 14. Availability & Resource Attacks
    "availability-resource-attacks": {
        "name": "Availability & Resource Attacks",
        "description": (
            "These attacks consume system or network resources and disrupt "
            "the availability of services and applications."
        ),
        "topics": [
            "DoS",
            "DDoS",
            "SYN Flood",
            "UDP Flood",
            "HTTP Flood",
            "Resource Exhaustion",
            "Application-Layer DoS"
        ]
    }

}