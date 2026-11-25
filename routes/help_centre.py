from flask import Blueprint, render_template, session, redirect, url_for

help_centre_bp = Blueprint("help_centre", __name__)


REPORTING_RESOURCES = [
    {
        "id": "cybercrime-portal",
        "title": "National Cyber Crime Reporting Portal",
        "category": "General Cybercrime Reporting",
        "description": (
            "The official Government of India portal for reporting online "
            "financial fraud, hacking, identity theft, social media crimes, "
            "cyberstalking, and other cyber offences. Complaints are handled "
            "by the relevant law enforcement agencies."
        ),
        "url": "https://cybercrime.gov.in/",
        "icon": "bi-shield-check",
        "button": "Report Cybercrime",
        "number": None,
    },
    {
        "id": "cyber-financial-helpline",
        "title": "National Cyber Financial Fraud Helpline",
        "category": "Urgent Financial Fraud Reporting",
        "description": (
            "Call this helpline immediately if money has been lost through "
            "UPI fraud, online banking fraud, card fraud, or another financial "
            "cyber scam. Prompt reporting can help authorities and participating "
            "financial institutions take action."
        ),
        "url": "https://cybercrime.gov.in/",
        "icon": "bi-telephone-fill",
        "button": "Open Official Portal",
        "number": "1930",
    },
    {
        "id": "report-suspect",
        "title": "Report Suspicious Cyber Identifiers",
        "category": "Suspicious Numbers, URLs and Accounts",
        "description": (
            "Report suspicious website URLs, phone numbers, email addresses, "
            "WhatsApp numbers, Telegram handles, SMS identifiers, and social "
            "media URLs that may be connected to cybercrime."
        ),
        "url": "https://cybercrime.gov.in/webform/cyber_suspect.aspx",
        "icon": "bi-exclamation-triangle",
        "button": "Report Suspicious Identifier",
        "number": None,
    },
    {
        "id": "chakshu",
        "title": "Sanchar Saathi – Chakshu",
        "category": "Fraudulent Calls, SMS and WhatsApp Messages",
        "description": (
            "The Department of Telecommunications facility for reporting "
            "suspected fraudulent communications, including impersonation "
            "scams, fake government calls, suspicious SMS messages, and "
            "fraudulent WhatsApp communications."
        ),
        "url": "https://sancharsaathi.gov.in/",
        "icon": "bi-phone",
        "button": "Visit Sanchar Saathi",
        "number": None,
    },
    {
        "id": "emergency-112",
        "title": "National Emergency Response Support System",
        "category": "Immediate Emergency Assistance",
        "description": (
            "Call the national emergency number when there is an immediate "
            "threat to personal safety, violence, or another emergency requiring "
            "police or emergency-service assistance. This is not a replacement "
            "for filing a cybercrime complaint."
        ),
        "url": "https://112.gov.in/",
        "icon": "bi-exclamation-octagon",
        "button": "Visit Emergency Services",
        "number": "112",
    },
    {
        "id": "women-helpline",
        "title": "Women Helpline",
        "category": "Support for Women in Distress",
        "description": (
            "Provides support and referral assistance for women facing violence "
            "or distress. It may be relevant in cases involving online harassment, "
            "threats, stalking, or abuse when additional support is needed."
        ),
        "url": "https://www.india.gov.in/",
        "icon": "bi-person-hearts",
        "button": "Visit Government Portal",
        "number": "181",
    },
    {
        "id": "ncw-helpline",
        "title": "National Commission for Women Helpline",
        "category": "Women’s Support and Assistance",
        "description": (
            "Provides assistance and referrals for women in distress, including "
            "connecting them with relevant authorities and support services. "
            "Use the National Cyber Crime Reporting Portal as well when reporting "
            "an online offence."
        ),
        "url": "https://www.ncwwomenhelpline.in/",
        "icon": "bi-person-check",
        "button": "Visit NCW Helpline",
        "number": "7827170170",
    },
    {
        "id": "child-helpline",
        "title": "Child Helpline",
        "category": "Children in Need of Protection",
        "description": (
            "Contact this helpline when a child needs care, protection, or help "
            "in a situation of abuse, exploitation, or distress. For online "
            "sexual exploitation or other cyber offences involving a child, "
            "the official cybercrime portal is also available."
        ),
        "url": "https://www.india.gov.in/",
        "icon": "bi-person-raised-hand",
        "button": "Visit Government Portal",
        "number": "1098",
    },
    {
        "id": "cybercrime-grievance",
        "title": "State/UT Cybercrime Grievance Contacts",
        "category": "Complaint Follow-up and Escalation",
        "description": (
            "Find the official State/UT nodal cybercrime officer and grievance "
            "officer contact details. This resource is intended for complainants "
            "who have already filed a report and need to follow up on its handling."
        ),
        "url": "https://cybercrime.gov.in/Webform/Crime_NodalGrivanceList.aspx",
        "icon": "bi-clipboard-check",
        "button": "Find State/UT Contacts",
        "number": None,
    },
    {
        "id": "consumer-helpline",
        "title": "National Consumer Helpline",
        "category": "Online Shopping and Consumer Grievances",
        "description": (
            "Use this service for consumer grievances such as e-commerce "
            "disputes, defective products, refunds, or service-related complaints. "
            "For criminal online payment fraud, report separately through the "
            "National Cyber Crime Reporting Portal or call 1930."
        ),
        "url": "https://consumerhelpline.gov.in/",
        "icon": "bi-bag-check",
        "button": "File Consumer Grievance",
        "number": "1915",
    },
]


@help_centre_bp.route("/help-centre", methods=["GET"])
def help_centre():
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    return render_template(
        "help_centre.html",
        resources=REPORTING_RESOURCES,
    )


@help_centre_bp.route("/help-centre/<topic_id>", methods=["GET"])
def help_topic(topic_id):
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    resource = next(
        (
            item
            for item in REPORTING_RESOURCES
            if item["id"] == topic_id
        ),
        None,
    )

    if resource is None:
        return redirect(url_for("help_centre.help_centre"))

    return redirect(resource["url"])