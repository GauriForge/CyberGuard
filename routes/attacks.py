
from flask import Blueprint, render_template, redirect, url_for, session

from data.social_engineering import SOCIAL_ENGINEERING
from data.phishing_variants import PHISHING_VARIANTS
from data.password_credential_attacks import PASSWORD_CREDENTIAL_ATTACKS
from data.malware import MALWARE
from data.spyware_surveillance import SPYWARE_SURVEILLANCE
from data.network_attacks import NETWORK_ATTACKS
from data.wireless_attacks import WIRELESS_ATTACKS
from data.web_application_attacks import WEB_APPLICATION_ATTACKS
from data.identity_access_session import IDENTITY_ACCESS_SESSION
from data.data_information_attacks import DATA_INFORMATION_ATTACKS
from data.insider_supply_chain import INSIDER_SUPPLY_CHAIN
from data.physical_device_attacks import PHYSICAL_DEVICE_ATTACKS
from data.mobile_iot_attacks import MOBILE_IOT_ATTACKS
from data.availability_resource_attacks import AVAILABILITY_RESOURCE_ATTACKS

from data.data_adapter import (
    get_category_attacks,
    get_subcategories,
    find_attack,
)


attacks_bp = Blueprint("attacks", __name__)


ATTACK_CATEGORIES = [
    {
        "id": "social-engineering",
        "name": "Social Engineering",
        "description": "Attacks that manipulate people into revealing information or taking unsafe actions.",
        "icon": "users",
        "attacks": SOCIAL_ENGINEERING,
    },
    {
        "id": "phishing",
        "name": "Phishing Variants",
        "description": "Deceptive messages and websites used to trick people.",
        "icon": "mail",
        "attacks": PHISHING_VARIANTS,
    },
    {
        "id": "password-credential",
        "name": "Password and Credential Attacks",
        "description": "Techniques involving compromised passwords and authentication credentials.",
        "icon": "key",
        "attacks": PASSWORD_CREDENTIAL_ATTACKS,
    },
    {
        "id": "malware",
        "name": "Malware",
        "description": "Malicious software and its impact on systems and data.",
        "icon": "bug",
        "attacks": MALWARE,
    },
    {
        "id": "spyware-surveillance",
        "name": "Spyware and Surveillance",
        "description": "Threats involving unauthorized monitoring and information collection.",
        "icon": "eye",
        "attacks": SPYWARE_SURVEILLANCE,
    },
    {
        "id": "network",
        "name": "Network Attacks",
        "description": "Threats targeting network communications and infrastructure.",
        "icon": "network",
        "attacks": NETWORK_ATTACKS,
    },
    {
        "id": "wireless",
        "name": "Wireless Attacks",
        "description": "Security threats affecting Wi-Fi and other wireless technologies.",
        "icon": "wifi",
        "attacks": WIRELESS_ATTACKS,
    },
    {
        "id": "web-application",
        "name": "Web Application Attacks",
        "description": "Common vulnerabilities and threats affecting web applications.",
        "icon": "globe",
        "attacks": WEB_APPLICATION_ATTACKS,
    },
    {
        "id": "identity-access-session",
        "name": "Identity, Access and Session Attacks",
        "description": "Threats involving identity verification, access controls and sessions.",
        "icon": "shield",
        "attacks": IDENTITY_ACCESS_SESSION,
    },
    {
        "id": "data-information",
        "name": "Data and Information Attacks",
        "description": "Threats involving unauthorized access, exposure or manipulation of data.",
        "icon": "database",
        "attacks": DATA_INFORMATION_ATTACKS,
    },
    {
        "id": "insider-supply-chain",
        "name": "Insider and Supply Chain Attacks",
        "description": "Threats involving trusted access and compromised suppliers or dependencies.",
        "icon": "git-branch",
        "attacks": INSIDER_SUPPLY_CHAIN,
    },
    {
        "id": "physical-device",
        "name": "Physical and Device Attacks",
        "description": "Threats involving physical access, devices and hardware.",
        "icon": "laptop",
        "attacks": PHYSICAL_DEVICE_ATTACKS,
    },
    {
        "id": "mobile-iot",
        "name": "Mobile and IoT Attacks",
        "description": "Security threats affecting mobile devices and connected devices.",
        "icon": "smartphone",
        "attacks": MOBILE_IOT_ATTACKS,
    },
    {
        "id": "availability-resource",
        "name": "Availability and Resource Attacks",
        "description": "Threats that disrupt service availability or exhaust system resources.",
        "icon": "server",
        "attacks": AVAILABILITY_RESOURCE_ATTACKS,
    },
]


def _get_category(category_id):
    """Return a category and its normalized attack records."""
    category = next(
        (
            item for item in ATTACK_CATEGORIES
            if item["id"] == str(category_id)
        ),
        None,
    )

    if category is None:
        return None, []

    return category, get_category_attacks(category["attacks"])


def _get_subcategories(category):
    """Return normalized subcategories with accurate attack counts."""
    return get_subcategories(category["attacks"])


def _get_subcategory(category, subcategory_id):
    """Return a matching subcategory and its normalized attacks."""
    for subcategory in _get_subcategories(category):
        if subcategory["id"] == str(subcategory_id):
            return subcategory, subcategory["attacks_list"]

    return None, []


def _find_attack(category, attack_id, subcategory_id=None):
    """Find an attack through the shared data adapter."""
    return find_attack(
        category["attacks"],
        attack_id,
        subcategory_id=subcategory_id,
    )


def _login_required():
    return not session.get("user_id")


def _not_found(message):
    return render_template("404.html", message=message), 404


@attacks_bp.route("/attacks")
def attack_categories():
    if _login_required():
        return redirect(url_for("auth.login"))

    categories = []

    for category in ATTACK_CATEGORIES:
        subcategories = _get_subcategories(category)
        _, attacks = _get_category(category["id"])

        categories.append({
            **category,
            "count": len(attacks),
            "subcategories": subcategories,
        })

    return render_template(
        "attack_categories.html",
        categories=categories,
    )


@attacks_bp.route("/attacks/<category_id>")
def attack_overview(category_id):
    if _login_required():
        return redirect(url_for("auth.login"))

    category, attacks = _get_category(category_id)

    if category is None:
        return _not_found("Attack category not found.")

    return render_template(
        "attack_overview.html",
        category=category,
        subcategories=_get_subcategories(category),
        subcategory=None,
        attacks=attacks,
    )


@attacks_bp.route("/attacks/<category_id>/<subcategory_id>")
def attack_subcategory(category_id, subcategory_id):
    if _login_required():
        return redirect(url_for("auth.login"))

    category, _ = _get_category(category_id)

    if category is None:
        return _not_found("Attack category not found.")

    subcategory, attacks = _get_subcategory(
        category,
        subcategory_id,
    )

    if subcategory is None:
        return _not_found("Attack subcategory not found.")

    return render_template(
        "attack_overview.html",
        category=category,
        subcategories=[],
        subcategory=subcategory,
        attacks=attacks,
    )


@attacks_bp.route("/attacks/<category_id>/topic/<attack_id>")
def attack_learning(category_id, attack_id):
    if _login_required():
        return redirect(url_for("auth.login"))

    category, _ = _get_category(category_id)

    if category is None:
        return _not_found("Attack category not found.")

    subcategory, attack = _find_attack(category, attack_id)

    if attack is None:
        return _not_found("Attack topic not found.")

    return render_template(
        "attack_learning.html",
        category=category,
        attack=attack,
        subcategory=subcategory,
    )


@attacks_bp.route(
    "/attacks/<category_id>/<subcategory_id>/<attack_id>"
)
def subcategory_attack_learning(
    category_id,
    subcategory_id,
    attack_id,
):
    if _login_required():
        return redirect(url_for("auth.login"))

    category, _ = _get_category(category_id)

    if category is None:
        return _not_found("Attack category not found.")

    subcategory, attack = _find_attack(
        category,
        attack_id,
        subcategory_id=subcategory_id,
    )

    if subcategory is None:
        return _not_found("Attack subcategory not found.")

    if attack is None:
        return _not_found("Attack topic not found.")

    return render_template(
        "attack_learning.html",
        category=category,
        attack=attack,
        subcategory=subcategory,
    )