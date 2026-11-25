
SOCIAL_ENGINEERING = {
    "id": "social-engineering",
    "name": "Social Engineering",
    "description": (
        "Understand how attackers exploit human trust, emotions, "
        "and digital communication to compromise people and organisations."
    ),
    "types": {
        "human-based": {
            "id": "human-based",
            "name": "Human-Based Social Engineering",
            "description": (
                "Attacks that rely on direct human interaction, "
                "manipulation, impersonation, or physical proximity."
            ),
            "types": {
                "impersonation": {
                    "id": "impersonation",
                    "name": "Impersonation",
                    "difficulty": "Beginner",
                    "summary": (
                        "An attacker pretends to be a trusted person "
                        "to obtain information, access, or assistance."
                    ),
                    "overview": (
                        "Impersonation is a social engineering technique "
                        "in which someone adopts another person's identity "
                        "or role. The attacker may pretend to be an employee, "
                        "technician, manager, delivery worker, or service "
                        "provider. The objective is to make the victim trust "
                        "the request without checking whether it is genuine."
                    ),
                    "how_it_works": [
                        "The attacker chooses a person or role the victim is likely to trust.",
                        "The attacker creates a believable story or reason for making contact.",
                        "The victim is asked to share information, grant access, or perform an action.",
                        "If the request is not verified, the attacker may gain unauthorised access or information.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "Fake IT support call",
                            "scenario": (
                                "An employee receives a call from someone "
                                "claiming to work in the IT department. "
                                "The caller says an account problem needs "
                                "immediate attention and asks the employee "
                                "to reveal a password or one-time code."
                            ),
                            "lesson": (
                                "Legitimate support staff should not need "
                                "the employee's password or authentication code."
                            ),
                        },
                        {
                            "title": "Impersonated manager",
                            "scenario": (
                                "A staff member receives an urgent message "
                                "apparently from a senior manager requesting "
                                "confidential documents."
                            ),
                            "lesson": (
                                "Verify unusual requests through a separate, "
                                "known communication channel."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The unauthorised maintenance visit",
                            "scenario": (
                                "A person arrives at an office claiming to "
                                "be a maintenance contractor. They ask an "
                                "employee to let them enter a restricted room."
                            ),
                            "investigation": (
                                "The employee checks the visitor's identity "
                                "and discovers that no maintenance visit was "
                                "scheduled."
                            ),
                            "outcome": (
                                "The access request is denied and the security "
                                "team is informed."
                            ),
                            "key_takeaway": (
                                "A convincing uniform or confident explanation "
                                "does not replace identity verification."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Would you trust the caller?",
                        "scenario": (
                            "Someone claiming to be from IT calls and says "
                            "your account will be disabled in five minutes "
                            "unless you provide your login code."
                        ),
                        "question": "What is the safest response?",
                        "options": [
                            "Provide the code to avoid losing access.",
                            "Ask for their personal phone number.",
                            "End the call and contact IT through the official channel.",
                            "Share the code but change the password later.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Contacting IT through a known official channel "
                            "allows you to verify the request independently. "
                            "Never share passwords or one-time authentication codes."
                        ),
                    },
                    "practical_lab": {
                        "title": "Verify a suspicious identity request",
                        "objective": (
                            "Practise identifying identity claims that need "
                            "independent verification."
                        ),
                        "scenario": (
                            "A visitor claims to be an external technician "
                            "and requests access to a restricted office area."
                        ),
                        "tasks": [
                            "Identify the information needed to verify the visitor.",
                            "Determine which official person or team should confirm the visit.",
                            "Choose a safe response without disclosing confidential information.",
                            "Record the incident according to workplace procedures.",
                        ],
                        "expected_outcome": (
                            "The learner verifies the visitor independently, "
                            "refuses unverified access, and reports suspicious activity."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What is the main goal of impersonation?",
                            "options": [
                                "To improve an organisation's security",
                                "To exploit trust by pretending to be someone else",
                                "To update software automatically",
                                "To encrypt every file on a computer",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Impersonation exploits trust in a person or role "
                                "to obtain information, access, or cooperation."
                            ),
                        },
                        {
                            "question": "An alleged technician asks for your password. What should you do?",
                            "options": [
                                "Provide it immediately",
                                "Write it on a note",
                                "Verify the request through official channels and refuse to share the password",
                                "Send it to a personal email address",
                            ],
                            "answer": 2,
                            "explanation": (
                                "Passwords must remain confidential, and the "
                                "person's identity should be verified independently."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Unexpected requests for confidential information.",
                        "Pressure to bypass identity or access checks.",
                        "Unscheduled visits or calls.",
                        "Requests for passwords or authentication codes.",
                        "Unusual urgency or claims of senior authority.",
                    ],
                    "detection": [
                        "Verify identities using approved directories or contact details.",
                        "Confirm unusual requests with the relevant manager.",
                        "Check visitor appointments and access authorisations.",
                        "Report suspicious identity claims to the security team.",
                    ],
                    "prevention": [
                        "Use multi-factor authentication.",
                        "Never disclose passwords or one-time codes.",
                        "Follow visitor-management procedures.",
                        "Confirm sensitive requests through a second channel.",
                        "Provide regular social engineering awareness training.",
                    ],
                    "impact": [
                        "Unauthorised access to accounts or buildings.",
                        "Exposure of confidential information.",
                        "Financial losses and operational disruption.",
                        "Damage to organisational reputation.",
                    ],
                    "conclusion": (
                        "Impersonation succeeds when trust replaces verification. "
                        "Check identities, follow access procedures, and report "
                        "suspicious requests."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Avoiding Social Engineering and Phishing Attacks",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },

                "pretexting": {
                    "id": "pretexting",
                    "name": "Pretexting",
                    "difficulty": "Beginner",
                    "summary": (
                        "An attacker invents a believable situation to persuade "
                        "someone to reveal information or take an action."
                    ),
                    "overview": (
                        "Pretexting involves constructing a false story, or "
                        "pretext, to influence a target. Unlike a simple "
                        "unsolicited request, the attacker may prepare details "
                        "that make the situation appear routine or legitimate. "
                        "The story might involve an account review, a delivery, "
                        "a payment problem, or an internal investigation."
                    ),
                    "how_it_works": [
                        "The attacker chooses a goal and develops a convincing story.",
                        "The attacker may collect public information to make the story sound credible.",
                        "The victim receives a request that appears to fit the situation.",
                        "The attacker attempts to obtain sensitive information or cause an unauthorised action.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "A fabricated account review",
                            "scenario": (
                                "A caller claims to be reviewing a customer's "
                                "account and asks for personal details that "
                                "the legitimate organisation would not request "
                                "in that way."
                            ),
                            "lesson": (
                                "Contact the organisation using its official "
                                "website or a trusted number."
                            ),
                        },
                        {
                            "title": "A false payment emergency",
                            "scenario": (
                                "An employee receives a request to urgently "
                                "change a supplier's bank details because of "
                                "an alleged payment issue."
                            ),
                            "lesson": (
                                "Verify payment changes using an established "
                                "independent approval process."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The convincing supplier request",
                            "scenario": (
                                "A finance employee receives an email claiming "
                                "that a supplier has changed its bank account."
                            ),
                            "investigation": (
                                "The employee notices the unusual request and "
                                "calls the supplier using a number already "
                                "recorded in the company's system."
                            ),
                            "outcome": (
                                "The supplier confirms that no change was made, "
                                "and the suspicious email is reported."
                            ),
                            "key_takeaway": (
                                "A plausible explanation is not proof of legitimacy."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "The urgent account review",
                        "scenario": (
                            "A caller says they are investigating suspicious "
                            "activity and asks you to confirm your password "
                            "and date of birth."
                        ),
                        "question": "What should you do first?",
                        "options": [
                            "Give the requested details because the story sounds credible.",
                            "Ask the caller to wait while you verify their identity through an official channel.",
                            "Share only the password.",
                            "Send the information through a personal email account.",
                        ],
                        "correct_answer": 1,
                        "explanation": (
                            "An invented scenario can sound convincing. "
                            "Independent verification is safer than trusting "
                            "the explanation supplied by the caller."
                        ),
                    },
                    "practical_lab": {
                        "title": "Evaluate a fabricated request",
                        "objective": (
                            "Identify the difference between a plausible story "
                            "and a verified request."
                        ),
                        "scenario": (
                            "An employee receives a request to disclose "
                            "customer information for an alleged audit."
                        ),
                        "tasks": [
                            "Identify the sensitive information being requested.",
                            "List details that require independent confirmation.",
                            "Choose an authorised verification channel.",
                            "Document the decision and escalation process.",
                        ],
                        "expected_outcome": (
                            "The learner avoids disclosing information until "
                            "the request and the requester's authority are verified."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What makes pretexting distinctive?",
                            "options": [
                                "It always uses malicious software.",
                                "It relies on a fabricated or misleading scenario.",
                                "It only happens through text messages.",
                                "It requires physical access to a server.",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Pretexting relies on a story designed to make "
                                "a request appear legitimate."
                            ),
                        },
                        {
                            "question": "A caller claims to be conducting an audit. What is the safest approach?",
                            "options": [
                                "Disclose all requested information",
                                "Trust the caller if they know your name",
                                "Verify the audit and the caller's authority independently",
                                "Ignore all workplace procedures",
                            ],
                            "answer": 2,
                            "explanation": (
                                "Knowing personal or workplace details does not "
                                "prove that a person is authorised."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Detailed stories used to justify unusual requests.",
                        "Requests to bypass standard procedures.",
                        "Urgency, secrecy, or threats of consequences.",
                        "Requests for sensitive data without clear authorisation.",
                    ],
                    "detection": [
                        "Check requests against established policies.",
                        "Verify the requester's identity independently.",
                        "Confirm payment and account changes using approved procedures.",
                        "Report inconsistent or suspicious details.",
                    ],
                    "prevention": [
                        "Apply least-privilege access controls.",
                        "Use dual approval for sensitive transactions.",
                        "Keep confidential information private.",
                        "Train staff to challenge unusual requests respectfully.",
                    ],
                    "impact": [
                        "Identity theft and privacy violations.",
                        "Fraudulent transactions.",
                        "Compromised accounts.",
                        "Regulatory and reputational consequences.",
                    ],
                    "conclusion": (
                        "Pretexting depends on believable explanations rather "
                        "than genuine authority. Verify the request, not just the story."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Secure Our World",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },

                "baiting": {
                    "id": "baiting",
                    "name": "Baiting",
                    "difficulty": "Beginner",
                    "summary": (
                        "An attacker uses something tempting or seemingly useful "
                        "to encourage an unsafe action."
                    ),
                    "overview": (
                        "Baiting exploits curiosity, convenience, or the promise "
                        "of a reward. The bait may be a USB drive, a free download, "
                        "a prize notification, or access to attractive content. "
                        "The aim is to persuade a person to open, connect, install, "
                        "or disclose something that creates a security risk."
                    ),
                    "how_it_works": [
                        "The attacker creates or presents an attractive offer or object.",
                        "The target is encouraged to interact with it.",
                        "The interaction may expose the target to malware, credential theft, or a fraudulent request.",
                        "The attacker attempts to benefit from the resulting access or information.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "An unknown USB drive",
                            "scenario": (
                                "Someone finds a USB drive in a shared office "
                                "space and considers plugging it into a work computer."
                            ),
                            "lesson": (
                                "Do not connect unknown removable media to "
                                "an organisation's devices."
                            ),
                        },
                        {
                            "title": "A suspicious free download",
                            "scenario": (
                                "A website advertises a free premium application "
                                "but asks the user to disable security protection "
                                "before installation."
                            ),
                            "lesson": (
                                "Avoid unofficial downloads and never disable "
                                "security controls to install an untrusted file."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The unknown removable drive",
                            "scenario": (
                                "An employee finds a USB drive labelled "
                                "'Payroll' and considers opening it."
                            ),
                            "investigation": (
                                "The employee reports the device to IT instead "
                                "of connecting it to a workstation."
                            ),
                            "outcome": (
                                "The security team handles the device under its "
                                "removable-media procedure."
                            ),
                            "key_takeaway": (
                                "Curiosity should never override device security policies."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "A tempting download",
                        "scenario": (
                            "A pop-up promises free software and instructs you "
                            "to turn off antivirus protection before downloading."
                        ),
                        "question": "Which action is safest?",
                        "options": [
                            "Disable antivirus and install it.",
                            "Download it using a personal account.",
                            "Close the pop-up and use a trusted software source.",
                            "Forward the installer to colleagues.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Unexpected offers that ask you to disable protection "
                            "are suspicious. Use trusted software sources."
                        ),
                    },
                    "practical_lab": {
                        "title": "Assess a suspicious digital offer",
                        "objective": (
                            "Recognise potentially unsafe downloads and removable media."
                        ),
                        "scenario": (
                            "You encounter an unknown USB drive and a website "
                            "offering a free application from an unverified source."
                        ),
                        "tasks": [
                            "Identify the security risks in both situations.",
                            "Explain why the offered item may be attractive to a victim.",
                            "Select a safe reporting or verification procedure.",
                            "Describe how to obtain legitimate software.",
                        ],
                        "expected_outcome": (
                            "The learner avoids unknown media and untrusted "
                            "downloads and follows approved security procedures."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What does baiting exploit?",
                            "options": [
                                "Curiosity or the promise of a reward",
                                "Only weak encryption algorithms",
                                "Network routing tables",
                                "Database indexing",
                            ],
                            "answer": 0,
                            "explanation": (
                                "Baiting encourages an unsafe interaction through "
                                "curiosity, convenience, or a tempting offer."
                            ),
                        },
                        {
                            "question": "You find an unknown USB drive at work. What should you do?",
                            "options": [
                                "Plug it in to identify the owner",
                                "Use it on a spare computer",
                                "Give it to IT or security without connecting it",
                                "Copy its contents to your laptop",
                            ],
                            "answer": 2,
                            "explanation": (
                                "Unknown removable media should be handled through "
                                "the organisation's approved security procedure."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Unexpected prizes or unusually attractive offers.",
                        "Unknown USB drives or removable devices.",
                        "Downloads from unofficial websites.",
                        "Instructions to disable antivirus or other protections.",
                    ],
                    "detection": [
                        "Inspect the source of software and downloads.",
                        "Report unknown devices to IT or security.",
                        "Use endpoint protection and application controls.",
                        "Check unexpected offers through official sources.",
                    ],
                    "prevention": [
                        "Disable autorun where appropriate.",
                        "Use approved software repositories.",
                        "Restrict removable-media use.",
                        "Never disable security protection for an unknown download.",
                    ],
                    "impact": [
                        "Malware infection.",
                        "Credential theft.",
                        "Unauthorised access to workplace systems.",
                        "Data exposure and operational disruption.",
                    ],
                    "conclusion": (
                        "If an offer or object seems unusually tempting, pause "
                        "and verify it before interacting with it."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Secure Our World",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },

                "tailgating": {
                    "id": "tailgating",
                    "name": "Tailgating",
                    "difficulty": "Beginner",
                    "summary": (
                        "An unauthorised person follows an authorised person "
                        "into a restricted physical area."
                    ),
                    "overview": (
                        "Tailgating is a physical security attack that exploits "
                        "courtesy, distraction, or weak access-control practices. "
                        "An unauthorised person may follow someone through a "
                        "secured door without presenting their own credentials."
                    ),
                    "how_it_works": [
                        "The attacker identifies a controlled entrance.",
                        "The attacker waits for an authorised person to enter.",
                        "The attacker attempts to follow through before the door closes.",
                        "If staff fail to challenge the entry, the attacker may access a restricted area.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "Following through an office entrance",
                            "scenario": (
                                "A person carrying boxes asks an employee to "
                                "hold a secure door open and follows them inside."
                            ),
                            "lesson": (
                                "Each person should follow the site's access "
                                "policy rather than relying on another person's entry."
                            ),
                        },
                        {
                            "title": "A visitor without a badge",
                            "scenario": (
                                "Someone enters behind a group of employees "
                                "and proceeds towards a restricted room."
                            ),
                            "lesson": (
                                "Visitors should be identified, registered, "
                                "and escorted where required."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The unregistered visitor",
                            "scenario": (
                                "A visitor enters an office behind an employee "
                                "without checking in at reception."
                            ),
                            "investigation": (
                                "Security staff notice the missing visitor "
                                "registration and confirm the person's appointment."
                            ),
                            "outcome": (
                                "The visitor is directed through the proper "
                                "registration process."
                            ),
                            "key_takeaway": (
                                "Physical access rules apply even when someone "
                                "appears harmless or is carrying equipment."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Someone follows you through a secure door",
                        "scenario": (
                            "You badge into a restricted office and an unknown "
                            "person attempts to follow you inside."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Hold the door open automatically.",
                            "Let them in if they look professional.",
                            "Follow site procedures and ask them to use the authorised entry process.",
                            "Give them your access card.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Do not bypass physical access controls. Direct "
                            "the person to reception or the authorised entry process."
                        ),
                    },
                    "practical_lab": {
                        "title": "Physical access decision exercise",
                        "objective": (
                            "Practise responding safely to unverified entry requests."
                        ),
                        "scenario": (
                            "An unknown person asks to enter a restricted area "
                            "behind you because they have left their access card behind."
                        ),
                        "tasks": [
                            "Identify the access-control policy that applies.",
                            "Choose a polite way to decline unauthorised entry.",
                            "Direct the person to reception or security.",
                            "Record or report repeated suspicious behaviour.",
                        ],
                        "expected_outcome": (
                            "The learner maintains access controls without "
                            "putting themselves at unnecessary risk."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What is tailgating?",
                            "options": [
                                "Following an authorised person into a restricted area without proper authorisation",
                                "Sending an unsolicited email",
                                "Stealing a password through a fake website",
                                "Encrypting files for ransom",
                            ],
                            "answer": 0,
                            "explanation": (
                                "Tailgating exploits physical access procedures "
                                "to enter a restricted area."
                            ),
                        },
                        {
                            "question": "A person asks you to let them into a restricted office. What is the best response?",
                            "options": [
                                "Share your access card",
                                "Allow entry if they seem friendly",
                                "Direct them to the approved visitor or access process",
                                "Leave the door unlocked",
                            ],
                            "answer": 2,
                            "explanation": (
                                "Every person must follow the authorised access "
                                "procedure, regardless of appearance or claimed role."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "People entering without displaying required credentials.",
                        "Requests to bypass locked doors or visitor registration.",
                        "Unescorted visitors in restricted areas.",
                        "People borrowing or sharing access cards.",
                    ],
                    "detection": [
                        "Check that visitors follow registration procedures.",
                        "Challenge suspicious entry attempts according to policy.",
                        "Report malfunctioning access-control doors.",
                        "Review access logs when an incident is suspected.",
                    ],
                    "prevention": [
                        "Use individual access credentials.",
                        "Avoid holding secured doors open for unverified people.",
                        "Provide visitor badges and escorts where required.",
                        "Train staff on physical security procedures.",
                    ],
                    "impact": [
                        "Theft of equipment or sensitive documents.",
                        "Unauthorised access to internal systems.",
                        "Physical tampering with devices.",
                        "Threats to employee safety and organisational security.",
                    ],
                    "conclusion": (
                        "Physical security depends on consistent access checks, "
                        "not assumptions about who belongs in a building."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Physical Security",
                            "url": "https://www.cisa.gov/topics/physical-security",
                        },
                    ],
                },

                "shoulder-surfing": {
                    "id": "shoulder-surfing",
                    "name": "Shoulder Surfing",
                    "difficulty": "Beginner",
                    "summary": (
                        "An attacker observes someone entering confidential "
                        "information or viewing a sensitive screen."
                    ),
                    "overview": (
                        "Shoulder surfing is the unauthorised observation of "
                        "private information, such as passwords, PINs, account "
                        "details, or confidential documents. It can happen in "
                        "public places, offices, transport, or any environment "
                        "where screens and keyboards are visible to others."
                    ),
                    "how_it_works": [
                        "The attacker positions themselves where the target's screen or keyboard is visible.",
                        "The target enters or displays sensitive information.",
                        "The attacker memorises, records, or otherwise captures what they observe.",
                        "The information may be used for unauthorised access or fraud.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "Entering a PIN in public",
                            "scenario": (
                                "A person stands close to someone using a payment "
                                "terminal and tries to observe their PIN."
                            ),
                            "lesson": (
                                "Shield the keypad and remain aware of nearby observers."
                            ),
                        },
                        {
                            "title": "A visible laptop screen",
                            "scenario": (
                                "An employee reviews confidential work on a "
                                "laptop in a crowded public area."
                            ),
                            "lesson": (
                                "Use a privacy screen where appropriate and "
                                "avoid displaying sensitive information in public."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The exposed login screen",
                            "scenario": (
                                "An employee enters a password while seated "
                                "where nearby visitors can see the keyboard."
                            ),
                            "investigation": (
                                "The employee realises the screen and keyboard "
                                "were visible to other people."
                            ),
                            "outcome": (
                                "The employee moves to a private location and "
                                "follows company policy for any potentially exposed credential."
                            ),
                            "key_takeaway": (
                                "Physical privacy is part of account security."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Working in a crowded place",
                        "scenario": (
                            "You need to sign in to a work account while "
                            "people are seated close behind you."
                        ),
                        "question": "Which action best reduces the risk?",
                        "options": [
                            "Use the same visible password as every other account.",
                            "Turn the screen towards the crowd.",
                            "Move to a more private location and shield the screen and keyboard.",
                            "Leave the account open when you walk away.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Reducing visibility and shielding input helps "
                            "prevent other people from observing confidential information."
                        ),
                    },
                    "practical_lab": {
                        "title": "Privacy risk assessment",
                        "objective": (
                            "Identify opportunities for unauthorised observation."
                        ),
                        "scenario": (
                            "A workstation is positioned near a public walkway, "
                            "and its display contains confidential information."
                        ),
                        "tasks": [
                            "Identify who could view the screen.",
                            "Describe ways to reposition the workstation or screen.",
                            "Recommend suitable privacy controls.",
                            "Explain how to secure the workstation when unattended.",
                        ],
                        "expected_outcome": (
                            "The learner identifies visual exposure risks and "
                            "recommends practical privacy safeguards."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What is shoulder surfing?",
                            "options": [
                                "Observing private information over someone's shoulder",
                                "Sending malicious attachments",
                                "Flooding a network with traffic",
                                "Stealing a computer physically",
                            ],
                            "answer": 0,
                            "explanation": (
                                "Shoulder surfing involves observing sensitive "
                                "information without permission."
                            ),
                        },
                        {
                            "question": "Which measure helps prevent shoulder surfing?",
                            "options": [
                                "Displaying passwords openly",
                                "Using a privacy screen and shielding sensitive input",
                                "Sharing a login with colleagues",
                                "Leaving a workstation unlocked",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Privacy screens, careful positioning, and "
                                "shielding sensitive input reduce visual exposure."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "People standing unusually close while you enter credentials.",
                        "Screens visible from public walkways.",
                        "Confidential documents left facing visitors.",
                        "Unattended devices displaying private information.",
                    ],
                    "detection": [
                        "Review workstation placement and screen visibility.",
                        "Check for unauthorised photography where policy permits.",
                        "Report suspected credential exposure.",
                        "Review account activity if credentials may have been observed.",
                    ],
                    "prevention": [
                        "Use privacy screens when appropriate.",
                        "Shield PINs and passwords while entering them.",
                        "Lock devices when unattended.",
                        "Avoid viewing sensitive information in exposed locations.",
                        "Use strong, unique passwords and multi-factor authentication.",
                    ],
                    "impact": [
                        "Credential compromise.",
                        "Exposure of personal or business information.",
                        "Unauthorised transactions.",
                        "Privacy and compliance violations.",
                    ],
                    "conclusion": (
                        "Protecting information means controlling who can see "
                        "it, as well as who can access it digitally."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Secure Our World",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },

                "quid-pro-quo": {
                    "id": "quid-pro-quo",
                    "name": "Quid Pro Quo",
                    "difficulty": "Beginner",
                    "summary": (
                        "An attacker offers a service or benefit in exchange "
                        "for information, access, or an unsafe action."
                    ),
                    "overview": (
                        "Quid pro quo is a social engineering technique based "
                        "on an exchange. The attacker promises help, a reward, "
                        "or another benefit in return for something valuable. "
                        "For example, someone may claim to fix a technical "
                        "problem if the victim reveals credentials."
                    ),
                    "how_it_works": [
                        "The attacker offers assistance, a reward, or a service.",
                        "The offer is tied to a request for information or action.",
                        "The target is encouraged to accept the exchange.",
                        "The attacker attempts to exploit the information or access provided.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "Fake technical assistance",
                            "scenario": (
                                "A caller offers to fix a computer issue in "
                                "exchange for a password or remote access."
                            ),
                            "lesson": (
                                "Use the organisation's official support process "
                                "and never disclose a password."
                            ),
                        },
                        {
                            "title": "A reward for survey information",
                            "scenario": (
                                "A message offers a gift in return for detailed "
                                "personal or workplace information."
                            ),
                            "lesson": (
                                "Check the organisation and the data request "
                                "before responding."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "Help in exchange for access",
                            "scenario": (
                                "A person claiming to be a support contractor "
                                "offers to resolve a software issue if an "
                                "employee installs an unapproved remote-access tool."
                            ),
                            "investigation": (
                                "The employee contacts the official support "
                                "desk to verify the offer."
                            ),
                            "outcome": (
                                "The request is rejected because the contractor "
                                "and the software installation are unverified."
                            ),
                            "key_takeaway": (
                                "An attractive service offer should never bypass "
                                "approved technical procedures."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Free technical support",
                        "scenario": (
                            "A stranger offers to repair your computer for free "
                            "if you provide administrator access."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Grant access immediately.",
                            "Provide your password but supervise them.",
                            "Use an approved support provider and refuse unverified access.",
                            "Disable all security controls first.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Unverified support offers can be used to obtain "
                            "privileged access. Follow authorised support procedures."
                        ),
                    },
                    "practical_lab": {
                        "title": "Evaluate an offer-for-access request",
                        "objective": (
                            "Recognise when a promised benefit is being used "
                            "to obtain excessive access."
                        ),
                        "scenario": (
                            "A person offers a free service in exchange for "
                            "administrator credentials."
                        ),
                        "tasks": [
                            "Identify the benefit being offered.",
                            "Identify the information or access requested in return.",
                            "Assess whether the request follows approved procedures.",
                            "Choose a safe verification and reporting action.",
                        ],
                        "expected_outcome": (
                            "The learner recognises an unsafe exchange and "
                            "refuses unauthorised disclosure or access."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What is the central feature of quid pro quo?",
                            "options": [
                                "An offer or benefit in exchange for information or action",
                                "A computer hardware failure",
                                "A network routing error",
                                "An encrypted backup",
                            ],
                            "answer": 0,
                            "explanation": (
                                "Quid pro quo manipulates people through a "
                                "promised exchange."
                            ),
                        },
                        {
                            "question": "Someone offers to fix your computer if you share your password. What is safest?",
                            "options": [
                                "Share the password",
                                "Follow official support procedures and refuse to disclose credentials",
                                "Post the password in a support forum",
                                "Disable multi-factor authentication",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Passwords should remain private, and technical "
                                "support must be verified."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Free services linked to unusual requests.",
                        "Offers that require credentials or privileged access.",
                        "Requests to install unapproved software.",
                        "Pressure to act before checking authorisation.",
                    ],
                    "detection": [
                        "Check the identity of support staff and contractors.",
                        "Verify offers through official channels.",
                        "Review requests for privileged access.",
                        "Report suspicious exchanges to the security team.",
                    ],
                    "prevention": [
                        "Never trade credentials for a service or reward.",
                        "Use approved technical support providers.",
                        "Restrict administrator privileges.",
                        "Train staff to recognise manipulation tactics.",
                    ],
                    "impact": [
                        "Compromised accounts and devices.",
                        "Unauthorised remote access.",
                        "Data theft or malware infection.",
                        "Financial loss and service disruption.",
                    ],
                    "conclusion": (
                        "A promised benefit does not justify bypassing security "
                        "procedures. Verify the provider and protect access."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Secure Our World",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },
            },
        },

        "computer-based": {
            "id": "computer-based",
            "name": "Computer-Based Social Engineering",
            "description": (
                "Attacks that use email, websites, messaging, pop-ups, "
                "or other digital channels to manipulate users."
            ),
            "types": {
                "phishing": {
                    "id": "phishing",
                    "name": "Phishing",
                    "difficulty": "Beginner",
                    "summary": (
                        "Fraudulent messages attempt to trick users into "
                        "revealing information, opening malicious content, "
                        "or visiting deceptive websites."
                    ),
                    "overview": (
                        "Phishing commonly uses email, messaging, or other "
                        "digital communications to impersonate a trusted "
                        "organisation or person. Messages may imitate banks, "
                        "delivery companies, employers, or online services. "
                        "The goal is often to steal credentials, obtain "
                        "personal information, or deliver malware."
                    ),
                    "how_it_works": [
                        "The attacker sends a deceptive message that appears relevant or urgent.",
                        "The message asks the target to click a link, open an attachment, or provide information.",
                        "The target may reach a fake login page or unsafe download.",
                        "The attacker attempts to collect information or compromise the device or account.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "A fake account security alert",
                            "scenario": (
                                "An email claims an account will be suspended "
                                "unless the recipient signs in using the supplied link."
                            ),
                            "lesson": (
                                "Visit the service through its known official "
                                "website rather than the message link."
                            ),
                        },
                        {
                            "title": "A fraudulent delivery notification",
                            "scenario": (
                                "A message claims a parcel cannot be delivered "
                                "and requests personal information or a payment."
                            ),
                            "lesson": (
                                "Check delivery status through the courier's "
                                "official app or website."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The suspicious account notification",
                            "scenario": (
                                "An employee receives an email asking them to "
                                "sign in to review a supposed security incident."
                            ),
                            "investigation": (
                                "The employee notices an unfamiliar sender and "
                                "reports the email without opening its link."
                            ),
                            "outcome": (
                                "The security team reviews the message and "
                                "warns other employees if necessary."
                            ),
                            "key_takeaway": (
                                "Unexpected account alerts should be verified "
                                "independently before interacting with them."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Spot the phishing email",
                        "scenario": (
                            "You receive an unexpected message claiming your "
                            "account will close today. It contains a link and "
                            "asks you to enter your password."
                        ),
                        "question": "What is the safest action?",
                        "options": [
                            "Click the link immediately.",
                            "Reply with your password.",
                            "Open the official website separately and report the suspicious message.",
                            "Forward the link to friends to test it.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Urgency and unexpected login links are warning "
                            "signs. Verify the issue through an official channel."
                        ),
                    },
                    "practical_lab": {
                        "title": "Phishing message analysis",
                        "objective": (
                            "Identify suspicious features in a simulated message."
                        ),
                        "scenario": (
                            "Review a fictional account-alert message that "
                            "contains an unexpected link and an urgent request."
                        ),
                        "tasks": [
                            "Identify the sender and any inconsistencies.",
                            "Highlight urgent language or unusual requests.",
                            "Explain why the link should not be trusted automatically.",
                            "Choose a safe reporting and verification procedure.",
                        ],
                        "expected_outcome": (
                            "The learner recognises phishing indicators and "
                            "responds without opening suspicious links or "
                            "disclosing credentials."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What is phishing primarily designed to do?",
                            "options": [
                                "Improve email delivery",
                                "Manipulate users into revealing information or taking unsafe actions",
                                "Repair damaged hardware",
                                "Increase network bandwidth",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Phishing uses deceptive communications to "
                                "steal information or persuade users to perform unsafe actions."
                            ),
                        },
                        {
                            "question": "An email asks you to verify your account through an unexpected link. What should you do?",
                            "options": [
                                "Enter your credentials",
                                "Download every attachment",
                                "Visit the official website independently and report the message",
                                "Reply with your authentication code",
                            ],
                            "answer": 2,
                            "explanation": (
                                "Independent verification avoids relying on a "
                                "potentially fraudulent link."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Unexpected requests for credentials or personal information.",
                        "Urgent threats or unusual rewards.",
                        "Mismatched sender addresses or suspicious domains.",
                        "Unexpected attachments or shortened links.",
                        "Requests to bypass normal procedures.",
                    ],
                    "detection": [
                        "Check sender details and domain names carefully.",
                        "Use approved phishing-reporting tools.",
                        "Inspect unexpected requests through a separate channel.",
                        "Keep email filtering and endpoint protection updated.",
                    ],
                    "prevention": [
                        "Use multi-factor authentication.",
                        "Avoid opening unexpected attachments or links.",
                        "Use unique passwords and a password manager.",
                        "Keep operating systems and applications updated.",
                        "Report suspicious messages promptly.",
                    ],
                    "impact": [
                        "Credential theft.",
                        "Malware infections.",
                        "Financial fraud.",
                        "Exposure of personal or organisational data.",
                    ],
                    "conclusion": (
                        "Phishing is easier to prevent when users pause, "
                        "verify unexpected requests, and report suspicious messages."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Recognise and Report Phishing",
                            "url": "https://www.cisa.gov/secure-our-world/recognize-and-report-phishing",
                        },
                    ],
                },

                "email-spoofing": {
                    "id": "email-spoofing",
                    "name": "Email Spoofing",
                    "difficulty": "Intermediate",
                    "summary": (
                        "An email is made to appear as though it came from "
                        "a different sender or organisation."
                    ),
                    "overview": (
                        "Email spoofing involves falsifying sender information "
                        "so a message appears to originate from a trusted source. "
                        "It is often used in phishing and business email fraud. "
                        "The displayed sender name alone is not reliable proof "
                        "of the message's authenticity."
                    ),
                    "how_it_works": [
                        "The sender information is falsified or made misleading.",
                        "The message is designed to resemble a trusted communication.",
                        "The recipient is encouraged to trust the apparent sender.",
                        "The attacker may request a payment, sensitive data, or an unsafe action.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "A message that appears to come from management",
                            "scenario": (
                                "An employee receives a message with a familiar "
                                "display name requesting a confidential file."
                            ),
                            "lesson": (
                                "Verify unusual requests through a separate "
                                "channel rather than relying on the display name."
                            ),
                        },
                        {
                            "title": "A fake supplier invoice",
                            "scenario": (
                                "A finance team receives an invoice message "
                                "that appears to come from a known supplier."
                            ),
                            "lesson": (
                                "Verify payment details and sender authenticity "
                                "using the established supplier records."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The altered payment request",
                            "scenario": (
                                "An organisation receives an email apparently "
                                "from a supplier asking for a bank-account change."
                            ),
                            "investigation": (
                                "Finance staff independently contact the supplier "
                                "using existing contact information."
                            ),
                            "outcome": (
                                "The supplier denies making the request, and "
                                "the suspicious message is escalated."
                            ),
                            "key_takeaway": (
                                "Payment changes require independent verification."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Can you trust the sender name?",
                        "scenario": (
                            "A message appears to come from your manager but "
                            "requests an urgent transfer to a new account."
                        ),
                        "question": "What is the safest next step?",
                        "options": [
                            "Transfer the money immediately.",
                            "Reply to the email asking for confirmation.",
                            "Verify the request through a known, independent contact method.",
                            "Ignore all payment procedures.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Sender names can be misleading. Confirm sensitive "
                            "requests independently and follow payment controls."
                        ),
                    },
                    "practical_lab": {
                        "title": "Sender authenticity review",
                        "objective": (
                            "Assess a simulated message for signs of sender deception."
                        ),
                        "scenario": (
                            "Review a fictional email requesting a confidential "
                            "document from a familiar display name."
                        ),
                        "tasks": [
                            "Compare the displayed name with the actual sender address.",
                            "Identify unexpected or unusual requests.",
                            "Determine how to verify the sender independently.",
                            "Record the suspicious indicators for the security team.",
                        ],
                        "expected_outcome": (
                            "The learner avoids trusting display names alone "
                            "and follows verification procedures."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What is email spoofing?",
                            "options": [
                                "Falsifying sender information to make a message appear to come from another source",
                                "Compressing email attachments",
                                "Blocking every email",
                                "Encrypting a hard drive",
                            ],
                            "answer": 0,
                            "explanation": (
                                "Email spoofing makes the apparent sender "
                                "different from the actual origin or authorised source."
                            ),
                        },
                        {
                            "question": "An apparent manager requests an urgent transfer. What should you do?",
                            "options": [
                                "Transfer funds based on the display name",
                                "Verify the request independently and follow financial controls",
                                "Share your banking password",
                                "Disable email filtering",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Sensitive financial requests must be independently "
                                "verified, even when the sender appears familiar."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Display names that do not match the sender address.",
                        "Unusual payment or information requests.",
                        "Unexpected changes to supplier bank details.",
                        "Pressure to avoid normal approval processes.",
                    ],
                    "detection": [
                        "Review sender addresses and message headers where appropriate.",
                        "Use email authentication controls such as SPF, DKIM, and DMARC.",
                        "Verify financial changes independently.",
                        "Report suspicious messages to IT or security.",
                    ],
                    "prevention": [
                        "Configure appropriate email authentication.",
                        "Use multi-person approval for high-risk payments.",
                        "Maintain trusted supplier contact records.",
                        "Train staff to recognise sender deception.",
                    ],
                    "impact": [
                        "Financial fraud.",
                        "Exposure of confidential information.",
                        "Compromised accounts.",
                        "Loss of customer and supplier trust.",
                    ],
                    "conclusion": (
                        "An email's displayed sender is not sufficient proof "
                        "of identity. Authenticate messages and verify sensitive requests."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Secure Our World",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },

                "fake-websites": {
                    "id": "fake-websites",
                    "name": "Fake Websites",
                    "difficulty": "Beginner",
                    "summary": (
                        "Deceptive websites imitate legitimate services to "
                        "collect credentials, payment details, or personal information."
                    ),
                    "overview": (
                        "Fake websites are designed to look like trusted "
                        "websites, including banks, shopping services, and "
                        "workplace portals. They may use misleading domain "
                        "names, copied logos, or fraudulent login forms. "
                        "A professional appearance does not prove a website "
                        "is legitimate."
                    ),
                    "how_it_works": [
                        "An attacker creates a website that imitates a legitimate service.",
                        "The victim is directed to it through a message, advertisement, or misleading search result.",
                        "The victim may enter credentials, payment details, or personal information.",
                        "The attacker attempts to misuse the submitted information.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "A fake banking login",
                            "scenario": (
                                "A message directs a customer to a website "
                                "whose address resembles their bank's domain."
                            ),
                            "lesson": (
                                "Use a saved bookmark or the bank's official "
                                "app rather than an unexpected message link."
                            ),
                        },
                        {
                            "title": "A fraudulent shopping offer",
                            "scenario": (
                                "A website offers popular products at unusually "
                                "low prices but provides no verifiable business details."
                            ),
                            "lesson": (
                                "Check the retailer's reputation, contact details, "
                                "payment protections, and return policy."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The imitation login page",
                            "scenario": (
                                "A user receives an account notification and "
                                "lands on a login page that resembles a familiar service."
                            ),
                            "investigation": (
                                "The user notices that the domain differs from "
                                "the known official address."
                            ),
                            "outcome": (
                                "The user closes the page and reports the link "
                                "without entering credentials."
                            ),
                            "key_takeaway": (
                                "Check the domain before entering sensitive information."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "Choose the trustworthy login route",
                        "scenario": (
                            "A message links to a login page with a familiar logo "
                            "but an unfamiliar web address."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Enter your password because the logo looks correct.",
                            "Use the official app or a known website address.",
                            "Reuse a password from another account.",
                            "Enter your password and check the address later.",
                        ],
                        "correct_answer": 1,
                        "explanation": (
                            "Visual appearance can be copied. Navigate through "
                            "a known official route before signing in."
                        ),
                    },
                    "practical_lab": {
                        "title": "Website trust assessment",
                        "objective": (
                            "Evaluate the visible trust indicators of a fictional website."
                        ),
                        "scenario": (
                            "Review a fictional shopping or login page supplied "
                            "as a classroom exercise."
                        ),
                        "tasks": [
                            "Inspect the domain and spelling.",
                            "Identify unexpected requests for sensitive information.",
                            "Check for verifiable contact and business details.",
                            "Decide whether to proceed, verify independently, or report the site.",
                        ],
                        "expected_outcome": (
                            "The learner recognises suspicious website indicators "
                            "without submitting real personal information."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "Why do attackers create fake websites?",
                            "options": [
                                "To improve legitimate website performance",
                                "To deceive visitors into sharing information or making payments",
                                "To install approved software updates",
                                "To improve password security",
                            ],
                            "answer": 1,
                            "explanation": (
                                "Fake websites often imitate trusted services "
                                "to collect sensitive information or money."
                            ),
                        },
                        {
                            "question": "A login page looks genuine but has an unfamiliar domain. What should you do?",
                            "options": [
                                "Enter your credentials",
                                "Use a known official address or app instead",
                                "Share the link with colleagues",
                                "Ignore the domain name",
                            ],
                            "answer": 1,
                            "explanation": (
                                "An unfamiliar domain is a reason to stop and "
                                "verify the service before entering information."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Misspelled or misleading domain names.",
                        "Unusually low prices or unrealistic offers.",
                        "Missing or unverifiable contact information.",
                        "Unexpected requests for credentials or payment.",
                        "Links received through unsolicited messages.",
                    ],
                    "detection": [
                        "Check the full domain name carefully.",
                        "Use trusted bookmarks and official apps.",
                        "Search for independent information about unfamiliar retailers.",
                        "Report suspected fraudulent websites.",
                    ],
                    "prevention": [
                        "Use unique passwords and multi-factor authentication.",
                        "Keep browsers and security software updated.",
                        "Avoid signing in through unexpected links.",
                        "Use protected payment methods and trusted retailers.",
                    ],
                    "impact": [
                        "Credential theft.",
                        "Payment fraud.",
                        "Identity theft.",
                        "Exposure of personal and financial data.",
                    ],
                    "conclusion": (
                        "Do not judge a website by its appearance alone. "
                        "Verify its address and legitimacy before submitting information."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Recognise and Report Phishing",
                            "url": "https://www.cisa.gov/secure-our-world/recognize-and-report-phishing",
                        },
                    ],
                },

                "pop-up-scams": {
                    "id": "pop-up-scams",
                    "name": "Pop-up Scams",
                    "difficulty": "Beginner",
                    "summary": (
                        "Misleading pop-up messages attempt to frighten users "
                        "or persuade them to install software, call fake support, "
                        "or disclose information."
                    ),
                    "overview": (
                        "Pop-up scams often use alarming messages such as "
                        "'your device is infected' or claims that an account "
                        "requires immediate action. The message may imitate "
                        "system warnings, advertise fraudulent support, or "
                        "push users towards unsafe downloads."
                    ),
                    "how_it_works": [
                        "A misleading pop-up appears while the user browses or uses an application.",
                        "The message creates fear, urgency, or confusion.",
                        "The user is encouraged to call a number, install software, or disclose information.",
                        "The attacker attempts to obtain money, access, or sensitive information.",
                    ],
                    "real_world_examples": [
                        {
                            "title": "A fake virus warning",
                            "scenario": (
                                "A browser page displays a warning claiming "
                                "that the computer is infected and gives a phone number."
                            ),
                            "lesson": (
                                "Do not call the number shown in an unexpected "
                                "warning. Close the page safely and use trusted security tools."
                            ),
                        },
                        {
                            "title": "A fake update prompt",
                            "scenario": (
                                "A pop-up claims a video cannot play until "
                                "an unfamiliar application is installed."
                            ),
                            "lesson": (
                                "Get updates through the operating system or "
                                "the application's official source."
                            ),
                        },
                    ],
                    "case_studies": [
                        {
                            "title": "The alarming browser warning",
                            "scenario": (
                                "A user sees a full-screen warning claiming "
                                "their computer is locked and instructing them "
                                "to contact support."
                            ),
                            "investigation": (
                                "The user avoids calling the number and follows "
                                "the organisation's approved procedure for "
                                "closing and reporting suspicious browser content."
                            ),
                            "outcome": (
                                "The user avoids disclosing information or "
                                "paying a fraudulent support service."
                            ),
                            "key_takeaway": (
                                "A web page can imitate a system warning. "
                                "Verify alerts through trusted security tools."
                            ),
                        }
                    ],
                    "simulation": {
                        "title": "The fake infection warning",
                        "scenario": (
                            "A pop-up claims your files will be deleted unless "
                            "you call a support number immediately."
                        ),
                        "question": "What is the safest response?",
                        "options": [
                            "Call the displayed number immediately.",
                            "Pay to remove the warning.",
                            "Avoid the supplied contact details and use trusted security procedures.",
                            "Install the recommended unknown program.",
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "Scare tactics are common in pop-up scams. "
                            "Use trusted security software and official support channels."
                        ),
                    },
                    "practical_lab": {
                        "title": "Analyse a simulated browser alert",
                        "objective": (
                            "Distinguish a misleading pop-up from a verified security notification."
                        ),
                        "scenario": (
                            "A fictional browser screenshot displays an urgent "
                            "infection warning and an unfamiliar support number."
                        ),
                        "tasks": [
                            "Identify the warning's fear-based language.",
                            "Identify the requested action and potential risk.",
                            "Choose a safe way to close or report the alert.",
                            "Describe how to verify a real security problem.",
                        ],
                        "expected_outcome": (
                            "The learner avoids the supplied phone number and "
                            "unknown downloads and verifies the issue independently."
                        ),
                    },
                    "assessment": [
                        {
                            "question": "What tactic is commonly used by pop-up scams?",
                            "options": [
                                "Fear and urgency",
                                "Routine software documentation",
                                "Scheduled backups",
                                "Normal account settings",
                            ],
                            "answer": 0,
                            "explanation": (
                                "Pop-up scams often frighten users into acting "
                                "before they can verify the warning."
                            ),
                        },
                        {
                            "question": "A pop-up asks you to call an unfamiliar number to remove a virus. What should you do?",
                            "options": [
                                "Call immediately",
                                "Provide remote access",
                                "Avoid the number and use trusted security tools or official support",
                                "Pay before checking the warning",
                            ],
                            "answer": 2,
                            "explanation": (
                                "Unexpected support numbers may lead to fraudulent "
                                "services. Verify security issues independently."
                            ),
                        },
                    ],
                    "warning_signs": [
                        "Alarming warnings from an unfamiliar web page.",
                        "Countdown timers or threats of immediate data loss.",
                        "Requests to call an unverified support number.",
                        "Instructions to install unfamiliar applications.",
                    ],
                    "detection": [
                        "Check alerts through trusted operating-system security tools.",
                        "Avoid interacting with suspicious pop-up controls.",
                        "Use approved browser and endpoint protection.",
                        "Report repeated suspicious alerts to IT or security.",
                    ],
                    "prevention": [
                        "Keep browsers and operating systems updated.",
                        "Use reputable security software.",
                        "Avoid untrusted downloads and websites.",
                        "Use official support channels.",
                    ],
                    "impact": [
                        "Financial fraud.",
                        "Installation of unwanted or malicious software.",
                        "Unauthorised remote access.",
                        "Loss of personal information.",
                    ],
                    "conclusion": (
                        "Unexpected warnings should prompt verification, "
                        "not panic. Use trusted tools rather than numbers or "
                        "downloads supplied by the pop-up."
                    ),
                    "learning_resources": [
                        {
                            "title": "CISA: Secure Our World",
                            "url": "https://www.cisa.gov/secure-our-world",
                        },
                    ],
                },
            },
        },
    },
}