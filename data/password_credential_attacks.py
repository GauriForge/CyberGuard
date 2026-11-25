
PASSWORD_CREDENTIAL_ATTACKS = {
    "id": "password-credential",
    "name": "Password and Credential Attacks",
    "description": (
        "Learn how attackers compromise passwords, steal authentication "
        "information, and exploit weaknesses in account security."
    ),

    "subcategories": {
        "password_based": {
            "id": "password-based",
            "name": "Password-Based Attacks",
            "description": (
                "Attacks that target passwords through guessing, reuse, "
                "or weaknesses in password creation and storage."
            ),

            "types": {
                "brute_force_attack": {
                    "id": "brute-force-attack",
                    "name": "Brute Force Attack",

                    "overview": (
                        "A brute force attack involves repeatedly trying "
                        "different password combinations until the correct "
                        "one is discovered. Weak passwords and missing "
                        "login protections make these attacks easier."
                    ),

                    "how_it_works": [
                        "An attacker identifies a login page or password-protected account.",
                        "Automated attempts test possible password combinations.",
                        "Weak passwords may be discovered if attempts are not adequately restricted.",
                        "Successful access can expose personal information or allow account misuse."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Repeated attempts against an email account",
                            "scenario": (
                                "An email service detects hundreds of failed "
                                "login attempts against an account. The owner "
                                "uses a short, predictable password, making "
                                "the account more vulnerable."
                            ),
                            "lesson": (
                                "Use long, unique passwords and enable "
                                "multifactor authentication."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "The Account That Had No Login Limits",
                        "scenario": (
                            "A fictional company allows unlimited password "
                            "attempts. Several employee accounts receive "
                            "large numbers of failed login requests."
                        ),
                        "problem": (
                            "The company has no effective rate limiting, "
                            "alerting, or multifactor authentication."
                        ),
                        "response": [
                            "Introduce rate limiting and progressive delays.",
                            "Enable multifactor authentication.",
                            "Alert users about suspicious login activity.",
                            "Review authentication logs for compromised accounts."
                        ],
                        "key_learning": (
                            "Password strength matters, but login protections "
                            "are equally important."
                        )
                    },

                    "simulation": {
                        "title": "Recognise a Brute Force Attempt",
                        "objective": (
                            "Identify suspicious login patterns from a "
                            "fictional authentication log."
                        ),
                        "steps": [
                            "Review the sample events below.",
                            "Count the repeated failed attempts.",
                            "Identify the account that requires investigation.",
                            "Choose suitable defensive actions."
                        ],
                        "sample_events": [
                            {
                                "time": "09:00",
                                "account": "employee01",
                                "result": "Failed login"
                            },
                            {
                                "time": "09:01",
                                "account": "employee01",
                                "result": "Failed login"
                            },
                            {
                                "time": "09:02",
                                "account": "employee01",
                                "result": "Failed login"
                            },
                            {
                                "time": "09:03",
                                "account": "employee01",
                                "result": "Successful login"
                            }
                        ],
                        "question": (
                            "Which pattern most strongly suggests that "
                            "the account needs investigation?"
                        ),
                        "options": [
                            "One successful login after many failures",
                            "A user logging in once",
                            "A password being changed voluntarily"
                        ],
                        "correct_answer": (
                            "One successful login after many failures"
                        ),
                        "explanation": (
                            "Repeated failures followed by success can "
                            "indicate a compromised account, although "
                            "the pattern should be investigated rather "
                            "than treated as proof."
                        )
                    },

                    "practical_lab": {
                        "title": "Investigate Failed Login Events",
                        "objective": (
                            "Practise analysing authentication events "
                            "without targeting real accounts."
                        ),
                        "environment": "Fictional log-analysis exercise",
                        "tasks": [
                            "Identify repeated failures for the same account.",
                            "Determine whether a successful login followed them.",
                            "Recommend a temporary protective response.",
                            "Explain which additional logs would help confirm the incident."
                        ],
                        "expected_outcome": (
                            "The learner identifies a suspicious pattern "
                            "and recommends investigation, rate limiting, "
                            "and multifactor authentication."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What makes a brute force attack possible?",
                            "options": [
                                "Repeated password guessing",
                                "Installing software updates",
                                "Encrypting a backup"
                            ],
                            "answer": "Repeated password guessing",
                            "explanation": (
                                "The attack relies on trying possible "
                                "passwords until a match is found."
                            )
                        },
                        {
                            "question": "Which control helps limit repeated login attempts?",
                            "options": [
                                "Rate limiting",
                                "Disabling security logs",
                                "Reusing passwords"
                            ],
                            "answer": "Rate limiting",
                            "explanation": (
                                "Rate limiting restricts the frequency "
                                "of login attempts."
                            )
                        }
                    ],

                    "prevention": [
                        "Use long, unique passwords.",
                        "Enable multifactor authentication.",
                        "Apply rate limiting and suitable login throttling.",
                        "Monitor repeated failures and unusual successful logins.",
                        "Use secure password hashing for stored credentials."
                    ],

                    "conclusion": (
                        "Brute force attacks demonstrate why strong "
                        "passwords need to be combined with authentication "
                        "controls and monitoring."
                    )
                },

                "dictionary_attack": {
                    "id": "dictionary-attack",
                    "name": "Dictionary Attack",

                    "overview": (
                        "A dictionary attack tests likely passwords drawn "
                        "from word lists, common phrases, predictable "
                        "variations, and frequently used credentials."
                    ),

                    "how_it_works": [
                        "An attacker obtains or prepares a list of common passwords.",
                        "The list is used to test password guesses against a target.",
                        "Predictable passwords may be discovered more quickly than random ones.",
                        "The risk depends on the account protections and whether the attack targets a live login or stolen password hashes."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Predictable Workplace Password",
                            "scenario": (
                                "Several employees choose passwords based "
                                "on the company name and the current year."
                            ),
                            "lesson": (
                                "Avoid predictable patterns and never reuse "
                                "work passwords on other services."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "Common Passwords Across a Team",
                        "scenario": (
                            "A fictional organisation discovers that "
                            "multiple employees have chosen easily "
                            "guessable passwords."
                        ),
                        "problem": (
                            "The organisation has no password screening "
                            "or guidance against predictable choices."
                        ),
                        "response": [
                            "Block commonly used and compromised passwords.",
                            "Encourage password-manager use.",
                            "Require unique credentials for important accounts.",
                            "Enable multifactor authentication."
                        ],
                        "key_learning": (
                            "A password can satisfy a length rule and "
                            "still be predictable."
                        )
                    },

                    "simulation": {
                        "title": "Spot Predictable Password Choices",
                        "objective": "Recognise common password patterns.",
                        "steps": [
                            "Compare the fictional password descriptions.",
                            "Identify which choices are predictable.",
                            "Recommend a safer alternative."
                        ],
                        "examples": [
                            {
                                "description": "CompanyName2026!",
                                "risk": "Predictable organisation and year pattern"
                            },
                            {
                                "description": "A unique password generated by a password manager",
                                "risk": "Lower predictability when stored securely"
                            }
                        ],
                        "question": "Which choice is generally safer?",
                        "options": [
                            "A company name followed by the current year",
                            "A long, unique, randomly generated password",
                            "A common phrase used on every account"
                        ],
                        "correct_answer": (
                            "A long, unique, randomly generated password"
                        ),
                        "explanation": (
                            "Randomly generated, unique passwords are "
                            "harder to predict and reduce password reuse."
                        )
                    },

                    "practical_lab": {
                        "title": "Password Predictability Review",
                        "objective": (
                            "Evaluate fictional password patterns without "
                            "testing any real account."
                        ),
                        "environment": "Offline awareness exercise",
                        "tasks": [
                            "Classify sample password descriptions by predictability.",
                            "Identify reused or organisation-related patterns.",
                            "Suggest password-manager and multifactor-authentication improvements."
                        ],
                        "expected_outcome": (
                            "The learner can explain why common words "
                            "and predictable variations are risky."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What does a dictionary attack primarily use?",
                            "options": [
                                "Lists of likely passwords",
                                "Network cable diagrams",
                                "Software update records"
                            ],
                            "answer": "Lists of likely passwords",
                            "explanation": (
                                "Dictionary attacks test likely passwords "
                                "rather than every possible combination."
                            )
                        },
                        {
                            "question": "What reduces the risk of password guessing?",
                            "options": [
                                "Using predictable variations",
                                "Using unique random passwords",
                                "Sharing passwords with colleagues"
                            ],
                            "answer": "Using unique random passwords",
                            "explanation": (
                                "Unique random passwords are less predictable "
                                "than common words and familiar patterns."
                            )
                        }
                    ],

                    "prevention": [
                        "Use long, randomly generated passwords.",
                        "Avoid names, dates, company names, and common phrases.",
                        "Use a reputable password manager.",
                        "Block known compromised passwords where supported.",
                        "Enable multifactor authentication."
                    ],

                    "conclusion": (
                        "Dictionary attacks exploit predictability, so "
                        "password uniqueness and randomness are important "
                        "parts of account security."
                    )
                },

                "password_spraying": {
                    "id": "password-spraying",
                    "name": "Password Spraying",

                    "overview": (
                        "Password spraying attempts a small number of "
                        "common passwords against many accounts instead "
                        "of trying numerous passwords against one account. "
                        "This can evade simplistic account-specific alerts."
                    ),

                    "how_it_works": [
                        "The attacker identifies a set of accounts.",
                        "A small number of common password guesses are attempted across those accounts.",
                        "Attempts may be spread over time to avoid obvious patterns.",
                        "Successful access can expose organisational information."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Suspicious Sign-ins Across Employee Accounts",
                            "scenario": (
                                "A company's identity system records failed "
                                "sign-ins involving the same small set of "
                                "password guesses across many employees."
                            ),
                            "lesson": (
                                "Security monitoring should look across "
                                "multiple accounts, not just repeated "
                                "failures against one account."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "The Login Pattern Hidden Across Accounts",
                        "scenario": (
                            "A fictional business sees a few failed logins "
                            "for many accounts. No single account initially "
                            "exceeds its alert threshold."
                        ),
                        "problem": (
                            "Its monitoring rules examine each account "
                            "separately and miss the wider pattern."
                        ),
                        "response": [
                            "Correlate sign-in events across accounts.",
                            "Review unfamiliar locations and device signals.",
                            "Apply appropriate authentication rate limits.",
                            "Investigate affected accounts and revoke suspicious sessions when warranted."
                        ],
                        "key_learning": (
                            "Cross-account analysis can reveal attacks "
                            "that are difficult to spot in isolated logs."
                        )
                    },

                    "simulation": {
                        "title": "Identify a Cross-Account Pattern",
                        "objective": (
                            "Recognise a possible password-spraying pattern "
                            "in a fictional sign-in summary."
                        ),
                        "sample_events": [
                            {
                                "account": "staff01",
                                "result": "Failed sign-in"
                            },
                            {
                                "account": "staff02",
                                "result": "Failed sign-in"
                            },
                            {
                                "account": "staff03",
                                "result": "Failed sign-in"
                            },
                            {
                                "account": "staff04",
                                "result": "Failed sign-in"
                            }
                        ],
                        "question": (
                            "What should an analyst investigate first?"
                        ),
                        "options": [
                            "Whether similar sign-in failures share a pattern",
                            "Whether the office printer is switched on",
                            "Whether staff changed their desktop wallpaper"
                        ],
                        "correct_answer": (
                            "Whether similar sign-in failures share a pattern"
                        ),
                        "explanation": (
                            "Failures across several accounts can indicate "
                            "a coordinated authentication attack."
                        )
                    },

                    "practical_lab": {
                        "title": "Cross-Account Sign-In Analysis",
                        "objective": (
                            "Practise correlating fictional authentication "
                            "events across multiple users."
                        ),
                        "environment": "Offline log-analysis exercise",
                        "tasks": [
                            "Group failed sign-ins by time and account.",
                            "Look for common patterns across accounts.",
                            "Identify which accounts need further review.",
                            "Recommend proportionate protective controls."
                        ],
                        "expected_outcome": (
                            "The learner can distinguish a single-account "
                            "problem from a potentially coordinated attack."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What distinguishes password spraying?",
                            "options": [
                                "A few likely passwords tested across many accounts",
                                "Many random passwords tested against only one account",
                                "Changing passwords after a successful login"
                            ],
                            "answer": (
                                "A few likely passwords tested across many accounts"
                            ),
                            "explanation": (
                                "Password spraying spreads guesses across "
                                "accounts rather than concentrating many "
                                "guesses on one account."
                            )
                        },
                        {
                            "question": "Which monitoring approach is useful?",
                            "options": [
                                "Correlating events across accounts",
                                "Ignoring failed sign-ins",
                                "Disabling authentication alerts"
                            ],
                            "answer": "Correlating events across accounts",
                            "explanation": (
                                "Cross-account correlation can reveal "
                                "patterns that individual-account rules miss."
                            )
                        }
                    ],

                    "prevention": [
                        "Enable multifactor authentication.",
                        "Monitor authentication events across accounts.",
                        "Use risk-based sign-in detection and rate limiting.",
                        "Block commonly used and compromised passwords.",
                        "Investigate unusual sign-in locations, devices, and patterns."
                    ],

                    "conclusion": (
                        "Password spraying is best detected by combining "
                        "strong authentication controls with monitoring "
                        "that identifies patterns across multiple accounts."
                    )
                },

                "credential_stuffing": {
                    "id": "credential-stuffing",
                    "name": "Credential Stuffing",

                    "overview": (
                        "Credential stuffing uses username-and-password "
                        "pairs exposed in earlier data breaches to attempt "
                        "access to other services. It succeeds when people "
                        "reuse credentials."
                    ),

                    "how_it_works": [
                        "Credentials are exposed in a breach or obtained from a compromised source.",
                        "The same username-and-password pairs are tried on another service.",
                        "Accounts using reused passwords may be accessed.",
                        "The victim may experience unauthorised purchases, data exposure, or account takeover."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Old Password Used on a New Website",
                            "scenario": (
                                "A user reuses the password from an older "
                                "shopping account on their primary email "
                                "account. After the shopping service suffers "
                                "a breach, both accounts become vulnerable."
                            ),
                            "lesson": (
                                "A different password for every service "
                                "prevents one breach from automatically "
                                "putting other accounts at risk."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "One Breach, Several Vulnerable Accounts",
                        "scenario": (
                            "A fictional service notices login attempts "
                            "against customer accounts using credentials "
                            "previously exposed elsewhere."
                        ),
                        "problem": (
                            "Some customers reused passwords across "
                            "unrelated services."
                        ),
                        "response": [
                            "Detect unusual login patterns and automation.",
                            "Notify affected users when appropriate.",
                            "Require password resets for confirmed compromised accounts.",
                            "Offer multifactor authentication and suspicious-session review."
                        ],
                        "key_learning": (
                            "Credential reuse allows a breach at one "
                            "service to affect accounts elsewhere."
                        )
                    },

                    "simulation": {
                        "title": "Respond to a Credential-Reuse Alert",
                        "objective": (
                            "Choose appropriate responses to a fictional "
                            "credential-stuffing alert."
                        ),
                        "scenario": (
                            "An account receives several sign-in attempts "
                            "from unfamiliar devices, and the security "
                            "service flags a possible credential match "
                            "from a known breach."
                        ),
                        "question": "What is the best first response?",
                        "options": [
                            "Review the alert and secure the account",
                            "Reuse the same password on another service",
                            "Disable all account security notifications"
                        ],
                        "correct_answer": "Review the alert and secure the account",
                        "explanation": (
                            "The user or security team should verify the "
                            "activity and take appropriate account-protection "
                            "steps, including changing an exposed password."
                        )
                    },

                    "practical_lab": {
                        "title": "Credential-Reuse Incident Response",
                        "objective": (
                            "Develop a safe response plan for suspected "
                            "credential stuffing."
                        ),
                        "environment": "Fictional incident-response scenario",
                        "tasks": [
                            "Review the sign-in alert and its context.",
                            "Identify accounts potentially affected by reused credentials.",
                            "Recommend unique passwords and multifactor authentication.",
                            "Describe how suspicious sessions should be reviewed."
                        ],
                        "expected_outcome": (
                            "The learner understands the relationship "
                            "between data breaches, password reuse, "
                            "and account takeover."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What does credential stuffing rely on?",
                            "options": [
                                "Reused credentials from previous exposures",
                                "Physical theft of a keyboard",
                                "Updating antivirus definitions"
                            ],
                            "answer": "Reused credentials from previous exposures",
                            "explanation": (
                                "The attack tries previously exposed "
                                "credential pairs on other services."
                            )
                        },
                        {
                            "question": "What is the strongest basic defence against credential reuse?",
                            "options": [
                                "One password for every account",
                                "Unique passwords for each service",
                                "Sharing passwords with friends"
                            ],
                            "answer": "Unique passwords for each service",
                            "explanation": (
                                "Unique passwords prevent one exposed "
                                "password from unlocking unrelated accounts."
                            )
                        }
                    ],

                    "prevention": [
                        "Use a unique password for every service.",
                        "Store passwords in a reputable password manager.",
                        "Enable multifactor authentication.",
                        "Monitor suspicious sign-ins and account changes.",
                        "Change exposed credentials and review active sessions."
                    ],

                    "conclusion": (
                        "Credential stuffing shows why password reuse "
                        "is dangerous even when an individual password "
                        "was originally strong."
                    )
                }
            }
        },

        "credential_theft": {
            "id": "credential-theft",
            "name": "Credential Theft and Authentication Abuse",
            "description": (
                "Attacks that steal authentication information or misuse "
                "credentials and sessions to gain unauthorised access."
            ),

            "types": {
                "phishing_for_credentials": {
                    "id": "phishing-for-credentials",
                    "name": "Credential Phishing",

                    "overview": (
                        "Credential phishing tricks people into entering "
                        "their usernames, passwords, or authentication "
                        "codes on deceptive pages or into fraudulent "
                        "communication channels."
                    ),

                    "how_it_works": [
                        "A victim receives a deceptive email, message, or link.",
                        "The message imitates a trusted service or creates urgency.",
                        "The victim is directed to a fraudulent sign-in page or asked to disclose information.",
                        "The attacker may use the stolen details to attempt account access."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Fake Account-Expiry Warning",
                            "scenario": (
                                "An employee receives a message claiming "
                                "that their work account will expire unless "
                                "they sign in immediately through a supplied link."
                            ),
                            "lesson": (
                                "Verify account warnings through the "
                                "organisation's known official website "
                                "or support channel."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "The Sign-In Page That Looked Familiar",
                        "scenario": (
                            "A fictional employee enters work credentials "
                            "into a page reached through an unexpected email."
                        ),
                        "problem": (
                            "The page imitates the organisation's normal "
                            "login screen, but its domain is unfamiliar."
                        ),
                        "response": [
                            "Report the message to the security team.",
                            "Change the exposed password through the official service.",
                            "Revoke suspicious sessions and review sign-in history.",
                            "Investigate possible exposure of multifactor authentication information."
                        ],
                        "key_learning": (
                            "A familiar-looking page is not proof that "
                            "a sign-in request is legitimate."
                        )
                    },

                    "simulation": {
                        "title": "Inspect a Suspicious Sign-In Message",
                        "objective": (
                            "Identify common warning signs of credential phishing."
                        ),
                        "sample_message": (
                            "Your account will be suspended today. "
                            "Use the link in this message to verify "
                            "your password immediately."
                        ),
                        "warning_signs": [
                            "Unexpected urgency",
                            "A request to enter credentials through a message link",
                            "A destination domain that has not been verified"
                        ],
                        "question": "What should the recipient do?",
                        "options": [
                            "Open the link and enter the password",
                            "Visit the known official website independently",
                            "Forward the password to the sender"
                        ],
                        "correct_answer": (
                            "Visit the known official website independently"
                        ),
                        "explanation": (
                            "Independent verification avoids trusting "
                            "a potentially deceptive link."
                        )
                    },

                    "practical_lab": {
                        "title": "Credential Phishing Awareness",
                        "objective": (
                            "Evaluate fictional messages for signs of "
                            "credential theft."
                        ),
                        "environment": "Offline awareness exercise",
                        "tasks": [
                            "Identify urgency and suspicious requests.",
                            "Check whether the destination domain is verified.",
                            "Choose a safe reporting method.",
                            "Describe the response if credentials were already entered."
                        ],
                        "expected_outcome": (
                            "The learner can recognise credential-phishing "
                            "indicators and follow a safe reporting process."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What is a common objective of credential phishing?",
                            "options": [
                                "Tricking users into disclosing login information",
                                "Improving password storage",
                                "Installing legitimate security updates"
                            ],
                            "answer": (
                                "Tricking users into disclosing login information"
                            ),
                            "explanation": (
                                "Credential phishing attempts to deceive "
                                "users into revealing authentication information."
                            )
                        },
                        {
                            "question": "How should an unexpected account warning be verified?",
                            "options": [
                                "Through a known official website or channel",
                                "By replying with the password",
                                "By trusting any supplied link"
                            ],
                            "answer": (
                                "Through a known official website or channel"
                            ),
                            "explanation": (
                                "Independent verification helps avoid "
                                "fraudulent sign-in pages."
                            )
                        }
                    ],

                    "prevention": [
                        "Verify unexpected requests through official channels.",
                        "Inspect domains carefully before signing in.",
                        "Use phishing-resistant multifactor authentication where available.",
                        "Report suspicious messages promptly.",
                        "Secure exposed credentials and investigate suspicious sessions."
                    ],

                    "conclusion": (
                        "Credential phishing targets trust as much as "
                        "technology, so careful verification and strong "
                        "authentication are essential."
                    )
                },

                "keylogging": {
                    "id": "keylogging",
                    "name": "Keylogging",

                    "overview": (
                        "Keylogging is the recording of keyboard input. "
                        "Malicious keyloggers may capture passwords, "
                        "messages, and other sensitive information."
                    ),

                    "how_it_works": [
                        "A keylogger is introduced through malicious software, a compromised device, or another unauthorised method.",
                        "It records keyboard input or related activity.",
                        "Captured information may be stored or transmitted.",
                        "An attacker may attempt to use the exposed information to access accounts."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Credentials Exposed on an Infected Device",
                            "scenario": (
                                "A user installs software from an untrusted "
                                "source. Later, unfamiliar account activity "
                                "appears after they enter their password."
                            ),
                            "lesson": (
                                "Use trusted software sources, keep devices "
                                "updated, and investigate signs of malware."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "Suspicious Account Activity After a Download",
                        "scenario": (
                            "A fictional employee installs an unauthorised "
                            "application and later discovers suspicious "
                            "sign-ins to their work account."
                        ),
                        "problem": (
                            "The device may have been compromised, and "
                            "credentials entered on it may be exposed."
                        ),
                        "response": [
                            "Follow the organisation's incident-response process.",
                            "Isolate the affected device when appropriate.",
                            "Investigate it with approved security tools.",
                            "Change exposed credentials from a trusted device.",
                            "Review account activity and revoke suspicious sessions."
                        ],
                        "key_learning": (
                            "Account protection sometimes requires "
                            "investigating the device used to sign in."
                        )
                    },

                    "simulation": {
                        "title": "Respond to Possible Keylogger Infection",
                        "objective": (
                            "Select safe actions when a device may be "
                            "capturing sensitive input."
                        ),
                        "question": (
                            "What is the safest initial response on a "
                            "managed work device?"
                        ),
                        "options": [
                            "Follow incident-response guidance and report the device",
                            "Continue entering sensitive credentials",
                            "Download more unverified software"
                        ],
                        "correct_answer": (
                            "Follow incident-response guidance and report the device"
                        ),
                        "explanation": (
                            "The device should be assessed through an "
                            "approved response process before it is "
                            "trusted for sensitive activity."
                        )
                    },

                    "practical_lab": {
                        "title": "Endpoint Security Investigation",
                        "objective": (
                            "Practise identifying possible endpoint "
                            "compromise using fictional alerts."
                        ),
                        "environment": "Defensive endpoint investigation",
                        "tasks": [
                            "Review fictional endpoint alerts.",
                            "Identify suspicious software installation events.",
                            "Recommend isolation and approved investigation steps.",
                            "Explain why credentials should be changed from a trusted device."
                        ],
                        "expected_outcome": (
                            "The learner can describe a safe response "
                            "to possible credential capture."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What can a malicious keylogger capture?",
                            "options": [
                                "Keyboard input such as passwords",
                                "Only monitor brightness",
                                "Only the device's battery level"
                            ],
                            "answer": "Keyboard input such as passwords",
                            "explanation": (
                                "Malicious keyloggers can record sensitive "
                                "information entered through the keyboard."
                            )
                        },
                        {
                            "question": "What should happen if a device may be compromised?",
                            "options": [
                                "Follow the approved incident-response process",
                                "Ignore all alerts",
                                "Enter more passwords to test it"
                            ],
                            "answer": (
                                "Follow the approved incident-response process"
                            ),
                            "explanation": (
                                "A potentially compromised device should "
                                "be investigated safely before it is trusted."
                            )
                        }
                    ],

                    "prevention": [
                        "Install software only from trusted sources.",
                        "Keep operating systems and applications updated.",
                        "Use reputable endpoint protection.",
                        "Avoid running unknown attachments or executables.",
                        "Investigate suspicious activity and change exposed credentials safely."
                    ],

                    "conclusion": (
                        "Keylogging demonstrates that even a strong password "
                        "can be exposed if the device used to enter it "
                        "is compromised."
                    )
                },

                "session_hijacking": {
                    "id": "session-hijacking",
                    "name": "Session Hijacking",

                    "overview": (
                        "Session hijacking occurs when an attacker obtains "
                        "or misuses a valid authenticated session, potentially "
                        "gaining access without needing to know the password."
                    ),

                    "how_it_works": [
                        "A user signs in and receives a session token or cookie.",
                        "The token is exposed through a security weakness, compromised device, or other unauthorised access.",
                        "An attacker attempts to reuse the session.",
                        "If protections are inadequate, the attacker may act as the authenticated user."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Account Remains Open on a Shared Computer",
                            "scenario": (
                                "A user accesses a sensitive service on a "
                                "shared device and leaves the session active."
                            ),
                            "lesson": (
                                "Sign out of shared devices and avoid "
                                "using untrusted computers for sensitive accounts."
                            )
                        }
                    ],

                    "case_study": {
                        "title": "The Session That Was Never Revoked",
                        "scenario": (
                            "A fictional employee reports suspicious "
                            "activity after signing in on an unfamiliar device."
                        ),
                        "problem": (
                            "The service has weak session controls and "
                            "does not adequately revoke suspicious sessions."
                        ),
                        "response": [
                            "Revoke active sessions where compromise is suspected.",
                            "Review authentication and session logs.",
                            "Improve cookie security and session expiration.",
                            "Require reauthentication for sensitive actions."
                        ],
                        "key_learning": (
                            "Protecting an account requires protecting "
                            "authenticated sessions as well as passwords."
                        )
                    },

                    "simulation": {
                        "title": "Choose a Session-Security Response",
                        "objective": (
                            "Recognise suspicious session activity and "
                            "select a suitable response."
                        ),
                        "scenario": (
                            "A user notices a sensitive action they did "
                            "not perform and an unfamiliar active session."
                        ),
                        "question": "What should be prioritised?",
                        "options": [
                            "Revoke suspicious sessions and investigate",
                            "Ignore the activity because the password is strong",
                            "Share the active session with a colleague"
                        ],
                        "correct_answer": (
                            "Revoke suspicious sessions and investigate"
                        ),
                        "explanation": (
                            "A stolen session can be misused even if the "
                            "attacker does not know the account password."
                        )
                    },

                    "practical_lab": {
                        "title": "Session Incident Review",
                        "objective": (
                            "Analyse a fictional session-security incident."
                        ),
                        "environment": "Offline incident-response exercise",
                        "tasks": [
                            "Review the reported unfamiliar activity.",
                            "Identify sessions requiring investigation.",
                            "Recommend revocation and reauthentication.",
                            "Describe improvements to session management."
                        ],
                        "expected_outcome": (
                            "The learner understands why session tokens "
                            "must be protected and revocable."
                        )
                    },

                    "assessment": [
                        {
                            "question": "What does session hijacking target?",
                            "options": [
                                "An authenticated session",
                                "Only the computer's wallpaper",
                                "A printer's paper tray"
                            ],
                            "answer": "An authenticated session",
                            "explanation": (
                                "Session hijacking involves obtaining or "
                                "misusing a valid authenticated session."
                            )
                        },
                        {
                            "question": "Which response can limit misuse of a compromised session?",
                            "options": [
                                "Revoke the suspicious session",
                                "Ignore session activity",
                                "Disable security logging"
                            ],
                            "answer": "Revoke the suspicious session",
                            "explanation": (
                                "Revocation can invalidate a session that "
                                "may have been exposed."
                            )
                        }
                    ],

                    "prevention": [
                        "Use HTTPS throughout authenticated sessions.",
                        "Set secure, HttpOnly, and appropriate SameSite cookie attributes.",
                        "Regenerate session identifiers after authentication and privilege changes.",
                        "Expire inactive sessions and revoke suspicious ones.",
                        "Require reauthentication for sensitive operations."
                    ],

                    "conclusion": (
                        "Session security is a separate part of account "
                        "security. Password protection alone cannot prevent "
                        "the misuse of a stolen session."
                    )
                }
            }
        }
    }
}