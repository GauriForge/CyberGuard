from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    abort,
)

resources_bp = Blueprint("resources", __name__)


LEARNING_RESOURCES = [
    {
        "id": "networking-basics",
        "title": "Computer Networking Fundamentals",
        "category": "Networking",
        "level": "Beginner",
        "description": (
            "Learn about IP addresses, ports, protocols, DNS, HTTP and "
            "the fundamentals of network communication."
        ),
        "topics": [
            "IP addresses and ports",
            "TCP and UDP",
            "DNS and HTTP/HTTPS",
            "Network devices and firewalls",
        ],
        "url": "https://www.cloudflare.com/learning/network-layer/what-is-a-computer-network/",
    },
    {
        "id": "web-security",
        "title": "Web Application Security",
        "category": "Web Security",
        "level": "Intermediate",
        "description": (
            "Understand common web application vulnerabilities and "
            "secure development practices."
        ),
        "topics": [
            "Input validation",
            "Authentication and authorization",
            "Secure session management",
            "Common web vulnerabilities",
        ],
        "url": "https://owasp.org/www-project-top-ten/",
    },
    {
        "id": "security-fundamentals",
        "title": "Cybersecurity Fundamentals",
        "category": "Cybersecurity",
        "level": "Beginner",
        "description": (
            "Explore security principles, risk management and "
            "basic protective measures."
        ),
        "topics": [
            "Confidentiality, integrity and availability",
            "Threats and vulnerabilities",
            "Security controls",
            "Risk assessment",
        ],
        "url": "https://www.cisa.gov/topics/cybersecurity-best-practices",
    },
    {
        "id": "phishing-awareness",
        "title": "Phishing Awareness",
        "category": "Email Security",
        "level": "Beginner",
        "description": (
            "Learn to recognize deceptive messages, suspicious links "
            "and requests for sensitive information."
        ),
        "topics": [
            "Common phishing indicators",
            "Sender verification",
            "Suspicious links and attachments",
            "Reporting phishing attempts",
        ],
        "url": "https://www.cisa.gov/secure-our-world/recognize-and-report-phishing",
    },
    {
        "id": "cryptography",
        "title": "Cryptography Basics",
        "category": "Cryptography",
        "level": "Intermediate",
        "description": (
            "Study encryption, hashing, digital signatures and their "
            "roles in protecting information."
        ),
        "topics": [
            "Symmetric and asymmetric encryption",
            "Cryptographic hashing",
            "Digital signatures",
            "Key management",
        ],
        "url": "https://www.cloudflare.com/learning/ssl/what-is-encryption/",
    },
    {
        "id": "incident-response",
        "title": "Incident Response",
        "category": "Incident Management",
        "level": "Intermediate",
        "description": (
            "Understand how organizations prepare for, detect, respond "
            "to and recover from cybersecurity incidents."
        ),
        "topics": [
            "Preparation",
            "Detection and analysis",
            "Containment and recovery",
            "Lessons learned",
        ],
        "url": "https://www.cisa.gov/topics/cyber-threats-and-advisories",
    },
    {
        "id": "secure-passwords",
        "title": "Password and Account Security",
        "category": "Account Security",
        "level": "Beginner",
        "description": (
            "Learn safer password practices, multi-factor authentication "
            "and account recovery precautions."
        ),
        "topics": [
            "Unique passwords",
            "Password managers",
            "Multi-factor authentication",
            "Account recovery",
        ],
        "url": "https://www.cisa.gov/secure-our-world/use-strong-passwords",
    },
    {
        "id": "digital-forensics",
        "title": "Digital Forensics Fundamentals",
        "category": "Digital Forensics",
        "level": "Advanced",
        "description": (
            "Explore evidence preservation, forensic documentation "
            "and the importance of maintaining evidence integrity."
        ),
        "topics": [
            "Evidence preservation",
            "Documentation",
            "Chain of custody",
            "Forensic integrity",
        ],
        "url": "https://www.nist.gov/forensic-science",
    },
    {
        "id": "cisco-intro-cybersecurity",
        "title": "Introduction to Cybersecurity — Cisco",
        "category": "Cybersecurity",
        "level": "Beginner",
        "description": (
            "Learn cybersecurity fundamentals, common threats, "
            "and ways to protect digital information."
        ),
        "topics": [
            "Cybersecurity fundamentals",
            "Common cyber threats",
            "Personal and organizational security",
        ],
        "url": "https://www.netacad.com/courses/introduction-to-cybersecurity",
    },
    {
        "id": "cisco-networking-basics",
        "title": "Networking Basics — Cisco",
        "category": "Networking",
        "level": "Beginner",
        "description": (
            "Learn how computer networks operate and understand "
            "basic networking concepts."
        ),
        "topics": [
            "Network fundamentals",
            "Network devices",
            "Basic network communication",
        ],
        "url": "https://www.netacad.com/catalogs/learn/networking-basics",
    },
    {
        "id": "tryhackme-cybersecurity",
        "title": "Hands-on Cybersecurity Training — TryHackMe",
        "category": "Cybersecurity",
        "level": "Beginner",
        "description": (
            "Practice cybersecurity through interactive rooms, guided "
            "learning paths, and practical exercises covering "
            "offensive and defensive security."
        ),
        "topics": [
            "Cybersecurity fundamentals",
            "Networking and Linux",
            "Security analysis",
            "Hands-on security exercises",
        ],
        "url": "https://tryhackme.com/",
    },
    {
        "id": "portswigger-web-security",
        "title": "Web Security Academy — PortSwigger",
        "category": "Web Security",
        "level": "Intermediate",
        "description": (
            "Study web application vulnerabilities and practise "
            "in free, interactive security labs."
        ),
        "topics": [
            "SQL injection",
            "Cross-site scripting",
            "Authentication vulnerabilities",
            "Web application security testing",
        ],
        "url": "https://portswigger.net/web-security",
    },
]


def _get_resource(resource_id):
    return next(
        (
            resource
            for resource in LEARNING_RESOURCES
            if resource["id"] == resource_id
        ),
        None,
    )


def _get_categories():
    return sorted({
        resource["category"]
        for resource in LEARNING_RESOURCES
    })


@resources_bp.route("/resources", methods=["GET"])
def learning_resources():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    search_query = request.args.get("q", "").strip()
    selected_category = request.args.get("category", "").strip()
    query = search_query.casefold()

    resources = LEARNING_RESOURCES

    if query:
        resources = [
            resource
            for resource in resources
            if query in resource["title"].casefold()
            or query in resource["description"].casefold()
            or query in resource["category"].casefold()
            or query in resource["level"].casefold()
            or any(
                query in topic.casefold()
                for topic in resource["topics"]
            )
        ]

    if selected_category:
        resources = [
            resource
            for resource in resources
            if resource["category"] == selected_category
        ]

    return render_template(
        "resources.html",
        resources=resources,
        categories=_get_categories(),
        search_query=search_query,
        selected_category=selected_category,
        selected_resource=None,
    )


@resources_bp.route("/resources/<resource_id>", methods=["GET"])
def resource_detail(resource_id):
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    resource = _get_resource(resource_id)

    if resource is None:
        abort(404)

    return render_template(
        "resources.html",
        resources=LEARNING_RESOURCES,
        categories=_get_categories(),
        search_query="",
        selected_category="",
        selected_resource=resource,
    )