
INSIDER_SUPPLY_CHAIN = {
    "id": "insider-supply-chain",
    "name": "Insider and Supply Chain Attacks",
    "description": "Attacks that exploit trusted access, malicious or careless insiders, and weaknesses in third-party suppliers or software dependencies.",

    "subcategories": {
        "insider_threats": {
            "id": "insider-threats",
            "name": "Insider Threats",
            "description": "Security incidents caused by people with legitimate access who intentionally or unintentionally put systems or information at risk.",

            "types": {
                "malicious_insider": {
                    "id": "malicious-insider",
                    "name": "Malicious Insider",

                    "overview": "A malicious insider is an employee, contractor or other trusted person who deliberately misuses authorised access to steal information, damage systems, disclose confidential material or undermine an organisation's operations.",

                    "how_it_works": [
                        "An individual obtains legitimate access through their role.",
                        "The individual deliberately misuses that access for an unauthorised purpose.",
                        "Sensitive information may be copied, records altered or services disrupted.",
                        "Investigators review access logs, change records and other evidence to establish what happened."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unauthorised Customer Data Access",
                            "description": "A staff member accesses customer records unrelated to their assigned duties and shares the information without permission."
                        },
                        {
                            "title": "Deliberate Modification of Business Records",
                            "description": "A trusted employee changes important records outside approved procedures, affecting the accuracy of business reporting."
                        }
                    ],

                    "case_study": {
                        "title": "The Unusual Employee Account Activity",
                        "scenario": "An organisation's monitoring system identifies repeated access to sensitive documents by an employee whose normal duties do not require those files.",
                        "findings": [
                            "The account had access to more information than its role required.",
                            "Access reviews had not been completed regularly.",
                            "The organisation needed to distinguish authorised work from suspicious activity using reliable evidence."
                        ],
                        "lesson": "Least-privilege access, separation of duties and proportionate activity monitoring help reduce insider risk."
                    },

                    "simulation": {
                        "title": "Investigate a Potential Insider Incident",
                        "scenario": "A fictional audit report shows that a staff account accessed restricted files and attempted an unusual bulk download.",
                        "tasks": [
                            "Compare the activity with the user's assigned responsibilities.",
                            "Identify which events require further investigation.",
                            "Recommend appropriate access restrictions while preserving evidence.",
                            "Explain why conclusions should be based on evidence rather than assumptions."
                        ],
                        "expected_learning": "Recognise suspicious insider activity and understand fair, evidence-based incident handling."
                    },

                    "practical_lab": {
                        "title": "Insider Threat Log Analysis",
                        "objective": "Identify access patterns that may indicate misuse of legitimate privileges.",
                        "activities": [
                            "Review fictional authentication and file-access logs.",
                            "Compare user roles with the resources accessed.",
                            "Identify unusual access times or download volumes.",
                            "Write an incident summary with proportionate recommendations."
                        ],
                        "safety": "Use synthetic logs and fictional user accounts only. Do not monitor private accounts or access real employee records without proper authorisation."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What distinguishes a malicious insider from an external attacker?",
                                "options": [
                                    "The insider deliberately misuses trusted access",
                                    "The insider always lacks an account",
                                    "The insider can only attack public websites",
                                    "The insider never has access to organisational information"
                                ],
                                "answer": "The insider deliberately misuses trusted access",
                                "explanation": "Malicious insiders abuse access or trust they already possess."
                            },
                            {
                                "question": "Which control helps limit insider threats?",
                                "options": [
                                    "Least-privilege access and regular permission reviews",
                                    "Giving every employee administrator access",
                                    "Disabling audit logs",
                                    "Sharing accounts between employees"
                                ],
                                "answer": "Least-privilege access and regular permission reviews",
                                "explanation": "Restricting access to legitimate job requirements limits opportunities for misuse."
                            }
                        ]
                    },

                    "prevention": [
                        "Apply least-privilege access and separation of duties.",
                        "Review sensitive permissions regularly.",
                        "Maintain audit logs and monitor unusual activity appropriately.",
                        "Use approval workflows for high-impact operations.",
                        "Revoke access promptly when responsibilities change or employment ends."
                    ],

                    "conclusion": "Malicious insiders can misuse legitimate access in ways that are difficult to distinguish from normal activity. Carefully managed permissions, reliable evidence and consistent access reviews help reduce this risk."
                },

                "negligent_insider": {
                    "id": "negligent-insider",
                    "name": "Negligent Insider",

                    "overview": "A negligent insider unintentionally creates a security risk through carelessness, mistakes or failure to follow established procedures. Unlike a malicious insider, the person does not necessarily intend to cause harm.",

                    "how_it_works": [
                        "A person handles information or systems as part of their normal responsibilities.",
                        "A mistake or unsafe decision bypasses an expected security control.",
                        "Information may be exposed, credentials compromised or a system misconfigured.",
                        "The organisation contains the incident and improves training or safeguards."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Accidental Email Disclosure",
                            "description": "An employee sends a confidential attachment to the wrong recipient after selecting an incorrect autocomplete suggestion."
                        },
                        {
                            "title": "Unsafe Password Handling",
                            "description": "A staff member stores a work password in an unprotected document, making it easier for another person to obtain."
                        }
                    ],

                    "case_study": {
                        "title": "The Misconfigured Shared Folder",
                        "scenario": "An employee creates a shared folder for a project but accidentally grants access to people outside the intended team.",
                        "findings": [
                            "The sharing interface made the scope of access easy to overlook.",
                            "The employee had not received sufficient guidance on sensitive document sharing.",
                            "No automated alert identified the overly broad permissions."
                        ],
                        "lesson": "Clear procedures, secure defaults and helpful system safeguards can prevent mistakes before they expose information."
                    },

                    "simulation": {
                        "title": "Respond to an Accidental Disclosure",
                        "scenario": "A fictional employee reports that a confidential document was sent to an unintended recipient.",
                        "tasks": [
                            "Identify the type of information involved.",
                            "Determine which sharing permissions or links need to be restricted.",
                            "Recommend appropriate reporting and containment steps.",
                            "Suggest a process change that could prevent a repeat incident."
                        ],
                        "expected_learning": "Respond constructively to accidental security incidents and identify practical preventive improvements."
                    },

                    "practical_lab": {
                        "title": "Human Error Risk Review",
                        "objective": "Identify preventable security mistakes in common workplace scenarios.",
                        "activities": [
                            "Review fictional email, password and document-sharing scenarios.",
                            "Identify the unsafe decision in each scenario.",
                            "Choose a safer alternative.",
                            "Create a short security checklist for everyday work."
                        ],
                        "safety": "Use fictional examples and dummy documents. Never include real passwords or confidential company information."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is a negligent insider threat?",
                                "options": [
                                    "An unintended security risk caused by mistakes or carelessness",
                                    "An attack that always requires malicious intent",
                                    "A security update from an authorised vendor",
                                    "A backup created according to policy"
                                ],
                                "answer": "An unintended security risk caused by mistakes or carelessness",
                                "explanation": "Negligent insider incidents arise from unsafe actions or errors rather than necessarily deliberate harm."
                            },
                            {
                                "question": "Which measure can reduce accidental information disclosure?",
                                "options": [
                                    "Safer sharing defaults and practical employee training",
                                    "Removing all confirmation prompts",
                                    "Encouraging password reuse",
                                    "Disabling document access controls"
                                ],
                                "answer": "Safer sharing defaults and practical employee training",
                                "explanation": "Training and well-designed safeguards help users make safer decisions."
                            }
                        ]
                    },

                    "prevention": [
                        "Provide regular, practical security awareness training.",
                        "Use secure defaults for document sharing and system configuration.",
                        "Encourage prompt reporting of mistakes without discouraging transparency.",
                        "Use password managers and multifactor authentication.",
                        "Make sensitive actions easy to review before they are completed."
                    ],

                    "conclusion": "Negligent insider incidents are often preventable. Training, secure defaults and a supportive reporting culture help people avoid mistakes and respond quickly when they occur."
                },

                "compromised_insider_account": {
                    "id": "compromised-insider-account",
                    "name": "Compromised Insider Account",

                    "overview": "A compromised insider account is a legitimate organisational account taken over by an unauthorised person. The attacker may use the account's existing permissions to access information, impersonate the employee or perform unauthorised actions.",

                    "how_it_works": [
                        "An attacker obtains credentials through phishing, password reuse, malware or another compromise.",
                        "The attacker authenticates using the stolen or abused account.",
                        "Existing account permissions may provide access to internal resources.",
                        "Security teams investigate the activity, secure the account and assess potential exposure."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Phishing Against an Employee",
                            "description": "An employee enters their credentials into a fraudulent sign-in page, allowing an attacker to attempt account takeover."
                        },
                        {
                            "title": "Reused Password Compromise",
                            "description": "A password exposed by an unrelated service is reused for a work account, increasing the chance of unauthorised access."
                        }
                    ],

                    "case_study": {
                        "title": "The Employee Account That Logged In from an Unusual Location",
                        "scenario": "A fictional organisation receives an alert for a successful login followed by unusual access to internal documents.",
                        "findings": [
                            "The account owner does not recognise the activity.",
                            "The account lacked an additional authentication factor.",
                            "The investigation must establish which sessions and resources were affected."
                        ],
                        "lesson": "Multifactor authentication, secure credential practices and effective session monitoring reduce the impact of account compromise."
                    },

                    "simulation": {
                        "title": "Secure a Compromised Account",
                        "scenario": "A user reports an unexpected sign-in notification and unfamiliar activity in their work account.",
                        "tasks": [
                            "Identify the immediate steps for reporting the incident.",
                            "Determine when to revoke sessions and reset credentials.",
                            "Review recent account activity for suspicious changes.",
                            "Recommend safeguards against future account takeover."
                        ],
                        "expected_learning": "Understand how compromised accounts are contained and investigated."
                    },

                    "practical_lab": {
                        "title": "Account Compromise Detection Lab",
                        "objective": "Identify suspicious authentication events in fictional login logs.",
                        "activities": [
                            "Review sample login times, device details and authentication outcomes.",
                            "Identify unusual patterns requiring verification.",
                            "Create a response checklist for a potentially compromised account.",
                            "Recommend appropriate multifactor authentication and session controls."
                        ],
                        "safety": "Use synthetic authentication logs and test accounts only. Never submit real credentials to a training exercise."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Why can a compromised employee account be dangerous?",
                                "options": [
                                    "It may provide access through existing legitimate permissions",
                                    "It automatically disables every security control",
                                    "It cannot access internal systems",
                                    "It always requires physical access to a server"
                                ],
                                "answer": "It may provide access through existing legitimate permissions",
                                "explanation": "An attacker may inherit the access available to the compromised account."
                            },
                            {
                                "question": "What should be done when an account is confirmed compromised?",
                                "options": [
                                    "Secure the account, revoke suspicious sessions and investigate activity",
                                    "Ignore the activity if the password still works",
                                    "Share the credentials with colleagues",
                                    "Delete all authentication logs"
                                ],
                                "answer": "Secure the account, revoke suspicious sessions and investigate activity",
                                "explanation": "Account containment and log review help prevent continued misuse and establish the extent of compromise."
                            }
                        ]
                    },

                    "prevention": [
                        "Enable multifactor authentication.",
                        "Use unique passwords and an approved password manager.",
                        "Monitor unusual authentication and account changes.",
                        "Apply least-privilege access to employee accounts.",
                        "Maintain a clear process for reporting and responding to account compromise."
                    ],

                    "conclusion": "A compromised insider account allows an attacker to act through a trusted identity. Strong authentication, restricted permissions and prompt investigation reduce the risk."
                }
            }
        },

        "supply_chain_attacks": {
            "id": "supply-chain-attacks",
            "name": "Supply Chain Attacks",
            "description": "Attacks that exploit weaknesses in software suppliers, service providers, vendors or third-party dependencies.",

            "types": {
                "software_supply_chain_attack": {
                    "id": "software-supply-chain-attack",
                    "name": "Software Supply Chain Attack",

                    "overview": "A software supply chain attack compromises a component, development process, update mechanism or distribution channel that other organisations trust. The resulting malicious or vulnerable software may reach users through an otherwise legitimate supplier or product.",

                    "how_it_works": [
                        "An attacker targets a software supplier, build process, dependency or distribution mechanism.",
                        "A component or update is compromised, or an unsafe dependency is introduced.",
                        "Downstream organisations receive or use the affected software.",
                        "Security teams investigate affected versions, assess exposure and apply trusted remediation."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Compromised Software Update",
                            "description": "A malicious change introduced into a trusted software distribution process causes organisations to receive a harmful update."
                        },
                        {
                            "title": "A Vulnerable Third-Party Library",
                            "description": "An application uses an outdated dependency containing a known vulnerability that attackers later exploit."
                        }
                    ],

                    "case_study": {
                        "title": "The Trusted Update That Caused an Incident",
                        "scenario": "An organisation discovers that a software component received from a supplier is associated with suspicious activity across several systems.",
                        "findings": [
                            "Multiple internal systems used the affected component.",
                            "The organisation did not have a complete inventory of software dependencies.",
                            "The response required coordination with the supplier and verification of remediation."
                        ],
                        "lesson": "Maintain a software inventory, verify updates, assess supplier risk and establish a response process for compromised components."
                    },

                    "simulation": {
                        "title": "Investigate a Suspected Software Supply Chain Incident",
                        "scenario": "A fictional security advisory identifies a potentially compromised component used by several internal applications.",
                        "tasks": [
                            "Identify applications that depend on the affected component.",
                            "Determine which versions are present.",
                            "Review the supplier's advisory and trusted remediation guidance.",
                            "Recommend containment, patching and verification steps."
                        ],
                        "expected_learning": "Understand dependency tracing, supplier coordination and remediation during software supply chain incidents."
                    },

                    "practical_lab": {
                        "title": "Software Dependency Risk Review",
                        "objective": "Review a sample software inventory and identify dependency risks.",
                        "activities": [
                            "Inspect a fictional software bill of materials.",
                            "Identify outdated or flagged components.",
                            "Match affected versions to a mock security advisory.",
                            "Prepare a prioritised remediation plan."
                        ],
                        "safety": "Use sample manifests and a local training environment. Do not install suspicious packages or modify production build systems."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What makes a software supply chain attack different from many direct attacks?",
                                "options": [
                                    "It exploits trust in software suppliers, components or distribution processes",
                                    "It can only target physical computers",
                                    "It always requires an employee to lose a device",
                                    "It affects only software that has no users"
                                ],
                                "answer": "It exploits trust in software suppliers, components or distribution processes",
                                "explanation": "Supply chain attacks take advantage of relationships and dependencies that downstream users trust."
                            },
                            {
                                "question": "What is a software bill of materials useful for?",
                                "options": [
                                    "Identifying components used in a software product",
                                    "Replacing all security testing",
                                    "Guaranteeing that software has no vulnerabilities",
                                    "Providing every user with administrator access"
                                ],
                                "answer": "Identifying components used in a software product",
                                "explanation": "A software bill of materials helps organisations identify dependencies and assess whether known issues affect them."
                            }
                        ]
                    },

                    "prevention": [
                        "Maintain an inventory of applications and software dependencies.",
                        "Review supplier security practices and relevant advisories.",
                        "Verify software signatures and update sources.",
                        "Use dependency scanning and software composition analysis.",
                        "Restrict build-system permissions and protect release pipelines.",
                        "Prepare a process for identifying, containing and remediating compromised components."
                    ],

                    "conclusion": "Software supply chain attacks exploit the trust placed in suppliers and dependencies. Software inventories, verified updates and effective supplier-risk management improve resilience."
                },

                "third_party_vendor_compromise": {
                    "id": "third-party-vendor-compromise",
                    "name": "Third-Party Vendor Compromise",

                    "overview": "A third-party vendor compromise occurs when an attacker breaches a supplier or service provider and uses that access or relationship to affect the supplier's customers. The risk can extend to managed services, cloud platforms, outsourced support and other external business relationships.",

                    "how_it_works": [
                        "An organisation grants a vendor access to systems or information for legitimate work.",
                        "The vendor's systems or credentials are compromised, or the vendor has inadequate security controls.",
                        "The attacker attempts to use the vendor relationship to reach customer environments or information.",
                        "Affected organisations restrict access, coordinate investigations and verify that systems are secure."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Compromised Managed Service Provider",
                            "description": "An attacker compromises a service provider's account and attempts to misuse the remote access available to that provider."
                        },
                        {
                            "title": "A Supplier's Exposed Customer Records",
                            "description": "A third-party provider stores customer information insecurely, resulting in unauthorised exposure."
                        }
                    ],

                    "case_study": {
                        "title": "The External Support Account",
                        "scenario": "A company identifies unusual activity from a vendor account that normally performs approved maintenance on internal systems.",
                        "findings": [
                            "The vendor account had access to several systems.",
                            "Access was not restricted to approved maintenance windows.",
                            "The organisation needed to coordinate with the supplier to determine the extent of the incident."
                        ],
                        "lesson": "Limit third-party access, require strong authentication and monitor vendor activity using clearly defined security requirements."
                    },

                    "simulation": {
                        "title": "Respond to a Vendor Security Alert",
                        "scenario": "A fictional service provider notifies its customers that a support account may have been compromised.",
                        "tasks": [
                            "Identify internal systems and information accessible to the vendor.",
                            "Decide which vendor sessions or permissions need temporary restriction.",
                            "Coordinate incident investigation with the supplier.",
                            "Verify remediation before restoring normal access."
                        ],
                        "expected_learning": "Understand third-party incident coordination and the importance of limiting external access."
                    },

                    "practical_lab": {
                        "title": "Third-Party Access Audit Lab",
                        "objective": "Evaluate vendor permissions and identify unnecessary access.",
                        "activities": [
                            "Review a fictional vendor register and access matrix.",
                            "Identify accounts with excessive permissions.",
                            "Check whether access has an owner, purpose and expiry date.",
                            "Recommend controls for approval, monitoring and revocation."
                        ],
                        "safety": "Use fictional supplier records and mock permissions. Do not access real vendor accounts or systems."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Why can a compromised vendor affect its customers?",
                                "options": [
                                    "The vendor may have trusted access to customer systems or information",
                                    "Vendors never use digital systems",
                                    "Customer systems automatically become immune to attacks",
                                    "Vendor access cannot be restricted"
                                ],
                                "answer": "The vendor may have trusted access to customer systems or information",
                                "explanation": "Third-party relationships can create access paths that attackers may try to exploit."
                            },
                            {
                                "question": "Which practice helps reduce third-party access risk?",
                                "options": [
                                    "Restrict vendor permissions and review them regularly",
                                    "Create permanent unrestricted vendor accounts",
                                    "Share internal administrator passwords",
                                    "Disable monitoring of external access"
                                ],
                                "answer": "Restrict vendor permissions and review them regularly",
                                "explanation": "Limited, monitored and reviewed access reduces the potential impact of a vendor compromise."
                            }
                        ]
                    },

                    "prevention": [
                        "Assess vendor security before granting sensitive access.",
                        "Use multifactor authentication for external accounts.",
                        "Restrict vendor access to approved systems and tasks.",
                        "Monitor and review third-party activity.",
                        "Set clear contractual security and incident-notification requirements.",
                        "Revoke access promptly when a service or contract ends."
                    ],

                    "conclusion": "Third-party compromises can cross organisational boundaries through trusted business relationships. Strong vendor oversight, limited access and coordinated incident response help contain the risk."
                },

                "dependency_confusion_and_typosquatting": {
                    "id": "dependency-confusion-and-typosquatting",
                    "name": "Dependency Confusion and Typosquatting",

                    "overview": "Dependency confusion and typosquatting are software dependency risks. Dependency confusion can occur when a package manager selects an unintended package with a matching name from an untrusted source. Typosquatting uses package names that resemble legitimate packages, hoping developers will select the wrong one.",

                    "how_it_works": [
                        "A development project relies on third-party or internally maintained packages.",
                        "A developer or automated build process resolves a package name from a source that is not the intended trusted source.",
                        "An unintended or malicious package may be installed or included in a build.",
                        "The organisation investigates the dependency, verifies its origin and replaces unsafe components."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Lookalike Package Name",
                            "description": "A developer accidentally installs a package whose name closely resembles a well-known library."
                        },
                        {
                            "title": "An Unexpected Package Source",
                            "description": "A build process resolves a dependency from a public registry instead of the organisation's intended internal package source."
                        }
                    ],

                    "case_study": {
                        "title": "The Unexpected Build Dependency",
                        "scenario": "A development team notices an unfamiliar package in its build report. The package name resembles an approved internal dependency but its source is unexpected.",
                        "findings": [
                            "The build process did not enforce an approved package source.",
                            "The dependency was not checked against the team's trusted manifest.",
                            "The team needed to establish whether the package had executed or affected released software."
                        ],
                        "lesson": "Use trusted registries, dependency pinning and integrity verification to reduce the risk of unintended package installation."
                    },

                    "simulation": {
                        "title": "Review a Suspicious Dependency",
                        "scenario": "A fictional project contains a new dependency whose name differs slightly from an approved package.",
                        "tasks": [
                            "Compare the dependency name with the approved manifest.",
                            "Review its configured source and version.",
                            "Determine whether the dependency should be blocked pending verification.",
                            "Recommend changes to dependency management."
                        ],
                        "expected_learning": "Recognise suspicious dependency names and understand how package source controls protect development environments."
                    },

                    "practical_lab": {
                        "title": "Dependency Manifest Review Lab",
                        "objective": "Identify potentially unsafe package names and sources in a mock project manifest.",
                        "activities": [
                            "Review a fictional dependency manifest.",
                            "Compare packages against an approved dependency list.",
                            "Identify unexpected registries or unpinned versions.",
                            "Create a checklist for verifying dependencies before installation."
                        ],
                        "safety": "Use static sample manifests only. Do not install or execute suspicious packages."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is a common sign of a typosquatted package?",
                                "options": [
                                    "A package name that closely resembles a legitimate dependency",
                                    "A package with a verified and approved source",
                                    "A dependency documented in the approved manifest",
                                    "A version that matches the organisation's trusted release"
                                ],
                                "answer": "A package name that closely resembles a legitimate dependency",
                                "explanation": "Typosquatting relies on confusing a malicious package with a legitimate one."
                            },
                            {
                                "question": "Which practice helps prevent unintended dependency selection?",
                                "options": [
                                    "Use approved package sources and verify dependencies",
                                    "Install every similarly named package",
                                    "Disable dependency review",
                                    "Allow unrestricted package sources in all builds"
                                ],
                                "answer": "Use approved package sources and verify dependencies",
                                "explanation": "Trusted registries, dependency verification and controlled build settings reduce dependency risks."
                            }
                        ]
                    },

                    "prevention": [
                        "Use trusted package registries and explicitly configured sources.",
                        "Verify package names, maintainers and versions.",
                        "Pin dependencies and verify integrity where supported.",
                        "Review dependency changes before merging code.",
                        "Use automated dependency scanning and lockfiles.",
                        "Restrict build permissions and investigate unexpected packages."
                    ],

                    "conclusion": "Dependency confusion and typosquatting exploit mistakes in how software packages are named and selected. Controlled package sources, careful review and dependency verification help protect development pipelines."
                }
            }
        }
    }
}