
PHISHING_VARIANTS = {
    "id": "phishing",
    "name": "Phishing Variants",
    "description": (
        "Explore different phishing techniques, how attackers deceive "
        "victims, and how suspicious messages and websites can be identified."
    ),
    "types": {
        "email_phishing": {
            "id": "email-phishing",
            "name": "Email Phishing",
            "description": "Fraudulent emails designed to steal information or deliver malicious content.",
            "types": {
                "deceptive_email": {
                    "id": "deceptive-email",
                    "name": "Deceptive Email Attacks",
                    "summary": "Attackers send emails that appear to come from legitimate organisations, colleagues, or service providers.",
                    "learning_objectives": [
                        "Recognise suspicious email characteristics.",
                        "Understand how email deception works.",
                        "Identify safe ways to verify unexpected requests."
                    ],
                    "overview": (
                        "Email phishing is a social engineering technique in which "
                        "an attacker disguises a message as legitimate to persuade "
                        "the recipient to reveal information, open an attachment, "
                        "visit a fraudulent website, or perform an unsafe action."
                    ),
                    "how_it_works": [
                        "The attacker chooses a target and imitates a trusted sender.",
                        "The email introduces urgency, fear, curiosity, or an attractive offer.",
                        "The recipient is encouraged to click a link, open a file, or share information.",
                        "The attacker may collect credentials, deliver malware, or misuse the information."
                    ],
                    "warning_signs": [
                        "An unexpected request for passwords or financial information.",
                        "A sender address that differs from the organisation's genuine domain.",
                        "Urgent threats about account closure or immediate payment.",
                        "Unexpected attachments or links with unfamiliar destinations.",
                        "Greetings, wording, or branding that do not match the supposed sender."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Fake account security warning",
                            "scenario": (
                                "A student receives an email claiming that their "
                                "college account will be suspended unless they "
                                "verify their login details."
                            ),
                            "lesson": (
                                "The student should open the college website using "
                                "a known address or contact the IT department "
                                "instead of following the email link."
                            )
                        },
                        {
                            "title": "Unexpected invoice",
                            "scenario": (
                                "An employee receives an invoice attachment from "
                                "an unfamiliar supplier shortly before a payment deadline."
                            ),
                            "lesson": (
                                "The employee should verify the sender and invoice "
                                "through an established business contact before "
                                "opening unexpected attachments or approving payment."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The suspicious university email",
                        "background": (
                            "A university student receives a message using the "
                            "university logo. It claims that a mailbox upgrade "
                            "requires immediate password verification."
                        ),
                        "events": [
                            "The sender address contains an unfamiliar domain.",
                            "The message threatens to disable the mailbox within one hour.",
                            "The link leads to a website whose address differs from the university's official website."
                        ],
                        "analysis": (
                            "The unfamiliar domain, threatening deadline, and "
                            "unexpected password request are warning signs. "
                            "A logo alone does not establish that a message is genuine."
                        ),
                        "response": [
                            "Do not enter credentials on the linked page.",
                            "Verify the notice through the university's official portal.",
                            "Report the email to the appropriate IT or security team.",
                            "If credentials were already entered, change the password through the official website and report the incident."
                        ],
                        "lesson": "Verify the sender and destination independently before trusting an email."
                    },
                    "simulation": {
                        "title": "Spot the suspicious email",
                        "instructions": (
                            "Read the fictional email below and decide whether "
                            "it should be trusted."
                        ),
                        "scenario": (
                            "From: Campus Account Support <support@campus-security.example>\n"
                            "Subject: Immediate action required\n\n"
                            "Your mailbox will be disabled today. Use the link "
                            "provided in this message to confirm your password."
                        ),
                        "question": "What is the safest response?",
                        "options": [
                            "Click the link because the email uses university terminology.",
                            "Reply with the password to prevent account suspension.",
                            "Verify the notice through the official university portal and report the email.",
                            "Forward the email to classmates so they can check their accounts."
                        ],
                        "correct_answer": 2,
                        "explanation": (
                            "The safest response is to verify the notice through "
                            "an independently accessed official portal and report "
                            "the suspicious message. The example domain is fictional."
                        )
                    },
                    "practical_lab": {
                        "title": "Email Phishing Inspection Lab",
                        "objective": (
                            "Practise examining a fictional email without opening "
                            "links or attachments."
                        ),
                        "environment": "Offline, text-based exercise",
                        "steps": [
                            "Read the fictional email supplied in the simulation.",
                            "Identify the sender, subject, requested action, and deadline.",
                            "List at least three suspicious indicators.",
                            "Describe how you would verify the request safely.",
                            "Write a short incident report explaining your decision."
                        ],
                        "expected_result": (
                            "The learner identifies the suspicious request, "
                            "avoids interacting with the link, and chooses an "
                            "independent verification method."
                        ),
                        "safety_note": (
                            "Use only the fictional content provided here. "
                            "Do not send real phishing emails or collect real credentials."
                        )
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "Which is a common sign of email phishing?",
                                "options": [
                                    "An unexpected request for credentials",
                                    "A message expected from a verified contact",
                                    "A bookmark saved in your browser",
                                    "A routine calendar reminder"
                                ],
                                "answer": 0,
                                "explanation": "Unexpected credential requests should be independently verified."
                            },
                            {
                                "question": "What should you do with an unexpected attachment?",
                                "options": [
                                    "Open it immediately",
                                    "Forward it to everyone",
                                    "Verify the sender and purpose first",
                                    "Disable antivirus software"
                                ],
                                "answer": 2,
                                "explanation": "Unexpected attachments should be checked before opening."
                            },
                            {
                                "question": "Does a familiar logo prove that an email is genuine?",
                                "options": [
                                    "Yes, always",
                                    "No, logos can be copied",
                                    "Only if the email is urgent",
                                    "Only when the subject is short"
                                ],
                                "answer": 1,
                                "explanation": "Visual branding can be copied; check the sender and destination independently."
                            }
                        ]
                    },
                    "prevention": [
                        "Check the complete sender address and the destination of links.",
                        "Access important accounts through known bookmarks or official apps.",
                        "Never share passwords or verification codes in response to unexpected messages.",
                        "Use multifactor authentication where available.",
                        "Report suspicious messages using the organisation's approved process."
                    ],
                    "conclusion": (
                        "Email phishing relies on trust and hurried decisions. "
                        "Checking the sender, verifying requests independently, "
                        "and reporting suspicious messages can prevent account "
                        "compromise and malware infections."
                    )
                }
            }
        },
        "spear_phishing": {
            "id": "spear-phishing",
            "name": "Spear Phishing",
            "description": "Targeted phishing messages tailored to a particular person or organisation.",
            "types": {
                "targeted_deception": {
                    "id": "targeted-deception",
                    "name": "Targeted Phishing",
                    "summary": "A targeted phishing message uses details about a person, their role, or their organisation to appear credible.",
                    "learning_objectives": [
                        "Distinguish targeted phishing from generic phishing.",
                        "Understand how publicly available information can increase credibility.",
                        "Practise verifying unusual requests through trusted channels."
                    ],
                    "overview": (
                        "Spear phishing focuses on a specific target rather than "
                        "sending the same generic message to many recipients. "
                        "Attackers may refer to a real project, colleague, course, "
                        "or recent event to make a message seem familiar."
                    ),
                    "how_it_works": [
                        "The attacker gathers information about the target or organisation.",
                        "A message is tailored to the target's role or current activity.",
                        "The message requests information, payment, access, or another action.",
                        "If the target trusts the message, sensitive information or access may be exposed."
                    ],
                    "warning_signs": [
                        "A familiar name paired with an unusual request.",
                        "A request to bypass normal approval procedures.",
                        "Unexpected requests for confidential files or authentication codes.",
                        "Pressure to keep a conversation secret.",
                        "A sender using a personal address instead of the expected organisational account."
                    ],
                    "real_world_examples": [
                        {
                            "title": "A fake project request",
                            "scenario": (
                                "An employee receives a message mentioning a real "
                                "work project and asking them to share a confidential file."
                            ),
                            "lesson": (
                                "Confirm the request with the colleague through "
                                "a separate, established communication channel."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The familiar project request",
                        "background": (
                            "A team member receives an unexpected message that "
                            "mentions a current project and asks for a restricted document."
                        ),
                        "events": [
                            "The message contains accurate project details.",
                            "The sender asks the recipient to bypass the usual approval process.",
                            "The requested file contains confidential information."
                        ],
                        "analysis": (
                            "Accurate details can make a fraudulent request seem "
                            "genuine. The request to bypass established controls "
                            "is a particularly important warning sign."
                        ),
                        "response": [
                            "Do not share the document immediately.",
                            "Contact the supposed colleague using a known channel.",
                            "Follow the normal access-approval process.",
                            "Report the message if impersonation is suspected."
                        ],
                        "lesson": "Familiar details are not a substitute for identity verification."
                    },
                    "simulation": {
                        "title": "Verify the project request",
                        "instructions": "Choose the safest response to the fictional situation.",
                        "scenario": (
                            "A message appears to come from your project supervisor. "
                            "It requests a confidential file immediately and says "
                            "not to involve the usual approver."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Send the file because the sender knows the project.",
                            "Verify the request with the supervisor through a known channel and follow approval rules.",
                            "Upload the file to a public sharing website.",
                            "Send your password to confirm your identity."
                        ],
                        "correct_answer": 1,
                        "explanation": (
                            "Verify unusual requests independently and never bypass "
                            "confidentiality or approval requirements."
                        )
                    },
                    "practical_lab": {
                        "title": "Targeted Phishing Analysis",
                        "objective": "Identify manipulation in a fictional targeted message.",
                        "environment": "Offline case analysis",
                        "steps": [
                            "Read the fictional project request.",
                            "Identify the personal details used to build trust.",
                            "Identify the requested action and any unusual secrecy or urgency.",
                            "Choose an independent verification method.",
                            "Write a short recommendation for the organisation."
                        ],
                        "expected_result": (
                            "The learner recognises that a personalised message "
                            "can still be fraudulent and selects a safe verification process."
                        ),
                        "safety_note": "Use fictional examples only; do not target real people."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "What distinguishes spear phishing from generic phishing?",
                                "options": [
                                    "It is always sent by text message",
                                    "It is tailored to a specific target",
                                    "It cannot contain links",
                                    "It only targets public websites"
                                ],
                                "answer": 1,
                                "explanation": "Spear phishing is personalised to a particular target."
                            },
                            {
                                "question": "A message contains accurate project details. Does that prove it is legitimate?",
                                "options": [
                                    "Yes",
                                    "No, details may have been obtained elsewhere",
                                    "Only if it is urgent",
                                    "Only if it contains an attachment"
                                ],
                                "answer": 1,
                                "explanation": "Personal or organisational information can be gathered from many sources."
                            }
                        ]
                    },
                    "prevention": [
                        "Verify unusual requests using a known communication channel.",
                        "Follow access controls and approval procedures.",
                        "Limit unnecessary public sharing of sensitive organisational details.",
                        "Use multifactor authentication and report suspected impersonation."
                    ],
                    "conclusion": (
                        "Spear phishing becomes convincing by using context and "
                        "personalisation. Independent verification remains essential, "
                        "even when a message appears to know the recipient."
                    )
                }
            }
        },
        "whaling": {
            "id": "whaling",
            "name": "Whaling",
            "description": "Targeted phishing directed at senior executives or other high-value decision-makers.",
            "types": {
                "executive_impersonation": {
                    "id": "executive-impersonation",
                    "name": "Executive Impersonation",
                    "summary": "Whaling attempts to exploit the authority, responsibilities, or sensitive access associated with senior roles.",
                    "learning_objectives": [
                        "Recognise executive-targeted phishing.",
                        "Understand why authority and urgency can influence decisions.",
                        "Apply verification and approval procedures to sensitive requests."
                    ],
                    "overview": (
                        "Whaling is a specialised form of targeted phishing aimed "
                        "at senior leaders or other individuals with significant "
                        "financial, operational, or information access."
                    ),
                    "how_it_works": [
                        "The attacker selects a senior or high-access target.",
                        "The message imitates a trusted business contact or executive.",
                        "It requests a sensitive action, such as approving a payment or disclosing information.",
                        "The attacker hopes the recipient will act quickly because of the sender's apparent authority."
                    ],
                    "warning_signs": [
                        "An unusual request for a large or urgent payment.",
                        "A demand to bypass dual approval.",
                        "A request for confidential employee or business records.",
                        "Instructions to keep a transaction secret.",
                        "Unexpected changes to payment details."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Urgent executive payment",
                            "scenario": (
                                "A finance employee receives a message appearing "
                                "to come from a senior executive and requesting "
                                "an immediate transfer to a new account."
                            ),
                            "lesson": (
                                "The employee should verify the request using "
                                "approved procedures and independently confirmed contact details."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The urgent transfer",
                        "background": (
                            "A fictional organisation receives a payment request "
                            "that appears to come from a senior executive."
                        ),
                        "events": [
                            "The request is marked confidential and urgent.",
                            "The destination bank details are new.",
                            "The message discourages the normal second approval."
                        ],
                        "analysis": (
                            "The combination of urgency, changed payment details, "
                            "and pressure to bypass controls is suspicious regardless "
                            "of the apparent sender's seniority."
                        ),
                        "response": [
                            "Pause the transaction.",
                            "Verify the request using the organisation's approved process.",
                            "Confirm new payment details independently.",
                            "Notify the appropriate finance or security team."
                        ],
                        "lesson": "Authority must never replace financial verification controls."
                    },
                    "simulation": {
                        "title": "The executive email",
                        "instructions": "Select the safest action in this fictional situation.",
                        "scenario": (
                            "An email apparently from the managing director asks "
                            "you to transfer funds to a new account before the end "
                            "of the day and skip the normal second approval."
                        ),
                        "question": "What is the safest response?",
                        "options": [
                            "Transfer the funds immediately",
                            "Ignore all company payment policies",
                            "Verify the request independently and follow the normal approval process",
                            "Send the executive your account password"
                        ],
                        "correct_answer": 2,
                        "explanation": "Sensitive financial actions require independent verification and established approvals."
                    },
                    "practical_lab": {
                        "title": "Executive Request Verification",
                        "objective": "Evaluate a fictional high-risk business request.",
                        "environment": "Offline decision-making exercise",
                        "steps": [
                            "Read the fictional payment request.",
                            "Identify the urgency, authority, and secrecy cues.",
                            "Check whether the request changes established payment details.",
                            "Write the verification steps required before action.",
                            "Explain when the request should be reported."
                        ],
                        "expected_result": (
                            "The learner identifies red flags and refuses to bypass "
                            "independent verification or approval controls."
                        ),
                        "safety_note": "Do not initiate real payments or contact real targets for this exercise."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "Who is commonly targeted by whaling?",
                                "options": [
                                    "Only schoolchildren",
                                    "Senior executives and high-value decision-makers",
                                    "Only website visitors",
                                    "Only anonymous forum users"
                                ],
                                "answer": 1,
                                "explanation": "Whaling focuses on senior or otherwise high-value targets."
                            },
                            {
                                "question": "What should happen when an urgent payment request changes bank details?",
                                "options": [
                                    "Pay without checking",
                                    "Verify the change independently and follow approval rules",
                                    "Share account credentials",
                                    "Disable financial alerts"
                                ],
                                "answer": 1,
                                "explanation": "Independent verification helps prevent fraudulent payment changes."
                            }
                        ]
                    },
                    "prevention": [
                        "Require independent verification for sensitive financial requests.",
                        "Maintain dual approval for high-value transactions.",
                        "Confirm changed bank details using previously verified contact information.",
                        "Train staff to challenge suspicious requests regardless of apparent seniority.",
                        "Report suspected impersonation promptly."
                    ],
                    "conclusion": (
                        "Whaling exploits authority and access. Clear financial "
                        "controls, independent verification, and a culture where "
                        "employees can question unusual requests reduce the risk."
                    )
                }
            }
        },
        "smishing": {
            "id": "smishing",
            "name": "Smishing",
            "description": "Phishing delivered through SMS or other text messaging services.",
            "types": {
                "fraudulent_text": {
                    "id": "fraudulent-text",
                    "name": "Fraudulent Text Messages",
                    "summary": "Smishing messages use text notifications and short links to persuade recipients to disclose information or make payments.",
                    "learning_objectives": [
                        "Identify suspicious text messages.",
                        "Understand the risks of shortened links and unexpected payment demands.",
                        "Practise verifying delivery, banking, and account alerts safely."
                    ],
                    "overview": (
                        "Smishing combines SMS or messaging services with phishing "
                        "techniques. Messages may impersonate banks, delivery "
                        "companies, government services, or online platforms."
                    ),
                    "how_it_works": [
                        "A message claims there is a delivery, account, payment, or security issue.",
                        "It pressures the recipient to follow a link or reply.",
                        "The link may lead to a fraudulent form or the reply may reveal useful information.",
                        "The attacker may misuse submitted details or attempt further fraud."
                    ],
                    "warning_signs": [
                        "Unexpected delivery fees or parcel problems.",
                        "Shortened or unfamiliar links.",
                        "Requests for passwords, card details, or one-time codes.",
                        "Threats of penalties or account suspension.",
                        "Messages that ask the recipient to install an unfamiliar application."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Fake parcel fee",
                            "scenario": (
                                "A person receives a text claiming a parcel is "
                                "being held until a small fee is paid through a link."
                            ),
                            "lesson": (
                                "Check the delivery directly through the courier's "
                                "official application or website."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The missing delivery",
                        "background": (
                            "A fictional text message claims that a parcel cannot "
                            "be delivered without a small additional payment."
                        ),
                        "events": [
                            "The recipient is not expecting a fee.",
                            "The message uses an unfamiliar website address.",
                            "The payment page requests card details."
                        ],
                        "analysis": (
                            "Unexpected fees, unfamiliar destinations, and requests "
                            "for payment information are warning signs. The message "
                            "should not be trusted solely because it mentions a delivery."
                        ),
                        "response": [
                            "Do not open the supplied link or enter payment details.",
                            "Check delivery status through the courier's official service.",
                            "Report the suspicious text through available reporting channels.",
                            "Contact the bank promptly if financial information was disclosed."
                        ],
                        "lesson": "Verify delivery and payment claims through independently accessed services."
                    },
                    "simulation": {
                        "title": "Check the delivery alert",
                        "instructions": "Choose the safest response.",
                        "scenario": (
                            "A fictional text says that your parcel is delayed and "
                            "requires immediate payment through an unfamiliar link."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Enter your card details",
                            "Reply with your banking PIN",
                            "Check the parcel through the courier's official service",
                            "Forward the link to other people"
                        ],
                        "correct_answer": 2,
                        "explanation": "Use the courier's official service rather than a link in an unexpected message."
                    },
                    "practical_lab": {
                        "title": "Smishing Message Review",
                        "objective": "Identify suspicious features in a fictional SMS.",
                        "environment": "Offline text analysis",
                        "steps": [
                            "Read the fictional delivery message.",
                            "Identify the claim and the action being requested.",
                            "Inspect the displayed domain as text without opening it.",
                            "Write down two safe ways to verify the claim.",
                            "Describe how to report the message."
                        ],
                        "expected_result": (
                            "The learner identifies the suspicious request and "
                            "chooses a trusted verification method."
                        ),
                        "safety_note": "The message is fictional. Do not visit suspicious links or enter real payment information."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "What does smishing use to deliver phishing attempts?",
                                "options": [
                                    "Text messages",
                                    "Only printed letters",
                                    "Only offline documents",
                                    "Only computer games"
                                ],
                                "answer": 0,
                                "explanation": "Smishing commonly uses SMS or messaging services."
                            },
                            {
                                "question": "How should an unexpected delivery fee be verified?",
                                "options": [
                                    "Use the message link",
                                    "Send payment immediately",
                                    "Check through the courier's official service",
                                    "Provide a one-time code by text"
                                ],
                                "answer": 2,
                                "explanation": "Independent verification avoids relying on potentially fraudulent links."
                            }
                        ]
                    },
                    "prevention": [
                        "Avoid links in unexpected messages about money or account problems.",
                        "Verify claims through official applications or known website addresses.",
                        "Never disclose passwords, banking PINs, or one-time codes by text.",
                        "Report suspicious messages and block the sender when appropriate.",
                        "Contact your financial institution immediately if payment details may be compromised."
                    ],
                    "conclusion": (
                        "Smishing exploits the speed and familiarity of text messages. "
                        "Taking a moment to verify unexpected claims can prevent "
                        "financial loss and account compromise."
                    )
                }
            }
        },
        "vishing": {
            "id": "vishing",
            "name": "Vishing",
            "description": "Voice-based phishing carried out through phone calls or voice messages.",
            "types": {
                "fraudulent_call": {
                    "id": "fraudulent-call",
                    "name": "Fraudulent Support Calls",
                    "summary": "Vishing callers impersonate trusted people or organisations to obtain information or persuade victims to act.",
                    "learning_objectives": [
                        "Recognise suspicious phone requests.",
                        "Understand caller ID spoofing and impersonation.",
                        "Use safe callback and reporting procedures."
                    ],
                    "overview": (
                        "Vishing uses voice communication to manipulate a person "
                        "into revealing confidential information, approving a "
                        "transaction, installing software, or disclosing verification codes."
                    ),
                    "how_it_works": [
                        "The caller claims to represent a bank, technical support team, or government service.",
                        "The caller describes a problem or creates a sense of urgency.",
                        "The victim is asked to reveal information or perform an action.",
                        "The attacker may use the information to access accounts or commit fraud."
                    ],
                    "warning_signs": [
                        "Requests for passwords, PINs, or one-time codes.",
                        "Pressure to act immediately.",
                        "Instructions to install remote-access software unexpectedly.",
                        "Requests to move money to a supposedly safe account.",
                        "A caller who discourages independent verification."
                    ],
                    "real_world_examples": [
                        {
                            "title": "The fake bank representative",
                            "scenario": (
                                "A caller claims that a bank account is compromised "
                                "and asks the customer to read out a one-time code."
                            ),
                            "lesson": (
                                "End the call and contact the bank using the number "
                                "on its official website or payment card."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The suspicious security call",
                        "background": (
                            "A fictional customer receives a call from someone "
                            "claiming to work for the bank's fraud department."
                        ),
                        "events": [
                            "The caller claims an urgent transaction needs to be stopped.",
                            "The caller asks for a one-time authentication code.",
                            "The caller discourages the customer from ending the call."
                        ],
                        "analysis": (
                            "Legitimate security staff should not require customers "
                            "to disclose authentication codes to an unsolicited caller. "
                            "Caller ID alone is not proof of identity."
                        ),
                        "response": [
                            "Do not disclose the code.",
                            "End the call if it feels suspicious.",
                            "Call the bank using an independently verified number.",
                            "Report any disclosed information or unauthorised transaction promptly."
                        ],
                        "lesson": "A caller's claimed identity must be verified independently."
                    },
                    "simulation": {
                        "title": "The urgent bank call",
                        "instructions": "Choose the safest response to this fictional call.",
                        "scenario": (
                            "A caller claims to be from your bank and asks you to "
                            "read out a one-time code to stop a suspicious transaction."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Read out the code",
                            "End the call and contact the bank through an official number",
                            "Give the caller your banking PIN",
                            "Install software at the caller's request"
                        ],
                        "correct_answer": 1,
                        "explanation": "Never disclose authentication codes to an unsolicited caller; independently contact the bank."
                    },
                    "practical_lab": {
                        "title": "Voice Phishing Response Exercise",
                        "objective": "Practise responding safely to a fictional suspicious call.",
                        "environment": "Offline role-play or written exercise",
                        "steps": [
                            "Read the fictional call scenario.",
                            "Identify the requested information or action.",
                            "List the pressure tactics used by the caller.",
                            "Write a safe way to end and verify the call.",
                            "Record the steps you would take if information had already been disclosed."
                        ],
                        "expected_result": (
                            "The learner refuses to disclose secrets and independently "
                            "contacts the legitimate organisation."
                        ),
                        "safety_note": "Use a fictional script only; do not call real people or organisations as part of the exercise."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "What is vishing?",
                                "options": [
                                    "Phishing through voice calls",
                                    "A type of data backup",
                                    "A firewall configuration",
                                    "A file compression method"
                                ],
                                "answer": 0,
                                "explanation": "Vishing uses voice communication to carry out phishing."
                            },
                            {
                                "question": "A caller asks for your one-time code. What is safest?",
                                "options": [
                                    "Share it if the caller knows your name",
                                    "Share it if the caller sounds professional",
                                    "Do not disclose it and verify the call independently",
                                    "Send it through a text message instead"
                                ],
                                "answer": 2,
                                "explanation": "Never disclose authentication codes to an unsolicited caller."
                            }
                        ]
                    },
                    "prevention": [
                        "Do not disclose passwords, PINs, or authentication codes during unsolicited calls.",
                        "End suspicious calls and use independently verified contact details.",
                        "Never install remote-access tools at an unsolicited caller's direction.",
                        "Verify payment requests through established organisational procedures.",
                        "Report suspected fraud to the relevant organisation."
                    ],
                    "conclusion": (
                        "Vishing relies on persuasive conversation and pressure. "
                        "Ending suspicious calls, protecting authentication codes, "
                        "and verifying callers independently are effective safeguards."
                    )
                }
            }
        },
        "clone_phishing": {
            "id": "clone-phishing",
            "name": "Clone Phishing",
            "description": "A fraudulent message that imitates a legitimate message or notification.",
            "types": {
                "message_cloning": {
                    "id": "message-cloning",
                    "name": "Cloned Message Attacks",
                    "summary": "Attackers copy the appearance or context of a genuine message while substituting a harmful link or attachment.",
                    "learning_objectives": [
                        "Understand how familiar messages can be imitated.",
                        "Identify unexpected changes to links and attachments.",
                        "Verify repeated or replacement messages safely."
                    ],
                    "overview": (
                        "Clone phishing imitates a legitimate message, sometimes "
                        "claiming to resend an earlier email or provide an updated "
                        "document. The replacement message contains a fraudulent "
                        "link or attachment."
                    ),
                    "how_it_works": [
                        "An attacker obtains or imitates the appearance of a legitimate message.",
                        "A replacement message is presented as an update or resend.",
                        "A link or attachment is changed to direct the recipient toward a fraudulent destination.",
                        "The recipient may trust the familiar subject or context and interact with the content."
                    ],
                    "warning_signs": [
                        "An unexpected resend of a familiar document.",
                        "A changed sender address or destination domain.",
                        "A request to sign in again to view a routine file.",
                        "An attachment that was not expected.",
                        "A message whose explanation does not match the surrounding conversation."
                    ],
                    "real_world_examples": [
                        {
                            "title": "The replacement document",
                            "scenario": (
                                "A colleague appears to resend a meeting document, "
                                "but the new message asks the recipient to sign in "
                                "through an unfamiliar website."
                            ),
                            "lesson": (
                                "Confirm the resend with the colleague and access "
                                "the document through the usual trusted platform."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The unexpected document resend",
                        "background": (
                            "A fictional employee receives a second message with "
                            "the same subject as a document shared earlier."
                        ),
                        "events": [
                            "The new message claims the earlier attachment was replaced.",
                            "The new link leads to a different domain.",
                            "The page asks for the employee's account password."
                        ],
                        "analysis": (
                            "A familiar subject does not guarantee a familiar "
                            "destination. Unexpected sign-in prompts and changed "
                            "links deserve independent verification."
                        ),
                        "response": [
                            "Do not enter credentials on the unfamiliar page.",
                            "Contact the supposed sender through an established channel.",
                            "Open the document through the usual trusted platform.",
                            "Report the suspicious message."
                        ],
                        "lesson": "Verify unexpected replacement messages instead of relying on familiar formatting."
                    },
                    "simulation": {
                        "title": "The replacement attachment",
                        "instructions": "Choose the safest response.",
                        "scenario": (
                            "A familiar email subject appears again, but this time "
                            "the message directs you to a new sign-in page."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Enter your password because the subject is familiar",
                            "Verify with the sender and access the document through the usual platform",
                            "Disable browser security",
                            "Forward the link to colleagues"
                        ],
                        "correct_answer": 1,
                        "explanation": "Unexpected links and replacement attachments should be verified independently."
                    },
                    "practical_lab": {
                        "title": "Message Comparison Lab",
                        "objective": "Compare two fictional messages and identify suspicious differences.",
                        "environment": "Offline document comparison",
                        "steps": [
                            "Read the original fictional message and its alleged replacement.",
                            "Compare sender details, links, attachments, and requested actions.",
                            "Record any differences that require verification.",
                            "Choose a trusted way to access the original document.",
                            "Write a brief incident note."
                        ],
                        "expected_result": (
                            "The learner identifies unexpected changes and avoids "
                            "entering credentials on an unverified page."
                        ),
                        "safety_note": "Use fictional messages and text-only URLs; do not open suspicious links."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "What is a characteristic of clone phishing?",
                                "options": [
                                    "Imitating a legitimate message with altered harmful content",
                                    "Encrypting a personal backup",
                                    "Updating an operating system",
                                    "Creating a normal calendar event"
                                ],
                                "answer": 0,
                                "explanation": "Clone phishing imitates a familiar legitimate message while substituting dangerous content."
                            },
                            {
                                "question": "A replacement email contains an unexpected sign-in link. What should you do?",
                                "options": [
                                    "Enter credentials immediately",
                                    "Verify the message and use the trusted platform",
                                    "Disable multifactor authentication",
                                    "Share the link publicly"
                                ],
                                "answer": 1,
                                "explanation": "Verify the replacement and access the document through an established channel."
                            }
                        ]
                    },
                    "prevention": [
                        "Check links and sender details even in familiar conversations.",
                        "Verify unexpected resends or replacement attachments.",
                        "Access shared documents through trusted platforms.",
                        "Use multifactor authentication and report suspicious messages."
                    ],
                    "conclusion": (
                        "Clone phishing exploits familiarity. Comparing message "
                        "details and verifying unexpected changes helps prevent "
                        "credential theft and unsafe downloads."
                    )
                }
            }
        },
        "pharming": {
            "id": "pharming",
            "name": "Pharming",
            "description": "Redirecting users toward fraudulent websites that imitate legitimate destinations.",
            "types": {
                "fraudulent_redirection": {
                    "id": "fraudulent-redirection",
                    "name": "Fraudulent Website Redirection",
                    "summary": "Pharming attempts to direct users to a fake website, potentially without relying on a convincing message link.",
                    "learning_objectives": [
                        "Explain the purpose of pharming.",
                        "Recognise suspicious website destinations and security warnings.",
                        "Understand basic protective measures against fraudulent redirection."
                    ],
                    "overview": (
                        "Pharming involves redirecting a user to a fraudulent "
                        "website that imitates a legitimate service. Redirection "
                        "may involve tampering with local name-resolution settings "
                        "or compromising DNS-related infrastructure."
                    ),
                    "how_it_works": [
                        "An attacker manipulates a mechanism used to locate a website or influences the user toward a fraudulent destination.",
                        "The victim reaches a page that imitates a trusted service.",
                        "The page may request credentials or payment details.",
                        "Submitted information may be stolen or misused."
                    ],
                    "warning_signs": [
                        "Unexpected browser security warnings.",
                        "A website address that differs from the expected domain.",
                        "Unusual login prompts or unfamiliar page behaviour.",
                        "Unexpected redirects after entering a known address.",
                        "Requests for information unrelated to the service."
                    ],
                    "real_world_examples": [
                        {
                            "title": "The imitation banking page",
                            "scenario": (
                                "A user attempts to access online banking but "
                                "encounters an unexpected redirect to a page that "
                                "looks almost identical to the bank's website."
                            ),
                            "lesson": (
                                "Stop before entering credentials, check the address, "
                                "and contact the bank through a trusted channel."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The unexpected banking redirect",
                        "background": (
                            "A fictional user types a familiar banking address "
                            "but arrives at an unfamiliar login page."
                        ),
                        "events": [
                            "The page looks similar to the bank's branding.",
                            "The browser displays an unexpected security warning.",
                            "The page requests account credentials."
                        ],
                        "analysis": (
                            "A familiar-looking page is not proof of authenticity. "
                            "Unexpected redirection and security warnings must be "
                            "taken seriously."
                        ),
                        "response": [
                            "Do not enter credentials or ignore the warning.",
                            "Close the suspicious page.",
                            "Access the bank through its verified application or trusted contact method.",
                            "Run appropriate security checks and report the incident if redirection persists."
                        ],
                        "lesson": "Visual similarity cannot replace checking a site's identity and security."
                    },
                    "simulation": {
                        "title": "A website that looks right",
                        "instructions": "Choose the safest action.",
                        "scenario": (
                            "A banking page looks familiar, but your browser shows "
                            "an unexpected security warning and the address looks unusual."
                        ),
                        "question": "What should you do?",
                        "options": [
                            "Ignore the warning and sign in",
                            "Enter a small test payment",
                            "Stop and access the bank through a verified route",
                            "Share your credentials with support in a chat"
                        ],
                        "correct_answer": 2,
                        "explanation": "Stop and verify the destination through a trusted route instead of ignoring warnings."
                    },
                    "practical_lab": {
                        "title": "Safe Website Verification",
                        "objective": "Practise recognising suspicious website indicators without visiting dangerous sites.",
                        "environment": "Offline comparison exercise",
                        "steps": [
                            "Compare fictional legitimate and fraudulent domain names supplied by the instructor.",
                            "Identify spelling differences and unexpected subdomains.",
                            "Review the example browser warning.",
                            "Describe a trusted method of reaching the genuine service.",
                            "Write down what to do if repeated redirects occur."
                        ],
                        "expected_result": (
                            "The learner recognises suspicious destinations and "
                            "chooses a verified route to the service."
                        ),
                        "safety_note": "Use fictional domains only. Never test pharming against real services or alter DNS settings on a live network."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "What is the main goal of pharming?",
                                "options": [
                                    "Redirecting users to fraudulent websites",
                                    "Improving website performance",
                                    "Backing up a database",
                                    "Updating a browser"
                                ],
                                "answer": 0,
                                "explanation": "Pharming attempts to direct users to fraudulent destinations."
                            },
                            {
                                "question": "What should you do when a trusted site redirects unexpectedly?",
                                "options": [
                                    "Ignore all warnings",
                                    "Enter your password to test it",
                                    "Stop and verify the destination through a trusted route",
                                    "Install an unknown browser extension"
                                ],
                                "answer": 2,
                                "explanation": "Unexpected redirects should be investigated before credentials are entered."
                            }
                        ]
                    },
                    "prevention": [
                        "Keep browsers, operating systems, and security software updated.",
                        "Pay attention to website addresses and browser security warnings.",
                        "Use trusted bookmarks or official applications for sensitive services.",
                        "Secure home routers and avoid untrusted configuration changes.",
                        "Contact the organisation through a known channel if a redirect seems suspicious."
                    ],
                    "conclusion": (
                        "Pharming can make a fraudulent destination appear familiar. "
                        "Checking website identity, respecting browser warnings, "
                        "and using trusted routes reduce the risk of credential theft."
                    )
                }
            }
        },
        "business_email_compromise": {
            "id": "business-email-compromise",
            "name": "Business Email Compromise",
            "description": "Fraud that abuses or impersonates business email accounts to manipulate payments or information sharing.",
            "types": {
                "payment_and_invoice_fraud": {
                    "id": "payment-and-invoice-fraud",
                    "name": "Payment and Invoice Fraud",
                    "summary": "Attackers impersonate business contacts or misuse email accounts to redirect payments or obtain sensitive information.",
                    "learning_objectives": [
                        "Recognise payment and invoice manipulation.",
                        "Understand the importance of independently verifying account changes.",
                        "Apply safe business communication and approval procedures."
                    ],
                    "overview": (
                        "Business email compromise (BEC) is a form of fraud "
                        "involving impersonation or misuse of business email. "
                        "It often targets payments, invoices, payroll details, "
                        "or confidential business information."
                    ),
                    "how_it_works": [
                        "The attacker impersonates a supplier, employee, or executive, or gains access to an account.",
                        "The attacker sends a plausible business request.",
                        "The request asks for a payment, bank-detail change, or confidential information.",
                        "If the request is not independently checked, money or data may be lost."
                    ],
                    "warning_signs": [
                        "Unexpected changes to supplier bank details.",
                        "Requests to bypass established financial controls.",
                        "Unusual secrecy or pressure to pay quickly.",
                        "A sender address with subtle differences.",
                        "A request that differs from the usual payment process."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Changed supplier account",
                            "scenario": (
                                "A fictional supplier emails a company to say that "
                                "all future payments must go to a new bank account."
                            ),
                            "lesson": (
                                "Confirm the change with the supplier using "
                                "previously verified contact details and follow "
                                "the company's approval process."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The changed invoice details",
                        "background": (
                            "A finance team receives an invoice containing bank "
                            "details different from those used previously."
                        ),
                        "events": [
                            "The email requests payment before the end of the day.",
                            "The sender discourages telephone confirmation.",
                            "The new account details have not been independently verified."
                        ],
                        "analysis": (
                            "A change in payment details combined with urgency "
                            "and resistance to verification is a serious warning sign."
                        ),
                        "response": [
                            "Pause the payment.",
                            "Contact the supplier using an existing verified number.",
                            "Follow the organisation's payment approval process.",
                            "Notify finance and security teams if fraud is suspected."
                        ],
                        "lesson": "Verify payment changes independently, even when the invoice looks routine."
                    },
                    "simulation": {
                        "title": "Verify the invoice",
                        "instructions": "Choose the correct response.",
                        "scenario": (
                            "A supplier emails new bank details and requests "
                            "immediate payment without the usual confirmation."
                        ),
                        "question": "What is the safest response?",
                        "options": [
                            "Pay immediately",
                            "Confirm the new details using a previously verified contact and follow approval rules",
                            "Reply asking the sender for your password",
                            "Delete all financial records"
                        ],
                        "correct_answer": 1,
                        "explanation": "Independent confirmation and established approval controls help prevent payment fraud."
                    },
                    "practical_lab": {
                        "title": "Business Email Fraud Review",
                        "objective": "Assess a fictional payment-change request.",
                        "environment": "Offline business-process exercise",
                        "steps": [
                            "Review the fictional invoice and accompanying email.",
                            "Compare the payment instructions with the established process.",
                            "List the warning signs and information requiring verification.",
                            "Draft a safe verification message or call checklist.",
                            "Record the decision and the appropriate reporting route."
                        ],
                        "expected_result": (
                            "The learner identifies the payment-change risk and "
                            "documents the required independent verification."
                        ),
                        "safety_note": "Use fictional invoices and account details only. Do not make real payments."
                    },
                    "assessment": {
                        "questions": [
                            {
                                "question": "What is a common objective of business email compromise?",
                                "options": [
                                    "Redirecting payments or obtaining sensitive business information",
                                    "Improving employee training",
                                    "Updating company calendars",
                                    "Reducing network latency"
                                ],
                                "answer": 0,
                                "explanation": "BEC commonly targets business payments and confidential information."
                            },
                            {
                                "question": "A supplier requests a new bank account. What should finance do?",
                                "options": [
                                    "Change the account immediately",
                                    "Verify the change using established contact details",
                                    "Share the request publicly",
                                    "Ignore approval procedures"
                                ],
                                "answer": 1,
                                "explanation": "Payment changes should be independently verified before being applied."
                            }
                        ]
                    },
                    "prevention": [
                        "Verify bank-detail changes through previously confirmed contact details.",
                        "Use dual approval for sensitive payments.",
                        "Protect email accounts with multifactor authentication.",
                        "Train employees to recognise impersonation and unusual requests.",
                        "Report suspicious transactions and preserve relevant messages."
                    ],
                    "conclusion": (
                        "Business email compromise often resembles ordinary work. "
                        "Independent payment verification, strong email security, "
                        "and consistent approval procedures help prevent costly fraud."
                    )
                }
            }
        }
    }
}