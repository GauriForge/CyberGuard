
SPYWARE_SURVEILLANCE = {
    "id": "spyware-surveillance",
    "name": "Spyware and Surveillance",
    "description": (
        "Understand spyware, unauthorized monitoring, tracking technologies, "
        "and the methods used to protect personal and organizational privacy."
    ),
    "types": {
        "computer_based": {
            "id": "computer-based",
            "name": "Computer-Based Spyware and Surveillance",
            "description": (
                "Threats that use software, devices, or digital services "
                "to collect information without appropriate consent."
            ),
            "types": {
                "keyloggers": {
                    "id": "keyloggers",
                    "name": "Keyloggers",
                    "overview": (
                        "Keyloggers record keyboard input. Malicious versions "
                        "may capture passwords, private messages, and other "
                        "sensitive information without the user's knowledge."
                    ),
                    "how_it_works": [
                        "A keylogger reaches a device through malicious software, "
                        "an unsafe download, or unauthorized physical access.",
                        "It records keyboard input or other selected activity.",
                        "Captured information may be stored locally or transmitted "
                        "to an unauthorized recipient."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Stolen login credentials",
                            "content": (
                                "An employee installs an unverified utility that "
                                "secretly records keystrokes. The collected "
                                "credentials are later used in an attempted "
                                "account compromise."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Compromised Office Computer",
                        "content": (
                            "An organization notices suspicious logins to several "
                            "employee accounts. An investigation finds that an "
                            "unauthorized program had been installed on a shared "
                            "computer. Investigators isolate the device, preserve "
                            "evidence, reset affected credentials, and review "
                            "account activity."
                        ),
                        "discussion": [
                            "Which warning signs could have exposed the incident?",
                            "Why should the affected device be isolated?",
                            "What additional controls could prevent a recurrence?"
                        ]
                    },
                    "simulation": {
                        "title": "Recognize a Keylogger Incident",
                        "scenario": (
                            "A computer becomes unusually slow after an employee "
                            "installs software from an unfamiliar website. Soon "
                            "afterward, the employee receives alerts about "
                            "unrecognized login attempts."
                        ),
                        "tasks": [
                            "Identify the suspicious indicators.",
                            "Choose the safest immediate response.",
                            "Decide which accounts and devices require investigation."
                        ],
                        "expected_outcome": (
                            "The learner identifies possible credential theft, "
                            "reports the incident, and follows the organization's "
                            "device-isolation and account-recovery procedures."
                        )
                    },
                    "practical_lab": {
                        "title": "Keylogger Detection and Response",
                        "mode": "defensive",
                        "steps": [
                            "Inspect a provided, harmless sample of process and "
                            "security-alert logs.",
                            "Identify unfamiliar processes and suspicious "
                            "persistence indicators.",
                            "Document the evidence without executing suspicious files.",
                            "Recommend containment and credential-protection steps."
                        ],
                        "expected_result": (
                            "A short incident report identifying suspicious "
                            "indicators and appropriate defensive actions."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the primary purpose of a malicious keylogger?",
                            "options": [
                                "To improve typing speed",
                                "To record keyboard input without authorization",
                                "To update the operating system",
                                "To encrypt every file automatically"
                            ],
                            "answer": 1,
                            "explanation": (
                                "A malicious keylogger records keyboard input "
                                "to obtain information such as credentials."
                            )
                        },
                        {
                            "question": "What should you do if a device may contain a keylogger?",
                            "options": [
                                "Enter all passwords again",
                                "Ignore the warning",
                                "Follow incident-response procedures and protect affected accounts",
                                "Disable every security control"
                            ],
                            "answer": 2,
                            "explanation": (
                                "The device should be investigated safely, and "
                                "potentially exposed accounts should be protected."
                            )
                        }
                    ],
                    "prevention": [
                        "Install software only from trusted sources.",
                        "Keep operating systems and security tools updated.",
                        "Use multifactor authentication where possible.",
                        "Investigate unexpected security alerts promptly."
                    ],
                    "conclusion": (
                        "Keyloggers can expose sensitive information. Safe "
                        "software practices, monitoring, and timely incident "
                        "response reduce the risk."
                    )
                },

                "screen_monitoring_spyware": {
                    "id": "screen-monitoring-spyware",
                    "name": "Screen Monitoring Spyware",
                    "overview": (
                        "Screen-monitoring spyware captures screenshots or "
                        "observes on-screen activity without appropriate "
                        "authorization. It may expose confidential documents, "
                        "messages, and business information."
                    ),
                    "how_it_works": [
                        "A monitoring component is installed or abused on a device.",
                        "It captures selected screen activity.",
                        "The collected information may be stored or sent elsewhere."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Exposure of confidential documents",
                            "content": (
                                "A compromised workstation captures screens "
                                "containing customer information. The organization "
                                "investigates the device and checks whether "
                                "sensitive information was exposed."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Unexpected Monitoring on a Workstation",
                        "content": (
                            "A staff member discovers an unfamiliar monitoring "
                            "application. The security team checks whether it was "
                            "authorized, reviews its permissions, and investigates "
                            "any unexplained data transfers."
                        ),
                        "discussion": [
                            "How can legitimate monitoring be distinguished from spyware?",
                            "Why do authorization and transparency matter?",
                            "What evidence should the security team preserve?"
                        ]
                    },
                    "simulation": {
                        "title": "Investigate Suspicious Screen Capture",
                        "scenario": (
                            "A workstation has an unfamiliar application with "
                            "screen-recording permissions and unexpected network activity."
                        ),
                        "tasks": [
                            "Review the available application and network logs.",
                            "Determine whether the behavior has an approved business purpose.",
                            "Recommend safe containment and investigation steps."
                        ],
                        "expected_outcome": (
                            "The learner identifies suspicious monitoring behavior "
                            "and recommends a documented defensive investigation."
                        )
                    },
                    "practical_lab": {
                        "title": "Review Screen-Recording Permissions",
                        "mode": "defensive",
                        "steps": [
                            "Review a sample inventory of installed applications.",
                            "Identify applications with screen-capture permissions.",
                            "Compare each application with the approved software list.",
                            "Document unnecessary permissions and recommended actions."
                        ],
                        "expected_result": (
                            "A permission-review report identifying applications "
                            "that require verification."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What information could screen-monitoring spyware expose?",
                            "options": [
                                "Only the computer's wallpaper",
                                "Confidential information displayed on screen",
                                "Only public weather information",
                                "Nothing sensitive"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Screen captures can reveal messages, documents, "
                                "credentials, and other sensitive information."
                            )
                        }
                    ],
                    "prevention": [
                        "Review application permissions regularly.",
                        "Restrict installation of unauthorized applications.",
                        "Monitor unusual application and network behavior.",
                        "Use transparent, approved monitoring policies."
                    ],
                    "conclusion": (
                        "Screen monitoring becomes a security threat when it "
                        "collects information without proper authorization. "
                        "Permission reviews and endpoint monitoring help detect abuse."
                    )
                },

                "browser_spyware": {
                    "id": "browser-spyware",
                    "name": "Browser Spyware and Tracking",
                    "overview": (
                        "Browser spyware may monitor browsing activity, collect "
                        "search information, modify browser settings, or redirect "
                        "users to unwanted websites. Not every tracking cookie "
                        "is malicious; context and consent matter."
                    ),
                    "how_it_works": [
                        "An unwanted extension or application gains browser access.",
                        "It collects browsing information or changes browser behavior.",
                        "Collected data may be used for unauthorized tracking or abuse."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unwanted Browser Extension",
                            "content": (
                                "A user installs an extension that requests "
                                "unnecessary permissions. Later, unexpected "
                                "redirects and unfamiliar search settings prompt "
                                "a security review."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Browser That Would Not Behave",
                        "content": (
                            "Several users report search redirects after installing "
                            "a free browser add-on. The support team checks "
                            "extensions, removes unauthorized software, and reviews "
                            "browser policies."
                        ),
                        "discussion": [
                            "Which extension permissions are excessive?",
                            "How can an organization reduce extension-related risks?",
                            "Why should browser settings be checked after removal?"
                        ]
                    },
                    "simulation": {
                        "title": "Investigate an Unwanted Extension",
                        "scenario": (
                            "A browser repeatedly redirects searches and contains "
                            "an extension the user does not recognize."
                        ),
                        "tasks": [
                            "Review the extension's name and permissions.",
                            "Check whether it is approved.",
                            "Select safe removal and reporting actions."
                        ],
                        "expected_outcome": (
                            "The learner identifies a suspicious extension and "
                            "describes a safe remediation process."
                        )
                    },
                    "practical_lab": {
                        "title": "Browser Extension Security Review",
                        "mode": "defensive",
                        "steps": [
                            "Inspect a supplied list of browser extensions.",
                            "Flag unfamiliar extensions and excessive permissions.",
                            "Check the approved-extension policy.",
                            "Write recommendations for removal or further investigation."
                        ],
                        "expected_result": (
                            "A browser security checklist with justified findings."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is a sensible response to an unfamiliar browser extension?",
                            "options": [
                                "Grant it every permission",
                                "Check its source, permissions, and approval status",
                                "Share passwords with its developer",
                                "Ignore all browser warnings"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Checking the source, permissions, and approval "
                                "status helps identify potentially unsafe extensions."
                            )
                        }
                    ],
                    "prevention": [
                        "Install extensions only when necessary and from trusted sources.",
                        "Review permissions before installation.",
                        "Remove unauthorized extensions.",
                        "Keep browsers updated and use organizational browser policies."
                    ],
                    "conclusion": (
                        "Careful extension management and permission reviews "
                        "reduce unwanted browser tracking and related risks."
                    )
                },

                "remote_access_spyware": {
                    "id": "remote-access-spyware",
                    "name": "Unauthorized Remote Monitoring",
                    "overview": (
                        "Remote monitoring tools can become spyware when "
                        "installed or used without the device owner's "
                        "authorization. They may allow an outsider to observe "
                        "activity or access sensitive information."
                    ),
                    "how_it_works": [
                        "An unauthorized remote-access component is installed or abused.",
                        "The component communicates with a remote operator.",
                        "The operator may attempt to observe activity or access data."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unapproved Remote-Access Tool",
                            "content": (
                                "An employee finds remote-access software that "
                                "was never approved by the IT team. Security staff "
                                "verify the installation and investigate its activity."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Unexpected Remote Access",
                        "content": (
                            "A workstation shows unexplained remote sessions. "
                            "Investigators review access logs, confirm the source "
                            "of the sessions, revoke unauthorized access, and "
                            "strengthen authentication."
                        ),
                        "discussion": [
                            "Which logs can help establish who accessed the device?",
                            "Why should remote access be restricted?",
                            "How can future unauthorized sessions be detected?"
                        ]
                    },
                    "simulation": {
                        "title": "Respond to an Unknown Remote Session",
                        "scenario": (
                            "A user reports an unexpected remote-control notification "
                            "on a work computer."
                        ),
                        "tasks": [
                            "Identify immediate containment options.",
                            "Determine what access logs should be reviewed.",
                            "Recommend account and device recovery actions."
                        ],
                        "expected_outcome": (
                            "The learner follows a defensive incident-response "
                            "process without attempting unauthorized access."
                        )
                    },
                    "practical_lab": {
                        "title": "Review Remote-Access Logs",
                        "mode": "defensive",
                        "steps": [
                            "Examine sample remote-session logs.",
                            "Identify unfamiliar accounts, devices, or session times.",
                            "Compare findings against approved access records.",
                            "Write a concise incident report."
                        ],
                        "expected_result": (
                            "A documented assessment of suspicious remote-access activity."
                        )
                    },
                    "assessment": [
                        {
                            "question": "When does remote-monitoring software become a security threat?",
                            "options": [
                                "Whenever a computer is online",
                                "When it is installed or used without proper authorization",
                                "Whenever software is updated",
                                "When a user locks the screen"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Unauthorized monitoring can violate privacy and "
                                "provide access to sensitive information."
                            )
                        }
                    ],
                    "prevention": [
                        "Allow only approved remote-access tools.",
                        "Require strong authentication and least-privilege access.",
                        "Review remote-session logs.",
                        "Disable unused remote-access services."
                    ],
                    "conclusion": (
                        "Remote-access controls, reliable logging, and prompt "
                        "investigation help prevent unauthorized monitoring."
                    )
                }
            }
        },

        "human_based": {
            "id": "human-based",
            "name": "Human-Based Surveillance and Privacy Abuse",
            "description": (
                "Threats in which a person misuses access, trust, or physical "
                "observation to monitor another person without appropriate consent."
            ),
            "types": {
                "stalkerware": {
                    "id": "stalkerware",
                    "name": "Stalkerware and Non-Consensual Monitoring",
                    "overview": (
                        "Stalkerware refers to tools or applications used to "
                        "monitor another person's device or activity without "
                        "their informed consent. It may be associated with "
                        "harassment, coercive control, or privacy abuse."
                    ),
                    "how_it_works": [
                        "A person obtains physical or account access to a device.",
                        "Monitoring software or account-sharing features are misused.",
                        "Private activity or location information may be observed."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Unexpected Knowledge of Private Activity",
                            "content": (
                                "A person repeatedly refers to private messages or "
                                "movements they should not know about. The affected "
                                "individual seeks support and reviews account "
                                "security from a device they trust."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Privacy Without Consent",
                        "content": (
                            "An individual suspects that a partner is monitoring "
                            "their phone. Because changing settings could alert "
                            "the other person, they seek advice from a trusted "
                            "support service and plan safe next steps."
                        ),
                        "discussion": [
                            "Why might immediate removal of suspected software be risky?",
                            "How can a person seek help while protecting their safety?",
                            "What does informed consent mean in digital monitoring?"
                        ]
                    },
                    "simulation": {
                        "title": "Respond Safely to Suspected Stalkerware",
                        "scenario": (
                            "A person notices unexplained account activity and "
                            "suspects someone close to them is monitoring their device."
                        ),
                        "tasks": [
                            "Identify safe ways to seek help.",
                            "Consider the risks of changing settings on the monitored device.",
                            "Create a safety-conscious account-security plan."
                        ],
                        "expected_outcome": (
                            "The learner prioritizes personal safety, trusted support, "
                            "and careful investigation."
                        )
                    },
                    "practical_lab": {
                        "title": "Privacy and Account-Security Checklist",
                        "mode": "defensive",
                        "steps": [
                            "Review a fictional account-security report.",
                            "Identify unfamiliar sessions and shared access.",
                            "List safe ways to secure accounts from a trusted device.",
                            "Prepare a privacy-protection recommendation."
                        ],
                        "expected_result": (
                            "A safety-conscious checklist for reviewing account access."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the priority when someone suspects non-consensual monitoring by a partner?",
                            "options": [
                                "Confront the person immediately in every case",
                                "Prioritize personal safety and seek trusted support",
                                "Ignore all warning signs",
                                "Delete all evidence immediately"
                            ],
                            "answer": 1,
                            "explanation": (
                                "The safest response depends on the situation; "
                                "personal safety and trusted support should come first."
                            )
                        }
                    ],
                    "prevention": [
                        "Use unique passwords and multifactor authentication where safe.",
                        "Review account sessions and location-sharing settings when safe to do so.",
                        "Seek trusted professional support if monitoring may involve abuse.",
                        "Preserve relevant evidence when doing so does not increase risk."
                    ],
                    "conclusion": (
                        "Non-consensual monitoring is a privacy and safety issue. "
                        "Support and careful safety planning are more important "
                        "than rushing to change a device."
                    )
                },

                "unauthorized_physical_observation": {
                    "id": "unauthorized-physical-observation",
                    "name": "Unauthorized Physical Observation",
                    "overview": (
                        "Physical observation becomes a privacy concern when "
                        "someone deliberately watches, records, or follows "
                        "another person in ways that violate privacy, consent, "
                        "or applicable law."
                    ),
                    "how_it_works": [
                        "A person observes activity in a private or sensitive context.",
                        "Information may be recorded or shared without permission.",
                        "The information may be used for harassment or other abuse."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Recording in a Private Space",
                            "content": (
                                "A person discovers an unfamiliar recording device "
                                "in a private area. They avoid tampering with "
                                "potential evidence and report the matter to "
                                "appropriate authorities or property management."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "An Unfamiliar Recording Device",
                        "content": (
                            "A visitor notices a device positioned to capture "
                            "a private area. The responsible staff member documents "
                            "the discovery, restricts access if appropriate, and "
                            "escalates the incident for a lawful investigation."
                        ),
                        "discussion": [
                            "Why is privacy context important?",
                            "Why should the discovery be documented?",
                            "Who should handle the investigation?"
                        ]
                    },
                    "simulation": {
                        "title": "Handle a Privacy Incident",
                        "scenario": (
                            "A staff member reports a suspected unauthorized "
                            "recording device in a sensitive area."
                        ),
                        "tasks": [
                            "Identify the immediate privacy and safety concerns.",
                            "Choose appropriate reporting and evidence-preservation steps.",
                            "Recommend a review of access and privacy controls."
                        ],
                        "expected_outcome": (
                            "The learner documents and reports the concern "
                            "without unnecessarily disturbing possible evidence."
                        )
                    },
                    "practical_lab": {
                        "title": "Physical Privacy Risk Assessment",
                        "mode": "defensive",
                        "steps": [
                            "Review a fictional floor plan and privacy policy.",
                            "Identify locations where recording would be inappropriate.",
                            "Recommend signage, access controls, and reporting procedures.",
                            "Prepare a short risk assessment."
                        ],
                        "expected_result": (
                            "A practical privacy-risk report with appropriate safeguards."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is an appropriate response to discovering a suspected unauthorized recording device?",
                            "options": [
                                "Publish photos of everyone nearby",
                                "Document and report the discovery through appropriate channels",
                                "Ignore it regardless of context",
                                "Destroy it immediately in every situation"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Documenting and reporting the discovery supports "
                                "a safe and appropriate investigation."
                            )
                        }
                    ],
                    "prevention": [
                        "Apply clear recording and privacy policies.",
                        "Restrict access to sensitive areas.",
                        "Provide a safe reporting process.",
                        "Investigate privacy complaints promptly and lawfully."
                    ],
                    "conclusion": (
                        "Respect for consent, privacy rules, and appropriate "
                        "reporting helps prevent and address physical surveillance abuse."
                    )
                }
            }
        }
    }
}