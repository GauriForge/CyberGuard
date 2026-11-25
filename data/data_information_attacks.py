
DATA_INFORMATION_ATTACKS = {
    "id": "data-information",
    "name": "Data and Information Attacks",
    "description": "Attacks that compromise the confidentiality, integrity or availability of sensitive information.",

    "subcategories": {
        "data_theft_and_exfiltration": {
            "id": "data-theft-and-exfiltration",
            "name": "Data Theft and Exfiltration",
            "description": "Attacks involving unauthorised collection, copying or transfer of sensitive information.",

            "types": {
                "data_exfiltration": {
                    "id": "data-exfiltration",
                    "name": "Data Exfiltration",

                    "overview": "Data exfiltration is the unauthorised transfer of information from an organisation, device or system to an external destination. It may occur through compromised accounts, malicious software, insecure cloud storage or misuse of legitimate access.",

                    "how_it_works": [
                        "An attacker gains access to sensitive information.",
                        "The attacker identifies valuable files, records or databases.",
                        "Information is copied or transferred through an available channel.",
                        "The transfer may go unnoticed if monitoring and access controls are weak."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unauthorised Transfer of Customer Records",
                            "description": "An employee account is compromised and used to download customer records that the account holder would not normally need for their role."
                        },
                        {
                            "title": "Sensitive Files in an External Cloud Account",
                            "description": "An organisation discovers that confidential documents were copied to an unauthorised external storage account."
                        }
                    ],

                    "case_study": {
                        "title": "The Missing Customer Database",
                        "scenario": "A company's security team detects an unusually large transfer of customer information outside its network. An investigation finds that a compromised account had broader permissions than necessary.",
                        "findings": [
                            "The account could access more records than its role required.",
                            "Large downloads were not generating timely alerts.",
                            "The organisation lacked clear controls for external data transfers."
                        ],
                        "lesson": "Least-privilege access, data-loss prevention and centralised monitoring can reduce the risk and impact of data exfiltration."
                    },

                    "simulation": {
                        "title": "Investigate an Unusual Data Transfer",
                        "scenario": "A fictional monitoring dashboard reports that an account downloaded thousands of records outside normal working hours.",
                        "tasks": [
                            "Compare the activity with the account's usual behaviour.",
                            "Identify the records and systems involved.",
                            "Decide which events require immediate investigation.",
                            "Recommend containment and evidence-preservation steps."
                        ],
                        "expected_learning": "Recognise suspicious data-transfer patterns and understand how incident responders investigate possible information theft."
                    },

                    "practical_lab": {
                        "title": "Data Exfiltration Detection Lab",
                        "objective": "Identify potentially unauthorised data transfers from fictional security logs.",
                        "activities": [
                            "Review sample file-access and network-transfer logs.",
                            "Identify unusual transfer volumes and destinations.",
                            "Determine whether the account had a legitimate business need.",
                            "Write a short incident report with recommended controls."
                        ],
                        "safety": "Use synthetic logs and sample files only. Do not copy confidential information or test against systems without authorisation."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What does data exfiltration mean?",
                                "options": [
                                    "Unauthorised transfer of information out of a system",
                                    "Creating an encrypted backup",
                                    "Installing an approved software update",
                                    "Deleting temporary files during maintenance"
                                ],
                                "answer": "Unauthorised transfer of information out of a system",
                                "explanation": "Data exfiltration involves information leaving a system or organisation without appropriate authorisation."
                            },
                            {
                                "question": "Which control can help detect suspicious data transfers?",
                                "options": [
                                    "Data-loss prevention and transfer monitoring",
                                    "Removing all access logs",
                                    "Giving every user administrator access",
                                    "Disabling security alerts"
                                ],
                                "answer": "Data-loss prevention and transfer monitoring",
                                "explanation": "Monitoring and data-loss prevention can identify or restrict transfers that violate organisational policies."
                            }
                        ]
                    },

                    "prevention": [
                        "Apply least-privilege access to files and databases.",
                        "Monitor unusual downloads and outbound data transfers.",
                        "Use data-loss prevention controls where appropriate.",
                        "Encrypt sensitive information at rest and in transit.",
                        "Review external sharing permissions and investigate suspicious activity."
                    ],

                    "conclusion": "Data exfiltration can expose valuable information and damage trust. Appropriate access restrictions, monitoring and data-handling policies help prevent unauthorised transfers."
                },

                "data_breach": {
                    "id": "data-breach",
                    "name": "Data Breach",

                    "overview": "A data breach occurs when sensitive, confidential or protected information is accessed, disclosed or acquired without authorisation. Breaches may result from cyberattacks, human error, misconfigured services or the loss of devices containing sensitive data.",

                    "how_it_works": [
                        "An attacker exploits a vulnerability or obtains unauthorised access, or information is exposed accidentally.",
                        "Sensitive records become accessible to an unauthorised party.",
                        "The organisation identifies the exposure through reports, alerts or investigation.",
                        "The organisation contains the incident and assesses the information affected."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Misconfigured Cloud Storage Service",
                            "description": "A company accidentally makes a storage location containing customer documents publicly accessible."
                        },
                        {
                            "title": "A Lost Unencrypted Device",
                            "description": "An employee loses a device containing confidential files that were not adequately protected."
                        }
                    ],

                    "case_study": {
                        "title": "The Publicly Accessible Records",
                        "scenario": "A routine security review reveals that a cloud storage location containing customer documents could be accessed without the intended restrictions.",
                        "findings": [
                            "Storage permissions were configured incorrectly.",
                            "The organisation did not regularly review public exposure.",
                            "The scope and duration of the exposure required investigation."
                        ],
                        "lesson": "Secure default configurations, regular exposure reviews and an established incident-response process help reduce data-breach risk."
                    },

                    "simulation": {
                        "title": "Respond to a Suspected Data Breach",
                        "scenario": "A security alert indicates that a collection of confidential documents may have been accessible to unauthorised users.",
                        "tasks": [
                            "Identify the affected system and information.",
                            "Determine how access should be restricted.",
                            "Preserve relevant logs and evidence.",
                            "Identify the stakeholders who need to be informed under applicable policies and laws."
                        ],
                        "expected_learning": "Understand the initial steps involved in investigating and responding to a data breach."
                    },

                    "practical_lab": {
                        "title": "Data Breach Response Lab",
                        "objective": "Develop a response plan for a simulated information exposure.",
                        "activities": [
                            "Review a fictional incident timeline.",
                            "Classify the sensitivity of exposed records.",
                            "Recommend immediate containment measures.",
                            "Prepare an incident summary and remediation checklist."
                        ],
                        "safety": "Use fictional records and a mock incident environment. Do not expose or upload real personal information."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which situation may constitute a data breach?",
                                "options": [
                                    "Confidential records become accessible to unauthorised people",
                                    "An employee receives an approved software update",
                                    "A backup is stored with proper access controls",
                                    "A user changes a display preference"
                                ],
                                "answer": "Confidential records become accessible to unauthorised people",
                                "explanation": "A data breach involves unauthorised access to, disclosure of or acquisition of protected information."
                            },
                            {
                                "question": "What should an organisation do after discovering a suspected breach?",
                                "options": [
                                    "Contain the exposure and investigate its scope",
                                    "Delete all evidence immediately",
                                    "Ignore the incident if the system still works",
                                    "Publish every affected user's information"
                                ],
                                "answer": "Contain the exposure and investigate its scope",
                                "explanation": "Containment and evidence-based investigation help limit harm and establish what happened."
                            }
                        ]
                    },

                    "prevention": [
                        "Restrict access to confidential records.",
                        "Encrypt sensitive information and protect encryption keys.",
                        "Review cloud storage permissions and system configurations.",
                        "Maintain tested backups and an incident-response plan.",
                        "Train staff in secure information handling and reporting."
                    ],

                    "conclusion": "Data breaches can occur through both malicious activity and accidental exposure. Prevention, early detection and a structured response reduce their consequences."
                },

                "data_leakage": {
                    "id": "data-leakage",
                    "name": "Data Leakage",

                    "overview": "Data leakage is the unintended or unauthorised disclosure of information. It can occur when information is shared with the wrong recipient, stored in an exposed location, copied to an unmanaged device or included in an inappropriate message.",

                    "how_it_works": [
                        "Sensitive information is created, stored or shared.",
                        "A mistake, insecure configuration or malicious action exposes the information.",
                        "An unauthorised recipient may view, retain or redistribute it.",
                        "The organisation investigates the exposure and takes steps to prevent recurrence."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Email Sent to the Wrong Recipient",
                            "description": "An employee accidentally emails a spreadsheet containing confidential customer details to an external recipient."
                        },
                        {
                            "title": "An Unprotected Shared Document",
                            "description": "A document containing internal business information is shared using a link that permits access beyond the intended audience."
                        }
                    ],

                    "case_study": {
                        "title": "The Incorrectly Shared Spreadsheet",
                        "scenario": "An employee shares a spreadsheet with an external partner but selects a broader sharing option than intended.",
                        "findings": [
                            "The sharing permissions were not checked before sending.",
                            "The document contained more information than the partner needed.",
                            "The organisation lacked a consistent process for reviewing external sharing."
                        ],
                        "lesson": "Data minimisation, recipient verification and restricted sharing settings reduce accidental information exposure."
                    },

                    "simulation": {
                        "title": "Choose the Safe Sharing Option",
                        "scenario": "A fictional employee must share a report containing both public information and confidential customer details.",
                        "tasks": [
                            "Identify information that should not be shared.",
                            "Determine which recipient needs access.",
                            "Select a restricted sharing method.",
                            "Explain how to report an accidental disclosure."
                        ],
                        "expected_learning": "Recognise common causes of data leakage and select safer information-sharing practices."
                    },

                    "practical_lab": {
                        "title": "Information-Sharing Review Lab",
                        "objective": "Review sample document-sharing scenarios and identify leakage risks.",
                        "activities": [
                            "Inspect fictional sharing permissions.",
                            "Identify excessive access and unnecessary personal data.",
                            "Recommend appropriate restrictions.",
                            "Prepare a checklist for safe document sharing."
                        ],
                        "safety": "Use fictional documents and mock sharing settings only."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which situation is an example of data leakage?",
                                "options": [
                                    "Sending confidential information to the wrong recipient",
                                    "Encrypting a document before authorised sharing",
                                    "Deleting an expired temporary file",
                                    "Applying a security update"
                                ],
                                "answer": "Sending confidential information to the wrong recipient",
                                "explanation": "Information can leak through accidental disclosure as well as deliberate attacks."
                            },
                            {
                                "question": "What is a good way to reduce accidental data leakage?",
                                "options": [
                                    "Verify recipients and restrict document permissions",
                                    "Share every document publicly",
                                    "Include unnecessary personal information",
                                    "Disable access reviews"
                                ],
                                "answer": "Verify recipients and restrict document permissions",
                                "explanation": "Checking recipients and limiting access reduces the chance of exposing information unintentionally."
                            }
                        ]
                    },

                    "prevention": [
                        "Verify recipients before sending confidential information.",
                        "Restrict document-sharing permissions.",
                        "Share only the information required for the task.",
                        "Use approved storage and collaboration services.",
                        "Train employees to report accidental disclosures promptly."
                    ],

                    "conclusion": "Data leakage often results from everyday handling mistakes as well as security weaknesses. Careful sharing practices and appropriate access controls help keep information private."
                }
            }
        },

        "data_integrity_attacks": {
            "id": "data-integrity-attacks",
            "name": "Data Integrity Attacks",
            "description": "Attacks that alter, corrupt or manipulate information without appropriate authorisation.",

            "types": {
                "data_tampering": {
                    "id": "data-tampering",
                    "name": "Data Tampering",

                    "overview": "Data tampering occurs when information is changed without authorisation. The affected information might include financial records, application settings, business transactions or stored documents. Even small changes can produce serious consequences when systems rely on the accuracy of that information.",

                    "how_it_works": [
                        "An attacker or unauthorised user obtains access to stored or transmitted information.",
                        "One or more records or values are modified.",
                        "The change may remain unnoticed if integrity checks are absent.",
                        "Incorrect information may influence later decisions or system operations."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unauthorised Financial Record Changes",
                            "description": "A business discovers changes to payment details that were not approved by the authorised finance team."
                        },
                        {
                            "title": "Modified Application Configuration",
                            "description": "An unauthorised change to a system configuration causes an application to behave incorrectly."
                        }
                    ],

                    "case_study": {
                        "title": "The Altered Transaction Record",
                        "scenario": "An organisation finds discrepancies between its financial records and approved transaction reports. An investigation identifies modifications made through an account with excessive permissions.",
                        "findings": [
                            "Sensitive records could be edited without adequate review.",
                            "Changes were not consistently recorded in an audit trail.",
                            "The organisation lacked an effective reconciliation process."
                        ],
                        "lesson": "Restrict write permissions, maintain tamper-resistant audit logs and verify important records against trusted sources."
                    },

                    "simulation": {
                        "title": "Detect an Unauthorised Record Change",
                        "scenario": "A fictional system provides an approved record, a later version and a log of changes.",
                        "tasks": [
                            "Compare the original and modified values.",
                            "Identify changes without an authorised explanation.",
                            "Determine which records need verification.",
                            "Recommend a safe restoration and investigation process."
                        ],
                        "expected_learning": "Recognise data-integrity problems and understand how audit trails support investigations."
                    },

                    "practical_lab": {
                        "title": "Data Integrity Verification Lab",
                        "objective": "Identify unexpected changes in a set of fictional records.",
                        "activities": [
                            "Compare two versions of a sample dataset.",
                            "Review the accompanying change log.",
                            "Identify discrepancies that require investigation.",
                            "Propose integrity checks and controlled recovery steps."
                        ],
                        "safety": "Use disposable sample data. Do not modify production records or real financial information."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is data tampering?",
                                "options": [
                                    "Unauthorised modification of information",
                                    "Creating an approved backup",
                                    "Viewing a public document",
                                    "Applying a routine security update"
                                ],
                                "answer": "Unauthorised modification of information",
                                "explanation": "Data tampering changes information without appropriate permission or approval."
                            },
                            {
                                "question": "Which control helps detect unauthorised record changes?",
                                "options": [
                                    "Audit logs and integrity verification",
                                    "Unrestricted write access",
                                    "Deleting change history",
                                    "Sharing administrator credentials"
                                ],
                                "answer": "Audit logs and integrity verification",
                                "explanation": "Audit trails and integrity checks help identify and investigate unexpected changes."
                            }
                        ]
                    },

                    "prevention": [
                        "Restrict modification rights to authorised users.",
                        "Maintain reliable audit logs.",
                        "Use integrity verification for important files and records.",
                        "Require approval for sensitive transactions and configuration changes.",
                        "Maintain tested backups and reconcile critical records."
                    ],

                    "conclusion": "Data tampering threatens the accuracy and trustworthiness of information. Access controls, integrity checks and reliable audit trails help detect and prevent unauthorised changes."
                },

                "database_manipulation": {
                    "id": "database-manipulation",
                    "name": "Database Manipulation",

                    "overview": "Database manipulation in a security context involves unauthorised changes to database records, structures or stored information. It may result from compromised credentials, excessive permissions, vulnerable applications or misuse by an insider.",

                    "how_it_works": [
                        "An attacker or unauthorised user gains access to a database or an application connected to it.",
                        "Weak permissions or application vulnerabilities provide a path to unauthorised operations.",
                        "Records may be inserted, changed or deleted.",
                        "The effects may spread to reports, transactions and other dependent systems."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unauthorised Changes to Inventory",
                            "description": "A retail organisation discovers that stock quantities in its database have been changed without matching warehouse transactions."
                        },
                        {
                            "title": "Altered Customer Account Details",
                            "description": "A compromised application account is used to modify customer details without the required approval."
                        }
                    ],

                    "case_study": {
                        "title": "The Inconsistent Inventory Database",
                        "scenario": "A business notices that its reported stock levels do not match physical inventory. Database auditing shows changes made by an account that should only have read access.",
                        "findings": [
                            "The application account had excessive write permissions.",
                            "Database changes were not sufficiently monitored.",
                            "The organisation lacked regular reconciliation."
                        ],
                        "lesson": "Separate database roles, use parameterised queries in applications, audit sensitive operations and validate important transactions."
                    },

                    "simulation": {
                        "title": "Review Database Audit Events",
                        "scenario": "A fictional database audit report includes approved updates, unusual deletions and changes made by a read-only account.",
                        "tasks": [
                            "Identify operations inconsistent with the account's role.",
                            "Determine which changes require verification.",
                            "Recommend containment and restoration steps.",
                            "Explain how role separation would reduce the risk."
                        ],
                        "expected_learning": "Understand database permission boundaries and the importance of monitoring sensitive operations."
                    },

                    "practical_lab": {
                        "title": "Database Permission Audit Lab",
                        "objective": "Review a mock database permission table and identify excessive privileges.",
                        "activities": [
                            "Inspect fictional database users and assigned roles.",
                            "Compare permissions with required application functions.",
                            "Identify unnecessary insert, update and delete privileges.",
                            "Recommend a least-privilege role configuration."
                        ],
                        "safety": "Use a local sample database with fictional data. Do not experiment on production databases."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which practice reduces unauthorised database modifications?",
                                "options": [
                                    "Assigning only the database permissions each account needs",
                                    "Giving all users full database access",
                                    "Disabling database auditing",
                                    "Using shared administrator credentials"
                                ],
                                "answer": "Assigning only the database permissions each account needs",
                                "explanation": "Least-privilege database roles limit the operations available to each account."
                            },
                            {
                                "question": "How should an application safely include user input in SQL queries?",
                                "options": [
                                    "Use parameterised queries",
                                    "Concatenate all input directly into SQL statements",
                                    "Disable input validation",
                                    "Grant the application unrestricted database permissions"
                                ],
                                "answer": "Use parameterised queries",
                                "explanation": "Parameterised queries help keep user-provided values separate from SQL command structure."
                            }
                        ]
                    },

                    "prevention": [
                        "Apply least-privilege database roles.",
                        "Use parameterised queries and safe database APIs.",
                        "Validate input and enforce application-level authorisation.",
                        "Audit sensitive database operations.",
                        "Back up important data and test recovery procedures."
                    ],

                    "conclusion": "Database manipulation can undermine business operations and information accuracy. Secure application queries, restricted database permissions and auditing help protect critical records."
                }
            }
        },

        "data_availability_attacks": {
            "id": "data-availability-attacks",
            "name": "Data Availability Attacks",
            "description": "Attacks that prevent authorised users from accessing required information.",

            "types": {
                "ransomware_data_encryption": {
                    "id": "ransomware-data-encryption",
                    "name": "Ransomware Data Encryption",

                    "overview": "Ransomware is malicious software that can encrypt files or otherwise prevent access to data, with attackers commonly demanding payment for restoration or threatening to disclose stolen information. Recovery is not guaranteed even if a ransom is paid.",

                    "how_it_works": [
                        "Malicious software enters a system through a compromised account, vulnerable service or unsafe file.",
                        "The software executes and attempts to access files or connected storage.",
                        "Files may be encrypted or made unavailable.",
                        "The organisation isolates affected systems and begins incident response and recovery."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unavailable Business Documents",
                            "description": "An organisation discovers that shared business documents have become unreadable following a malware incident."
                        },
                        {
                            "title": "Disrupted Healthcare Systems",
                            "description": "A ransomware incident makes some operational systems and records temporarily unavailable, requiring the organisation to activate continuity procedures."
                        }
                    ],

                    "case_study": {
                        "title": "The Encrypted Shared Drive",
                        "scenario": "Employees report that documents on a shared drive cannot be opened. Security monitoring identifies suspicious activity originating from a workstation.",
                        "findings": [
                            "The workstation had access to shared files.",
                            "The organisation needed to determine whether other systems were affected.",
                            "Recovery depended on clean backups and a tested response process."
                        ],
                        "lesson": "Offline or isolated backups, endpoint protection, restricted permissions and rehearsed recovery procedures improve ransomware resilience."
                    },

                    "simulation": {
                        "title": "Ransomware Incident Response",
                        "scenario": "A fictional organisation detects that multiple files have been renamed and can no longer be opened.",
                        "tasks": [
                            "Identify the affected systems and shared resources.",
                            "Recommend safe isolation and escalation steps.",
                            "Identify the evidence responders should preserve.",
                            "Plan restoration from verified clean backups."
                        ],
                        "expected_learning": "Understand ransomware containment, evidence preservation and safe recovery planning."
                    },

                    "practical_lab": {
                        "title": "Ransomware Preparedness Lab",
                        "objective": "Develop a recovery plan using a simulated ransomware incident.",
                        "activities": [
                            "Review a fictional incident timeline.",
                            "Identify critical systems and dependencies.",
                            "Evaluate backup availability and recovery priorities.",
                            "Create a containment and recovery checklist."
                        ],
                        "safety": "Use a tabletop exercise and fictional incident records. Do not execute ransomware or encrypt real files."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is a common effect of ransomware?",
                                "options": [
                                    "Files or systems become inaccessible",
                                    "Every system becomes more secure",
                                    "All backups automatically become usable",
                                    "Authentication is permanently unnecessary"
                                ],
                                "answer": "Files or systems become inaccessible",
                                "explanation": "Ransomware commonly encrypts files or otherwise disrupts access to data."
                            },
                            {
                                "question": "What supports safer recovery after a ransomware incident?",
                                "options": [
                                    "Verified clean backups and a tested recovery plan",
                                    "Connecting every affected device immediately",
                                    "Deleting all logs before investigation",
                                    "Assuming a ransom guarantees recovery"
                                ],
                                "answer": "Verified clean backups and a tested recovery plan",
                                "explanation": "Tested backups and controlled recovery provide a safer path to restoring affected systems."
                            }
                        ]
                    },

                    "prevention": [
                        "Maintain isolated or offline backups and test restoration.",
                        "Keep operating systems and applications patched.",
                        "Use endpoint protection and monitor suspicious behaviour.",
                        "Restrict access to shared folders and administrative accounts.",
                        "Train users to recognise phishing and suspicious attachments."
                    ],

                    "conclusion": "Ransomware can disrupt access to critical information and business services. Layered prevention, isolated backups and rehearsed recovery procedures help organisations respond effectively."
                }
            }
        }
    }
}