
MOBILE_IOT_ATTACKS = {
    "id": "mobile-iot",
    "name": "Mobile and IoT Attacks",
    "description": "Security threats targeting smartphones, tablets, mobile applications, smart devices and Internet of Things (IoT) systems.",

    "subcategories": {
        "mobile_device_attacks": {
            "id": "mobile-device-attacks",
            "name": "Mobile Device Attacks",
            "description": "Threats that exploit weaknesses in mobile operating systems, device configurations, wireless connectivity or user behaviour.",

            "types": {
                "mobile_malware": {
                    "id": "mobile-malware",
                    "name": "Mobile Malware",
                    "overview": "Mobile malware is malicious software designed to compromise smartphones or tablets. Depending on its capabilities, it may steal information, display unwanted advertisements, monitor activity, misuse permissions or interfere with normal device operation.",

                    "how_it_works": [
                        "A user encounters a malicious application, attachment, download or link.",
                        "The application or file reaches the device through an unsafe source or an exploited weakness.",
                        "If the software runs successfully, it may abuse permissions or vulnerabilities to perform unauthorised actions.",
                        "Security tools and investigators examine application behaviour, permissions and relevant device evidence."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Fake Utility Application",
                            "description": "An application pretending to provide a useful service requests unnecessary permissions and attempts to collect information unrelated to its purpose."
                        },
                        {
                            "title": "A Malicious Application Update",
                            "description": "A compromised or untrustworthy application update introduces behaviour that was not present in the previously installed version."
                        }
                    ],

                    "case_study": {
                        "title": "The Application That Requested Too Much Access",
                        "scenario": "A fictional employee installs a utility application that requests access to contacts, messages and other resources unrelated to its advertised function.",
                        "findings": [
                            "The requested permissions exceeded what the application appeared to need.",
                            "The application came from an unverified source.",
                            "The organisation needed to assess whether sensitive information had been accessed."
                        ],
                        "lesson": "Application provenance, permission reviews and mobile security controls help reduce malware exposure."
                    },

                    "simulation": {
                        "title": "Investigate a Suspicious Mobile Application",
                        "scenario": "A fictional phone displays unusual pop-ups and battery consumption after an application was installed.",
                        "tasks": [
                            "Review the application's source and requested permissions.",
                            "Identify unusual symptoms that warrant investigation.",
                            "Choose appropriate containment and reporting steps.",
                            "Recommend safer installation and update practices."
                        ],
                        "expected_learning": "Recognise possible mobile malware symptoms without assuming that one symptom proves infection."
                    },

                    "practical_lab": {
                        "title": "Mobile Application Permission Review",
                        "objective": "Evaluate application permissions and identify potentially unnecessary access.",
                        "activities": [
                            "Review a fictional list of applications and permissions.",
                            "Compare each permission with the application's stated purpose.",
                            "Identify applications requiring further verification.",
                            "Prepare recommendations for removing unnecessary permissions or reporting suspicious behaviour."
                        ],
                        "safety": "Use mock application records or an authorised test device. Do not install suspected malware on a personal or production device."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which behaviour may indicate a suspicious mobile application?",
                                "options": [
                                    "Requesting permissions unrelated to its purpose",
                                    "Using only the permissions required for its function",
                                    "Receiving a verified security update",
                                    "Displaying a clear privacy policy"
                                ],
                                "answer": "Requesting permissions unrelated to its purpose",
                                "explanation": "Unnecessary permissions may indicate excessive data collection or potential misuse."
                            },
                            {
                                "question": "What is a sensible first step when an application appears malicious?",
                                "options": [
                                    "Follow the device or organisation's security response procedure",
                                    "Grant every requested permission",
                                    "Share sensitive information with the application",
                                    "Disable all device security controls"
                                ],
                                "answer": "Follow the device or organisation's security response procedure",
                                "explanation": "Appropriate containment, reporting and investigation help limit potential harm."
                            }
                        ]
                    },

                    "prevention": [
                        "Install applications from trusted distribution sources.",
                        "Review permissions before granting access.",
                        "Keep mobile operating systems and applications updated.",
                        "Use supported mobile security and device-management controls.",
                        "Remove applications that are unnecessary or untrustworthy.",
                        "Report suspicious behaviour and investigate it before assuming the device is compromised."
                    ],

                    "conclusion": "Mobile malware can affect privacy, account security and device reliability. Trusted installation sources, sensible permissions and timely updates reduce the risk."
                },

                "mobile_phishing": {
                    "id": "mobile-phishing",
                    "name": "Mobile Phishing and Smishing",
                    "overview": "Mobile phishing attempts to trick users into revealing credentials, payment details or other sensitive information through deceptive websites, applications or messages. Smishing is phishing delivered through SMS or similar text messaging services.",

                    "how_it_works": [
                        "A user receives an unexpected message or notification.",
                        "The message creates urgency or imitates a trusted organisation.",
                        "The user is encouraged to open a link, disclose information or install an application.",
                        "If the user complies, the attacker may obtain information or gain access to an account."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Fake Delivery Message",
                            "description": "A text message claims that a parcel cannot be delivered and asks the recipient to visit an unfamiliar website."
                        },
                        {
                            "title": "A Fraudulent Account Alert",
                            "description": "A message pretends to come from a bank or service provider and urges the user to confirm credentials through a supplied link."
                        }
                    ],

                    "case_study": {
                        "title": "The Urgent Banking Message",
                        "scenario": "A fictional user receives a message claiming that their bank account will be suspended unless they verify their details immediately.",
                        "findings": [
                            "The message creates urgency to discourage careful checking.",
                            "The link does not match the bank's known official domain.",
                            "The request for credentials cannot be verified through the message itself."
                        ],
                        "lesson": "Verify account alerts through an independently accessed official application or website rather than trusting message links."
                    },

                    "simulation": {
                        "title": "Identify a Suspicious Mobile Message",
                        "scenario": "Learners receive a set of fictional text messages, some legitimate and others suspicious.",
                        "tasks": [
                            "Identify urgency, suspicious links and unexpected requests.",
                            "Compare sender details with the claimed organisation.",
                            "Choose whether to report, ignore or independently verify each message.",
                            "Explain what to do if credentials were already submitted."
                        ],
                        "expected_learning": "Recognise common mobile phishing indicators and respond safely."
                    },

                    "practical_lab": {
                        "title": "Mobile Phishing Awareness Lab",
                        "objective": "Evaluate sample SMS messages and identify social engineering indicators.",
                        "activities": [
                            "Review fictional messages with altered example domains.",
                            "Identify suspicious requests and inconsistencies.",
                            "Classify each message as suspicious or requiring verification.",
                            "Create a safe reporting checklist for mobile phishing."
                        ],
                        "safety": "Use static training messages and nonfunctional example links. Never enter real credentials into training pages."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What does smishing refer to?",
                                "options": [
                                    "Phishing through SMS or text messages",
                                    "Encrypting files on a mobile device",
                                    "Updating a phone's operating system",
                                    "Backing up mobile photographs"
                                ],
                                "answer": "Phishing through SMS or text messages",
                                "explanation": "Smishing uses text messaging to deliver deceptive requests or links."
                            },
                            {
                                "question": "How should a user verify an unexpected banking alert?",
                                "options": [
                                    "Open the bank's official application or website independently",
                                    "Immediately follow the message's link",
                                    "Reply with the account password",
                                    "Forward the message to unknown contacts"
                                ],
                                "answer": "Open the bank's official application or website independently",
                                "explanation": "Independent verification avoids relying on potentially fraudulent links or contact details."
                            }
                        ]
                    },

                    "prevention": [
                        "Treat unexpected requests for credentials or payments cautiously.",
                        "Verify messages through official channels accessed independently.",
                        "Avoid opening unfamiliar links or attachments.",
                        "Enable multifactor authentication where available.",
                        "Report suspicious messages to the service provider or appropriate security team.",
                        "Change exposed credentials and report account compromise promptly."
                    ],

                    "conclusion": "Mobile phishing exploits trust and the convenience of messaging. Independent verification and careful handling of links help protect users from credential theft and fraud."
                },

                "mobile_app_permission_abuse": {
                    "id": "mobile-app-permission-abuse",
                    "name": "Mobile Application Permission Abuse",
                    "overview": "Mobile application permission abuse occurs when an application uses granted permissions in ways that exceed the user's reasonable expectations or the application's legitimate purpose. Sensitive permissions may expose location, contacts, photographs, microphones or other personal information.",

                    "how_it_works": [
                        "An application requests access to a device resource.",
                        "The user grants the permission, sometimes without reviewing its purpose.",
                        "The application accesses the resource in ways that may be excessive or unexpected.",
                        "The user or security team reviews permissions, application behaviour and available privacy controls."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unnecessary Location Access",
                            "description": "A simple application requests continuous location access even though its main function does not require location tracking."
                        },
                        {
                            "title": "Excessive Contact Permissions",
                            "description": "An application requests access to an entire contact list when its advertised function does not appear to require it."
                        }
                    ],

                    "case_study": {
                        "title": "The Unexpected Location Requests",
                        "scenario": "A fictional user notices that an application continues to request location access when the user is not actively using its main feature.",
                        "findings": [
                            "The permission settings allow more access than the user expected.",
                            "The application purpose does not clearly explain the need for continuous access.",
                            "The user needs to review the permission and available alternatives."
                        ],
                        "lesson": "Permission minimisation and transparent application behaviour help protect personal information."
                    },

                    "simulation": {
                        "title": "Review Mobile Privacy Settings",
                        "scenario": "Learners are given a fictional device with a list of applications and their permissions.",
                        "tasks": [
                            "Identify permissions that appear unnecessary.",
                            "Choose the least permissive setting that still supports the intended function.",
                            "Explain the difference between granting and denying optional access.",
                            "Recommend when an application should be removed or reported."
                        ],
                        "expected_learning": "Make informed decisions about application permissions and personal data exposure."
                    },

                    "practical_lab": {
                        "title": "Mobile Permission Audit",
                        "objective": "Assess a fictional mobile device's permission settings.",
                        "activities": [
                            "Inspect a mock application-permission table.",
                            "Match permissions with application functions.",
                            "Flag excessive access for review.",
                            "Prepare a recommended least-privilege permission profile."
                        ],
                        "safety": "Use fictional settings or your own authorised test device. Do not inspect another person's private information."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is the principle of least privilege for mobile applications?",
                                "options": [
                                    "Grant only the permissions necessary for the intended function",
                                    "Grant every permission requested by an application",
                                    "Disable every permission on every device regardless of need",
                                    "Share all personal information with installed applications"
                                ],
                                "answer": "Grant only the permissions necessary for the intended function",
                                "explanation": "Least privilege limits unnecessary access while allowing an application to perform its intended task."
                            },
                            {
                                "question": "What should a user do when an application requests an unrelated sensitive permission?",
                                "options": [
                                    "Review the request and deny it if it is not needed",
                                    "Automatically grant it",
                                    "Disable the device's screen lock",
                                    "Share the device PIN with the developer"
                                ],
                                "answer": "Review the request and deny it if it is not needed",
                                "explanation": "Reviewing permissions reduces unnecessary access to personal data and device resources."
                            }
                        ]
                    },

                    "prevention": [
                        "Review application permissions regularly.",
                        "Prefer limited or one-time access where suitable.",
                        "Check an application's purpose and developer before installation.",
                        "Remove applications that are no longer needed.",
                        "Keep the operating system updated.",
                        "Review privacy settings when an application changes its behaviour."
                    ],

                    "conclusion": "Permission abuse can expose personal information even when an application initially appears legitimate. Reviewing permissions and limiting unnecessary access helps protect mobile privacy."
                }
            }
        },

        "iot_device_attacks": {
            "id": "iot-device-attacks",
            "name": "Internet of Things (IoT) Attacks",
            "description": "Threats affecting connected devices such as smart cameras, home assistants, sensors, routers and industrial monitoring equipment.",

            "types": {
                "default_credentials_attack": {
                    "id": "default-credentials-attack",
                    "name": "Default Credential Abuse",
                    "overview": "Default credential abuse occurs when a connected device retains manufacturer-provided or otherwise predictable login credentials. If those credentials are known and the device is reachable, an unauthorised person may be able to access its settings or information.",

                    "how_it_works": [
                        "A device is installed with default or weak credentials.",
                        "The credentials are not changed or protected adequately.",
                        "An unauthorised person attempts to use those credentials against an accessible device.",
                        "The owner or administrator secures the device and reviews whether unauthorised access occurred."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Smart Camera with Unchanged Credentials",
                            "description": "A connected camera remains configured with an easily guessed or manufacturer-default password."
                        },
                        {
                            "title": "A Smart Router with a Weak Administrative Password",
                            "description": "An internet-connected router uses weak administrative credentials, potentially exposing its configuration."
                        }
                    ],

                    "case_study": {
                        "title": "The Unsecured Smart Camera",
                        "scenario": "A fictional organisation finds that several newly installed cameras still use their initial administrative credentials.",
                        "findings": [
                            "Installation did not require a credential change.",
                            "The cameras were reachable from a broader network than necessary.",
                            "The organisation lacked a complete device configuration checklist."
                        ],
                        "lesson": "Unique credentials, restricted network access and secure installation procedures are essential for connected devices."
                    },

                    "simulation": {
                        "title": "Secure a Newly Installed IoT Device",
                        "scenario": "A fictional administrator receives a new smart sensor and must prepare it for deployment.",
                        "tasks": [
                            "Identify the initial credential and setup risks.",
                            "Choose a strong, unique administrative password.",
                            "Review remote administration and network exposure settings.",
                            "Document the device's approved configuration."
                        ],
                        "expected_learning": "Understand secure onboarding and credential management for IoT devices."
                    },

                    "practical_lab": {
                        "title": "IoT Secure Configuration Checklist",
                        "objective": "Review a mock IoT device configuration for common security weaknesses.",
                        "activities": [
                            "Inspect a fictional configuration sheet.",
                            "Identify default credentials and unnecessary remote access.",
                            "Recommend unique credentials and restricted network access.",
                            "Create a secure installation checklist for future devices."
                        ],
                        "safety": "Use fictional configurations or an authorised isolated training device. Do not attempt to access devices belonging to others."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Why are default IoT credentials a security risk?",
                                "options": [
                                    "They may be widely known or easy to guess",
                                    "They automatically encrypt all device data",
                                    "They prevent every remote connection",
                                    "They cannot be changed by administrators"
                                ],
                                "answer": "They may be widely known or easy to guess",
                                "explanation": "Unchanged or predictable credentials can make unauthorised access easier."
                            },
                            {
                                "question": "What is a good practice when installing a connected device?",
                                "options": [
                                    "Set unique credentials and restrict unnecessary access",
                                    "Keep the default password permanently",
                                    "Expose every management service to the internet",
                                    "Disable all security updates"
                                ],
                                "answer": "Set unique credentials and restrict unnecessary access",
                                "explanation": "Secure configuration reduces opportunities for unauthorised access."
                            }
                        ]
                    },

                    "prevention": [
                        "Replace default credentials during initial setup.",
                        "Use unique passwords and multifactor authentication where supported.",
                        "Disable unnecessary remote administration.",
                        "Keep device firmware updated.",
                        "Place IoT devices on appropriately segmented networks.",
                        "Maintain an inventory of devices and their security settings."
                    ],

                    "conclusion": "Default credential abuse is a preventable risk in connected devices. Secure onboarding, unique credentials and restricted network access strengthen IoT security."
                },

                "iot_botnet_attack": {
                    "id": "iot-botnet-attack",
                    "name": "IoT Botnet Attacks",
                    "overview": "An IoT botnet is a group of compromised connected devices controlled by an attacker. Infected cameras, routers or other devices may be coordinated to generate unwanted traffic, participate in distributed denial-of-service attacks or perform other unauthorised activities.",

                    "how_it_works": [
                        "An attacker identifies devices with exploitable weaknesses or insecure configurations.",
                        "Some devices become compromised and communicate with attacker-controlled infrastructure.",
                        "The compromised devices receive instructions and may act together.",
                        "Defenders identify abnormal traffic, isolate affected devices and restore secure configurations."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Compromised Smart Cameras",
                            "description": "Poorly secured connected cameras are enrolled into a botnet and used to generate unwanted network traffic."
                        },
                        {
                            "title": "Infected Home Routers",
                            "description": "Routers with weak credentials or outdated firmware become part of a larger network of compromised devices."
                        }
                    ],

                    "case_study": {
                        "title": "The Smart Devices Generating Unusual Traffic",
                        "scenario": "A fictional network administrator observes that several smart devices are producing unusually high outbound traffic.",
                        "findings": [
                            "Some devices were running outdated firmware.",
                            "The devices communicated with unfamiliar external destinations.",
                            "The network lacked adequate separation between IoT equipment and important business systems."
                        ],
                        "lesson": "Firmware maintenance, network segmentation and traffic monitoring reduce botnet risk and limit the impact of compromised devices."
                    },

                    "simulation": {
                        "title": "Investigate Suspected IoT Botnet Activity",
                        "scenario": "A fictional network dashboard shows multiple connected devices generating unusual traffic at the same time.",
                        "tasks": [
                            "Identify the devices producing the abnormal traffic.",
                            "Compare activity with the normal device baseline.",
                            "Recommend isolation and evidence-preservation steps.",
                            "Propose a recovery plan that includes patching and credential changes where appropriate."
                        ],
                        "expected_learning": "Recognise possible botnet indicators and understand defensive containment."
                    },

                    "practical_lab": {
                        "title": "IoT Traffic Anomaly Analysis",
                        "objective": "Identify abnormal patterns in a fictional IoT network traffic report.",
                        "activities": [
                            "Review synthetic traffic summaries for multiple devices.",
                            "Identify unusual connection volumes and destinations.",
                            "Prioritise devices for investigation.",
                            "Write a containment and recovery recommendation."
                        ],
                        "safety": "Use synthetic logs and an isolated training environment. Do not generate denial-of-service traffic or connect to external targets."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is an IoT botnet?",
                                "options": [
                                    "A group of compromised connected devices controlled together",
                                    "A secure backup of smart-device settings",
                                    "A tool for installing approved firmware",
                                    "A list of authorised device owners"
                                ],
                                "answer": "A group of compromised connected devices controlled together",
                                "explanation": "Botnets coordinate compromised devices to perform activities chosen by an attacker."
                            },
                            {
                                "question": "Which action can help contain a suspected compromised IoT device?",
                                "options": [
                                    "Isolate it appropriately and investigate its activity",
                                    "Give it unrestricted network access",
                                    "Disable all network monitoring",
                                    "Ignore unusual outbound traffic"
                                ],
                                "answer": "Isolate it appropriately and investigate its activity",
                                "explanation": "Containment helps limit further malicious communication while the device is investigated."
                            }
                        ]
                    },

                    "prevention": [
                        "Update firmware and remove unsupported devices where possible.",
                        "Change default credentials and disable unnecessary services.",
                        "Segment IoT devices from critical systems.",
                        "Monitor unusual outbound traffic and device behaviour.",
                        "Replace devices that cannot receive necessary security updates.",
                        "Maintain an incident response plan for compromised connected devices."
                    ],

                    "conclusion": "IoT botnets turn insecure connected devices into resources for coordinated attacks. Secure configuration, timely updates and network monitoring help prevent compromise and limit its impact."
                },

                "insecure_iot_communication": {
                    "id": "insecure-iot-communication",
                    "name": "Insecure IoT Communication",
                    "overview": "Insecure IoT communication occurs when connected devices transmit information without adequate protection or fail to verify the systems with which they communicate. Depending on the design, this may expose data, allow unauthorised changes or make devices vulnerable to interception and impersonation.",

                    "how_it_works": [
                        "A device exchanges data with a mobile application, gateway, cloud service or another device.",
                        "The communication channel or endpoint verification is inadequately protected.",
                        "An attacker with suitable network access may attempt to observe or alter the communication.",
                        "Defenders review communication security and deploy appropriate encryption and authentication."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Unencrypted Sensor Connection",
                            "description": "A connected sensor sends sensitive measurements across a network without adequate transport protection."
                        },
                        {
                            "title": "Insufficient Device Authentication",
                            "description": "A smart device accepts communications without adequately verifying the identity of the sender."
                        }
                    ],

                    "case_study": {
                        "title": "The Exposed Smart Sensor",
                        "scenario": "A fictional engineering team discovers that a smart sensor transmits operational information through a channel that lacks appropriate transport protection.",
                        "findings": [
                            "The communication design did not adequately protect data in transit.",
                            "The receiving service did not consistently verify device identity.",
                            "The organisation needed to assess exposure and update the communication design."
                        ],
                        "lesson": "Encryption, certificate validation and strong device authentication help protect data exchanged by connected systems."
                    },

                    "simulation": {
                        "title": "Review an IoT Communication Design",
                        "scenario": "Learners receive a fictional architecture diagram showing smart devices, a gateway and a cloud service.",
                        "tasks": [
                            "Identify communication links that require protection.",
                            "Review where device and server identities should be verified.",
                            "Recommend appropriate encryption and authentication controls.",
                            "Explain how monitoring can help detect unexpected communications."
                        ],
                        "expected-learning": "Understand secure communication requirements for connected devices."
                    },

                    "practical_lab": {
                        "title": "IoT Communication Security Review",
                        "objective": "Evaluate a fictional device communication architecture for security weaknesses.",
                        "activities": [
                            "Review a mock network diagram and protocol inventory.",
                            "Identify connections that lack appropriate protection.",
                            "Recommend encryption and endpoint verification.",
                            "Create a short secure-communication checklist."
                        ],
                        "safety": "Use diagrams and synthetic configuration records. Do not intercept traffic on networks without explicit authorisation."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Why should IoT communications be encrypted?",
                                "options": [
                                    "To help protect information while it is transmitted",
                                    "To guarantee that every device is free from malware",
                                    "To eliminate the need for authentication",
                                    "To prevent all network traffic"
                                ],
                                "answer": "To help protect information while it is transmitted",
                                "explanation": "Encryption helps prevent unauthorised parties from reading intercepted data."
                            },
                            {
                                "question": "What does device authentication help establish?",
                                "options": [
                                    "Whether a communicating device or endpoint is trusted",
                                    "Whether a device has unlimited storage",
                                    "Whether every communication is harmless",
                                    "Whether firmware updates are unnecessary"
                                ],
                                "answer": "Whether a communicating device or endpoint is trusted",
                                "explanation": "Authentication helps verify identities before access or communication is accepted."
                            }
                        ]
                    },

                    "prevention": [
                        "Use appropriately configured encrypted communication protocols.",
                        "Verify server and device identities.",
                        "Protect device credentials and cryptographic keys.",
                        "Disable insecure or unnecessary communication services.",
                        "Apply firmware and protocol updates.",
                        "Monitor for unexpected destinations and unauthorised configuration changes."
                    ],

                    "conclusion": "Connected devices depend on trustworthy communication with other systems. Encryption, identity verification and secure configuration help protect data and device integrity."
                }
            }
        }
    }
}