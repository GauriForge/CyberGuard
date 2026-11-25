from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    session,
    abort,
)

from database.db import get_db
from models.assessment_model import save_assessment_result
from routes.attacks import ATTACK_CATEGORIES
from data.assessment_question_bank import build_attack_question_bank


assessments_bp = Blueprint(
    "assessments",
    __name__,
    url_prefix="/assessments",
)


# --------------------------------------------------
# GENERAL PRACTICE QUESTION BANK
# --------------------------------------------------

QUESTION_BANK = {
    "beginner": [
        (
            "What is phishing?",
            [
                "A method of cooling a computer",
                "A deceptive attempt to steal information",
                "A type of firewall",
                "A database backup method",
            ],
            1,
            "Phishing uses deceptive messages or websites to obtain sensitive information.",
        ),
        (
            "Which password is generally strongest?",
            [
                "password123",
                "gauri2006",
                "12345678",
                "R7!mQ2#vL9@p",
            ],
            3,
            "Long, unique passwords are generally harder to guess. Use a password manager to generate and store them.",
        ),
        (
            "What should you do with an unexpected suspicious link?",
            [
                "Open it immediately",
                "Forward it to everyone",
                "Verify it through a trusted channel",
                "Enter your password to check it",
            ],
            2,
            "Verify unexpected links through a trusted channel before interacting with them.",
        ),
        (
            "What does antivirus software help with?",
            [
                "Detecting and removing certain malicious software",
                "Increasing screen brightness",
                "Creating social media accounts",
                "Replacing all security practices",
            ],
            0,
            "Antivirus tools can detect and help remove supported forms of malware.",
        ),
        (
            "What is the purpose of multi-factor authentication?",
            [
                "To remove all passwords",
                "To add another verification factor",
                "To make files public",
                "To disable account security",
            ],
            1,
            "Multi-factor authentication adds another verification factor to help protect accounts.",
        ),
        (
            "Why should software updates be installed?",
            [
                "Only to change icons",
                "To remove all user files",
                "To fix bugs and security vulnerabilities",
                "To disable the internet",
            ],
            2,
            "Updates frequently include security fixes and reliability improvements.",
        ),
        (
            "Which information should not be shared with strangers?",
            [
                "Public weather information",
                "Your account password",
                "A public news headline",
                "A general cybersecurity definition",
            ],
            1,
            "Passwords must remain confidential.",
        ),
        (
            "What is malware?",
            [
                "Software designed to perform harmful or unauthorized actions",
                "A type of computer monitor",
                "A safe backup procedure",
                "A network cable",
            ],
            0,
            "Malware is software intended to cause harm or perform unauthorized activity.",
        ),
        (
            "What should you do if you suspect your account was compromised?",
            [
                "Ignore the warning",
                "Share your password with friends",
                "Secure the account using a trusted device and report the incident",
                "Disable every security feature",
            ],
            2,
            "Secure the account using a trusted device and report the suspected compromise.",
        ),
        (
            "What is a backup?",
            [
                "A duplicate copy of data for recovery",
                "A suspicious email",
                "A password attack",
                "An unknown network user",
            ],
            0,
            "Backups help recover data after loss, damage, or certain security incidents.",
        ),
    ],

    "intermediate": [
        (
            "What is SQL injection?",
            [
                "A physical network cable problem",
                "Manipulating database queries through unsafe input",
                "A password storage format",
                "A wireless encryption standard",
            ],
            1,
            "SQL injection occurs when untrusted input changes the meaning of a database query.",
        ),
        (
            "Which defence is most appropriate for SQL injection?",
            [
                "Disabling database backups",
                "Using longer page titles",
                "Parameterized queries",
                "Making the database publicly accessible",
            ],
            2,
            "Parameterized queries separate data from SQL instructions.",
        ),
        (
            "What does a firewall primarily do?",
            [
                "Filters network traffic according to configured rules",
                "Guarantees every file is safe",
                "Replaces user authentication",
                "Automatically restores every deleted file",
            ],
            0,
            "Firewalls control network traffic based on configured security policies.",
        ),
        (
            "What is the purpose of hashing passwords?",
            [
                "To display passwords publicly",
                "To store a one-way password verifier",
                "To send passwords in plain text",
                "To disable authentication",
            ],
            1,
            "Passwords should be stored using a suitable password-hashing algorithm and salt.",
        ),
        (
            "What is a denial-of-service attack intended to do?",
            [
                "Improve application performance",
                "Create stronger passwords",
                "Make a service unavailable to legitimate users",
                "Encrypt a backup for recovery",
            ],
            2,
            "Denial-of-service attacks attempt to disrupt service availability.",
        ),
        (
            "Why is least privilege important?",
            [
                "Every user should be an administrator",
                "Users should receive only the access they need",
                "All accounts should share one password",
                "Access controls should be removed",
            ],
            1,
            "Least privilege limits unnecessary permissions and reduces potential damage.",
        ),
        (
            "What is cross-site scripting (XSS)?",
            [
                "Unsafe script execution in a user's browser",
                "A physical theft method",
                "A password backup system",
                "A network cable standard",
            ],
            0,
            "XSS can occur when untrusted content is handled unsafely and executed by a browser.",
        ),
        (
            "What does HTTPS provide?",
            [
                "A guarantee that every website is honest",
                "Encrypted communication with server authentication",
                "Automatic malware removal",
                "Unlimited account permissions",
            ],
            1,
            "HTTPS protects communication but does not guarantee that a website is trustworthy.",
        ),
        (
            "Why should security logs be reviewed?",
            [
                "To remove the need for access controls",
                "To publish private user data",
                "To identify suspicious activity and support investigations",
                "To disable monitoring",
            ],
            2,
            "Logs help detect anomalies and reconstruct events during investigations.",
        ),
        (
            "What is social engineering?",
            [
                "Manipulating people into revealing information or taking unsafe actions",
                "A method of compressing files",
                "A type of processor",
                "A secure backup protocol",
            ],
            0,
            "Social engineering exploits human trust, behaviour, or urgency.",
        ),
    ],

    "advanced": [
        (
            "What is the primary purpose of threat modelling?",
            [
                "To eliminate the need for testing",
                "To identify threats and plan appropriate mitigations",
                "To publish system credentials",
                "To disable security monitoring",
            ],
            1,
            "Threat modelling identifies likely threats, attack surfaces, and potential mitigations.",
        ),
        (
            "What does defence in depth mean?",
            [
                "Relying on one security product",
                "Removing overlapping controls",
                "Using multiple complementary security layers",
                "Giving all users administrator access",
            ],
            2,
            "Layered controls reduce dependence on any single defensive measure.",
        ),
        (
            "What is a race condition in security?",
            [
                "A timing-dependent issue involving concurrent operations",
                "A password format",
                "A network encryption algorithm",
                "A backup schedule",
            ],
            0,
            "Race conditions can create vulnerabilities when operation timing affects program state.",
        ),
        (
            "What is the purpose of a SIEM platform?",
            [
                "To replace every endpoint",
                "To collect and correlate security events for analysis",
                "To make all logs publicly accessible",
                "To generate passwords only",
            ],
            1,
            "SIEM systems centralize security data and help identify suspicious patterns.",
        ),
        (
            "What is a zero-day vulnerability?",
            [
                "A vulnerability that has never existed",
                "A routine software update",
                "A vulnerability exploited before an effective fix is available or widely deployed",
                "A type of backup",
            ],
            2,
            "Zero-day vulnerabilities leave defenders with little or no time to prepare an effective fix.",
        ),
        (
            "Why is input validation important?",
            [
                "It guarantees every user is trustworthy",
                "It helps ensure input meets expected rules before processing",
                "It replaces authorization checks",
                "It makes databases unnecessary",
            ],
            1,
            "Validation helps reject malformed input but must be combined with context-appropriate protections.",
        ),
        (
            "What is an indicator of compromise (IOC)?",
            [
                "Evidence that may indicate malicious activity",
                "A guarantee of system integrity",
                "A standard user interface",
                "A software licence",
            ],
            0,
            "IOCs include suspicious hashes, domains, or IP addresses associated with an investigation.",
        ),
        (
            "What is the purpose of network segmentation?",
            [
                "To remove all network controls",
                "To limit communication between network zones",
                "To expose internal services publicly",
                "To share administrator credentials",
            ],
            1,
            "Segmentation can limit lateral movement and restrict access between systems.",
        ),
        (
            "What should happen when handling a suspected incident?",
            [
                "Delete all available logs",
                "Publicly disclose unverified claims",
                "Follow the incident-response process and preserve relevant evidence",
                "Turn off every system without considering impact",
            ],
            2,
            "Follow established procedures, assess the threat, and preserve relevant evidence.",
        ),
        (
            "Why are parameterized queries preferable to SQL string concatenation?",
            [
                "They separate query instructions from supplied values",
                "They remove the need for database permissions",
                "They automatically encrypt all stored data",
                "They guarantee protection against every vulnerability",
            ],
            0,
            "Parameterized queries help prevent supplied values from being interpreted as SQL syntax.",
        ),
    ],

    "high-level": [
        (
            "What is the main objective of a zero-trust security model?",
            [
                "Trust every internal connection",
                "Verify access explicitly according to policy",
                "Remove identity management",
                "Allow unrestricted network access",
            ],
            1,
            "Zero trust emphasizes explicit verification, least privilege, and contextual access decisions.",
        ),
        (
            "What is a supply-chain attack?",
            [
                "An attack involving a supplier, dependency, or distribution process",
                "A routine backup",
                "A physical cooling method",
                "A standard password reset",
            ],
            0,
            "Supply-chain attacks abuse trust in software, hardware, vendors, or delivery processes.",
        ),
        (
            "What is the purpose of digital forensic chain of custody?",
            [
                "To edit evidence freely",
                "To document evidence handling and maintain accountability",
                "To remove evidence timestamps",
                "To publish confidential evidence",
            ],
            1,
            "Chain-of-custody records help document how evidence was collected, transferred, and preserved.",
        ),
        (
            "What does lateral movement describe?",
            [
                "Moving a laptop to another room",
                "Installing a routine patch",
                "An intruder moving between systems within an environment",
                "Restoring a deleted file",
            ],
            2,
            "Lateral movement describes progression from one compromised system or account to others.",
        ),
        (
            "Why is an incident-response playbook useful?",
            [
                "It provides repeatable procedures for defined incident types",
                "It guarantees incidents never occur",
                "It removes the need for evidence",
                "It gives every user unrestricted access",
            ],
            0,
            "Playbooks help responders follow consistent, documented actions during incidents.",
        ),
        (
            "What is secure-by-design development?",
            [
                "Adding security only after deployment",
                "Considering security throughout design and development",
                "Ignoring threat models",
                "Disabling access controls for convenience",
            ],
            1,
            "Secure-by-design integrates security requirements and controls throughout development.",
        ),
        (
            "What is the purpose of a cryptographic salt in password storage?",
            [
                "To make a password publicly readable",
                "To replace password hashing",
                "To help make identical passwords produce different salted hashes",
                "To store the original password in plain text",
            ],
            2,
            "A unique salt helps defend against precomputed attacks and identical hash values for identical passwords.",
        ),
        (
            "What is the purpose of an attack surface assessment?",
            [
                "To identify exposed entry points and potential paths of attack",
                "To remove all system documentation",
                "To disable security updates",
                "To increase user permissions",
            ],
            0,
            "Attack-surface assessment identifies exposed assets, interfaces, and potential weaknesses.",
        ),
        (
            "Why should forensic evidence be hashed during collection?",
            [
                "To alter the evidence content",
                "To help verify evidence integrity",
                "To conceal evidence ownership",
                "To replace documentation",
            ],
            1,
            "Cryptographic hashes help demonstrate whether evidence has changed between checks.",
        ),
        (
            "What is the purpose of vulnerability prioritization?",
            [
                "To fix issues in random order",
                "To ignore business impact",
                "To rank remediation based on risk and context",
                "To publish vulnerability details before assessing exposure",
            ],
            2,
            "Prioritization considers severity, exploitability, exposure, and business impact.",
        ),
    ],
}


LEVELS = {
    "beginner": {
        "name": "Beginner",
        "description": "Build foundational knowledge of cybersecurity threats and safe practices.",
    },
    "intermediate": {
        "name": "Intermediate",
        "description": "Practise identifying common attacks and selecting appropriate defences.",
    },
    "advanced": {
        "name": "Advanced",
        "description": "Explore security architecture, monitoring, and incident handling.",
    },
    "high-level": {
        "name": "High Level",
        "description": "Evaluate advanced security concepts, investigations, and risk decisions.",
    },
}


# --------------------------------------------------
# QUESTION NORMALIZATION
# --------------------------------------------------

def _normalise_question(raw):
    """Normalize a question without modifying the source data."""

    if not isinstance(raw, dict):
        return None

    question_text = (
        raw.get("question")
        or raw.get("question_text")
        or raw.get("text")
        or raw.get("prompt")
    )

    options = (
        raw.get("options")
        or raw.get("choices")
        or raw.get("answer_options")
        or raw.get("answers")
    )

    if isinstance(options, dict):
        options = list(options.values())

    if not question_text or not isinstance(options, (list, tuple)):
        return None

    normalized_options = []

    for option in options:
        if isinstance(option, dict):
            option = (
                option.get("text")
                or option.get("label")
                or option.get("option")
                or option.get("value")
            )

        if option is None:
            return None

        normalized_options.append(str(option))

    if len(normalized_options) < 2:
        return None

    answer = raw.get(
        "correct_answer",
        raw.get(
            "correct_option",
            raw.get(
                "correct",
                raw.get("answer", raw.get("answer_index")),
            ),
        ),
    )

    if isinstance(answer, dict):
        answer = (
            answer.get("text")
            or answer.get("label")
            or answer.get("option")
            or answer.get("value")
        )

    if isinstance(answer, str):
        answer_text = answer.strip()

        if answer_text in normalized_options:
            answer = normalized_options.index(answer_text)
        elif answer_text.isdigit():
            answer = int(answer_text)
        else:
            return None

    if isinstance(answer, bool) or not isinstance(answer, int):
        return None

    if not 0 <= answer < len(normalized_options):
        return None

    explanation = (
        raw.get("explanation")
        or raw.get("feedback")
        or raw.get("rationale")
        or raw.get("solution")
        or ""
    )

    return {
        "question": str(question_text),
        "options": normalized_options,
        "answer": answer,
        "explanation": str(explanation),
    }


# --------------------------------------------------
# GENERAL ASSESSMENTS
# --------------------------------------------------

def _make_general_assessments():
    assessments = []

    for level_id, level in LEVELS.items():
        bank = QUESTION_BANK[level_id]

        for number in range(1, 4):
            offset = (number - 1) * 3
            ordered = bank[offset:] + bank[:offset]

            assessments.append({
                "id": f"{level_id}-assessment-{number}",
                "title": f"{level['name']} Assessment {number}",
                "description": level["description"],
                "level": level_id,
                "type": "general",
                "category_id": None,
                "questions": [
                    {
                        "question": question,
                        "options": options,
                        "answer": answer,
                        "explanation": explanation,
                    }
                    for question, options, answer, explanation
                    in ordered[:10]
                ],
            })

    return assessments


# --------------------------------------------------
# ATTACK-SPECIFIC ASSESSMENTS
# --------------------------------------------------

def _build_attack_assessments():
    """Build one 10-question assessment for every attack in the question bank."""

    assessments = []
    seen_assessment_ids = set()

    question_bank = build_attack_question_bank(ATTACK_CATEGORIES)

    category_names = {
        str(category.get("id") or ""): (
            category.get("name") or "Cybersecurity"
        )
        for category in ATTACK_CATEGORIES
    }

    for bank_record in question_bank.values():
        category_id = str(bank_record.get("category_id") or "")
        attack_id = str(bank_record.get("attack_id") or "").strip()

        if not category_id or not attack_id:
            continue

        questions = []

        for raw_question in bank_record.get("questions", []):
            normalized = _normalise_question(raw_question)

            if normalized is not None:
                questions.append(normalized)

        if len(questions) != 10:
            continue

        title = (
            bank_record.get("attack_name")
            or attack_id.replace("-", " ").title()
        )

        assessment_id = f"attack-{category_id}-{attack_id}"

        if assessment_id in seen_assessment_ids:
            continue

        seen_assessment_ids.add(assessment_id)

        assessments.append({
            "id": assessment_id,
            "title": f"{title} Assessment",
            "description": (
                f"Test your understanding of {title} "
                f"and its defensive measures in the "
                f"{category_names.get(category_id, 'Cybersecurity')} category."
            ),
            "level": "intermediate",
            "type": "attack",
            "category_id": category_id,
            "attack_id": attack_id,
            "questions": questions,
        })

    return assessments


def get_all_assessments():
    """Return general and data-driven attack assessments."""

    return _make_general_assessments() + _build_attack_assessments()


def get_assessment(assessment_id):
    """Find an assessment by its unique ID."""

    return next(
        (
            assessment
            for assessment in get_all_assessments()
            if assessment["id"] == assessment_id
        ),
        None,
    )


# --------------------------------------------------
# USER AND RESULT HELPERS
# --------------------------------------------------

def _current_user_id():
    return session.get("user_id")


def _get_previous_results():
    user_id = _current_user_id()

    if user_id is None:
        return []

    db = get_db()

    return db.execute(
        """
        SELECT *
        FROM assessment_results
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT 10
        """,
        (user_id,),
    ).fetchall()


# --------------------------------------------------
# SHARED TEMPLATE CONTEXT
# --------------------------------------------------

def _assessment_page_context(
    selected_assessment=None,
    selected_level=None,
    level_assessments=None,
):
    return {
        "assessments": get_all_assessments(),
        "selected_assessment": selected_assessment,
        "selected_level": selected_level,
        "level_assessments": level_assessments or [],
        "categories": ATTACK_CATEGORIES,
        "general_levels": LEVELS,
        "previous_results": _get_previous_results(),
    }


# --------------------------------------------------
# ASSESSMENT LIST
# --------------------------------------------------

@assessments_bp.route("/")
def assessment_list():

    if not _current_user_id():
        return redirect(url_for("auth.login"))

    return render_template(
        "assessments.html",
        **_assessment_page_context(),
    )


# --------------------------------------------------
# GENERAL PRACTICE LEVEL
# --------------------------------------------------

@assessments_bp.route("/level/<level_id>")
def assessment_level(level_id):

    if not _current_user_id():
        return redirect(url_for("auth.login"))

    if level_id not in LEVELS:
        abort(404)

    assessments = get_all_assessments()

    level_assessments = [
        assessment
        for assessment in assessments
        if assessment["type"] == "general"
        and assessment["level"] == level_id
    ]

    return render_template(
        "assessments.html",
        **_assessment_page_context(
            selected_level=LEVELS[level_id],
            level_assessments=level_assessments,
        ),
    )


# --------------------------------------------------
# TAKE AND SUBMIT ASSESSMENT
# --------------------------------------------------

@assessments_bp.route("/<assessment_id>", methods=["GET", "POST"])
def take_assessment(assessment_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    assessment = get_assessment(assessment_id)

    if assessment is None:
        abort(404)

    if request.method == "POST":

        questions = assessment.get("questions", [])
        total_questions = len(questions)
        score = 0

        for index, question in enumerate(questions):

            submitted_answer = request.form.get(f"question_{index}")

            if submitted_answer is None:
                continue

            try:
                selected_answer = int(submitted_answer)
            except (TypeError, ValueError):
                continue

            if 0 <= selected_answer < len(question["options"]):
                if selected_answer == question["answer"]:
                    score += 1

        result_id = save_assessment_result(
            user_id=session["user_id"],
            assessment_name=assessment["title"],
            score=score,
            total_questions=total_questions,
        )

        return redirect(
            url_for(
                "assessments.assessment_result",
                result_id=result_id,
            )
        )

    return render_template(
        "assessments.html",
        **_assessment_page_context(
            selected_assessment=assessment,
        ),
    )


# --------------------------------------------------
# ASSESSMENT RESULTS
# --------------------------------------------------

@assessments_bp.route("/results/<int:result_id>")
def assessment_result(result_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    db = get_db()

    result = db.execute(
        """
        SELECT *
        FROM assessment_results
        WHERE id = ? AND user_id = ?
        """,
        (result_id, session["user_id"]),
    ).fetchone()

    if result is None:
        abort(404)

    return render_template(
        "assessment_results.html",
        result=result,
    )