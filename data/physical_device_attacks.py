
PHYSICAL_DEVICE_ATTACKS = {
    "id": "physical-device",
    "name": "Physical and Device Attacks",
    "description": "Attacks that exploit physical access, device weaknesses, removable media or hardware interfaces to compromise systems, information or availability.",

    "subcategories": {
        "physical_access_attacks": {
            "id": "physical-access-attacks",
            "name": "Physical Access Attacks",
            "description": "Attacks that rely on unauthorised physical access to devices, facilities or protected equipment.",

            "types": {
                "unauthorised_physical_access": {
                    "id": "unauthorised-physical-access",
                    "name": "Unauthorised Physical Access",
                    "overview": "Unauthorised physical access occurs when someone enters a restricted area or reaches a device without permission. Depending on the environment, this can expose sensitive information, allow device tampering or provide access to systems that are otherwise well protected by software controls.",

                    "how_it_works": [
                        "An attacker identifies a location containing valuable devices or information.",
                        "Physical security controls are bypassed, misused or found to be inadequate.",
                        "The attacker reaches equipment, unattended devices or restricted information.",
                        "The incident is investigated using access records, available camera footage and device logs."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Unattended Office Computer",
                            "description": "A visitor reaches an unattended workstation in an area where visitor access is not properly supervised."
                        },
                        {
                            "title": "An Unsecured Equipment Room",
                            "description": "A server or networking room is left unlocked, allowing an unauthorised person to approach critical equipment."
                        }
                    ],

                    "case_study": {
                        "title": "The Unlocked Network Room",
                        "scenario": "A fictional organisation discovers that an unauthorised visitor entered a room containing networking equipment during normal office hours.",
                        "findings": [
                            "The room was not consistently kept locked.",
                            "Visitor movements were not recorded clearly.",
                            "The organisation could not immediately establish whether equipment had been accessed."
                        ],
                        "lesson": "Physical security must be managed alongside account security, network monitoring and other technical safeguards."
                    },

                    "simulation": {
                        "title": "Investigate a Physical Security Incident",
                        "scenario": "A fictional security officer reports that a restricted equipment room was found open after a visitor's appointment.",
                        "tasks": [
                            "List the equipment and information potentially exposed.",
                            "Identify which access records should be reviewed.",
                            "Decide whether equipment inspection or credential review is appropriate.",
                            "Recommend changes to visitor management and room security."
                        ],
                        "expected_learning": "Recognise physical access risks and develop a proportionate incident response."
                    },

                    "practical_lab": {
                        "title": "Physical Security Risk Assessment",
                        "objective": "Identify weaknesses in a fictional office or computer-room layout.",
                        "activities": [
                            "Review a sample floor plan with restricted and public areas.",
                            "Identify unattended workstations and unsecured equipment.",
                            "Assess visitor entry, supervision and access logging.",
                            "Prepare a prioritised list of physical security improvements."
                        ],
                        "safety": "Use fictional floor plans or an authorised training environment. Do not attempt to enter restricted areas."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Why is physical security important for cybersecurity?",
                                "options": [
                                    "Physical access can expose devices, data and internal systems",
                                    "Physical security replaces all software security",
                                    "Locked rooms prevent every cyberattack",
                                    "Physical access has no effect on information security"
                                ],
                                "answer": "Physical access can expose devices, data and internal systems",
                                "explanation": "An attacker who reaches a device may be able to tamper with it or access information."
                            },
                            {
                                "question": "Which measure helps protect a server room?",
                                "options": [
                                    "Restricted entry with access logging",
                                    "Leaving the door open during office hours",
                                    "Sharing access cards with visitors",
                                    "Disabling visitor records"
                                ],
                                "answer": "Restricted entry with access logging",
                                "explanation": "Controlled access and reliable records help prevent unauthorised entry and support investigations."
                            }
                        ]
                    },

                    "prevention": [
                        "Use locked rooms and access controls for sensitive equipment.",
                        "Issue visitor badges and supervise visitors in restricted areas.",
                        "Keep workstations locked when unattended.",
                        "Maintain physical entry records where appropriate.",
                        "Inspect equipment after suspected unauthorised access.",
                        "Combine physical controls with technical monitoring and incident reporting."
                    ],

                    "conclusion": "Physical access can undermine otherwise strong technical protections. Secure facilities, supervised visitors and clear access procedures reduce the likelihood of unauthorised device access."
                },

                "shoulder_surfing": {
                    "id": "shoulder-surfing",
                    "name": "Shoulder Surfing",
                    "overview": "Shoulder surfing is the observation of another person's screen, keyboard or other input to obtain sensitive information. It can occur in public places, shared offices or any environment where private information is visible to people who should not see it.",

                    "how_it_works": [
                        "A user enters a password, PIN or other sensitive information.",
                        "Another person observes the input or reads information displayed on the screen.",
                        "The observer may remember or record the information.",
                        "The exposed information may be misused if additional protections do not prevent access."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A PIN Entered in Public",
                            "description": "Someone watches a person enter a PIN at a payment terminal or access-controlled entry point."
                        },
                        {
                            "title": "Confidential Information on a Laptop",
                            "description": "A person seated nearby can read sensitive messages or documents displayed on an employee's laptop."
                        }
                    ],

                    "case_study": {
                        "title": "The Shared Workspace Disclosure",
                        "scenario": "An employee working in a crowded public area notices that people nearby can easily see the screen while confidential records are open.",
                        "findings": [
                            "The screen was positioned toward a busy walkway.",
                            "Sensitive information remained visible longer than necessary.",
                            "The employee had not considered the surrounding environment."
                        ],
                        "lesson": "Screen positioning, privacy filters and awareness of surroundings can reduce visual information exposure."
                    },

                    "simulation": {
                        "title": "Spot the Shoulder-Surfing Risk",
                        "scenario": "A fictional illustration shows a person entering credentials while another person can see the keyboard and screen.",
                        "tasks": [
                            "Identify which information is exposed.",
                            "Suggest a safer screen position.",
                            "Choose suitable privacy and authentication controls.",
                            "Explain what to do if sensitive credentials may have been observed."
                        ],
                        "expected_learning": "Recognise visual information disclosure and apply practical privacy measures."
                    },

                    "practical_lab": {
                        "title": "Visual Privacy Assessment",
                        "objective": "Evaluate how screen position and workspace design affect information privacy.",
                        "activities": [
                            "Review fictional desk layouts and screen positions.",
                            "Identify where unauthorised observers could see sensitive content.",
                            "Recommend privacy filters or alternative seating arrangements.",
                            "Create a short checklist for working in public places."
                        ],
                        "safety": "Use diagrams and dummy credentials only. Do not observe or record other people's private information."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is shoulder surfing?",
                                "options": [
                                    "Observing someone's screen or input to obtain information",
                                    "Encrypting a file before sharing it",
                                    "Installing an approved software update",
                                    "Creating a secure backup"
                                ],
                                "answer": "Observing someone's screen or input to obtain information",
                                "explanation": "Shoulder surfing relies on visually observing information rather than necessarily compromising a computer."
                            },
                            {
                                "question": "Which action reduces shoulder-surfing risk?",
                                "options": [
                                    "Use a privacy filter and position the screen carefully",
                                    "Display passwords in large text",
                                    "Leave confidential documents open in public",
                                    "Share PINs with nearby people"
                                ],
                                "answer": "Use a privacy filter and position the screen carefully",
                                "explanation": "Reducing visibility makes it harder for unauthorised people to observe sensitive information."
                            }
                        ]
                    },

                    "prevention": [
                        "Position screens away from public walkways.",
                        "Use privacy filters when working in exposed locations.",
                        "Shield PIN entry and other sensitive input.",
                        "Lock screens when stepping away.",
                        "Avoid opening confidential information in unsuitable public environments.",
                        "Change exposed credentials and report suspected compromise."
                    ],

                    "conclusion": "Shoulder surfing exploits the visibility of information rather than a software vulnerability. Awareness, careful screen placement and privacy controls help protect sensitive information."
                },

                "device_tampering": {
                    "id": "device-tampering",
                    "name": "Device Tampering",
                    "overview": "Device tampering involves unauthorised physical changes to a computer, peripheral, network device or other electronic equipment. Tampering can affect confidentiality, integrity or availability and may be difficult to detect without appropriate inspection and monitoring.",

                    "how_it_works": [
                        "An attacker gains physical access to a device or its connections.",
                        "The device, attached hardware or configuration is altered without authorisation.",
                        "The change may expose information, disrupt operation or undermine normal security controls.",
                        "The organisation isolates the equipment and investigates its condition and history."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Unapproved Peripheral",
                            "description": "An unknown device is connected to a workstation without the owner's or administrator's approval."
                        },
                        {
                            "title": "Altered Network Equipment",
                            "description": "A network device is physically changed without an authorised maintenance record, creating uncertainty about its integrity."
                        }
                    ],

                    "case_study": {
                        "title": "The Unrecognised Device Connection",
                        "scenario": "An IT team discovers an unfamiliar peripheral connected to a workstation in a restricted office.",
                        "findings": [
                            "The connection did not match the workstation's asset record.",
                            "No approved maintenance request explained the device.",
                            "The team needed to determine whether the workstation or its data had been affected."
                        ],
                        "lesson": "Asset inventories, controlled equipment access and authorised change records help identify suspicious physical changes."
                    },

                    "simulation": {
                        "title": "Assess Suspected Device Tampering",
                        "scenario": "A fictional workstation is found with an unfamiliar attachment and no matching equipment record.",
                        "tasks": [
                            "Document the device's condition and the discovery time.",
                            "Determine whether the workstation should be isolated.",
                            "Identify relevant asset, access and maintenance records.",
                            "Recommend safe inspection and restoration steps."
                        ],
                        "expected_learning": "Understand evidence preservation and the safe handling of potentially tampered equipment."
                    },

                    "practical_lab": {
                        "title": "Hardware Asset Verification",
                        "objective": "Identify discrepancies between a fictional hardware inventory and equipment found during an inspection.",
                        "activities": [
                            "Compare sample asset tags with an equipment register.",
                            "Identify unknown peripherals and undocumented changes.",
                            "Review mock maintenance records.",
                            "Prepare a discrepancy report with recommended next steps."
                        ],
                        "safety": "Use mock equipment records or authorised training hardware. Do not open, modify or tamper with production devices."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is device tampering?",
                                "options": [
                                    "Unauthorised physical alteration of a device or its connections",
                                    "Routine approved maintenance",
                                    "Creating a backup of an authorised file",
                                    "Applying a verified security patch"
                                ],
                                "answer": "Unauthorised physical alteration of a device or its connections",
                                "explanation": "Device tampering involves changes made without appropriate permission."
                            },
                            {
                                "question": "What is an appropriate response to a suspicious hardware attachment?",
                                "options": [
                                    "Document it and follow the authorised investigation process",
                                    "Ignore it because it is physically connected",
                                    "Connect it to additional computers to test it",
                                    "Delete all asset records"
                                ],
                                "answer": "Document it and follow the authorised investigation process",
                                "explanation": "Documentation and controlled investigation help preserve evidence and avoid spreading a potential risk."
                            }
                        ]
                    },

                    "prevention": [
                        "Maintain an accurate hardware and peripheral inventory.",
                        "Restrict access to sensitive equipment.",
                        "Require approval and records for maintenance and configuration changes.",
                        "Inspect equipment for unexplained alterations.",
                        "Use appropriate port controls and device-management policies.",
                        "Document and investigate suspicious hardware findings."
                    ],

                    "conclusion": "Physical device tampering can undermine the integrity of systems and information. Equipment inventories, controlled access and documented maintenance make unauthorised changes easier to detect."
                }
            }
        },

        "removable_media_and_hardware": {
            "id": "removable-media-and-hardware",
            "name": "Removable Media and Hardware Threats",
            "description": "Threats involving removable storage, untrusted peripherals and exposed device interfaces.",

            "types": {
                "malicious_usb_device": {
                    "id": "malicious-usb-device",
                    "name": "Malicious USB Device",
                    "overview": "A malicious USB device is a removable device designed or configured to perform unauthorised actions when connected to a computer. Not every unfamiliar USB device is malicious, but untrusted devices can create risks through storage contents, device impersonation or unexpected hardware behaviour.",

                    "how_it_works": [
                        "A user connects an unknown or untrusted USB device.",
                        "The device may present files or behave in an unexpected way, depending on its design.",
                        "If unsafe content is opened or the device is trusted without verification, the computer may be exposed to risk.",
                        "The device is handled through the organisation's security reporting and inspection process."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Unknown USB Drive",
                            "description": "An employee finds a USB drive in a shared area and connects it to a work computer to identify its owner."
                        },
                        {
                            "title": "An Unapproved USB Peripheral",
                            "description": "A user connects an unknown peripheral that has not been approved for use on the organisation's computers."
                        }
                    ],

                    "case_study": {
                        "title": "The USB Drive Found at Reception",
                        "scenario": "A staff member finds a removable drive near the reception desk and reports it after remembering the organisation's device policy.",
                        "findings": [
                            "The owner and origin of the drive were unknown.",
                            "Connecting it to an ordinary workstation could have exposed that system.",
                            "The organisation needed a safe process for handling found media."
                        ],
                        "lesson": "Unknown removable media should never be treated as trustworthy simply because it looks ordinary."
                    },

                    "simulation": {
                        "title": "Respond to an Unknown USB Device",
                        "scenario": "A fictional employee asks whether a USB drive found in a meeting room should be connected to a laptop.",
                        "tasks": [
                            "Choose the safest immediate response.",
                            "Identify the correct reporting channel.",
                            "Explain why ordinary computers should not be used to inspect unknown devices.",
                            "Recommend controls for removable media."
                        ],
                        "expected_learning": "Recognise removable-media risks and follow safe handling procedures."
                    },

                    "practical_lab": {
                        "title": "Removable Media Policy Review",
                        "objective": "Assess a fictional organisation's removable-media rules and identify gaps.",
                        "activities": [
                            "Review a mock device-use policy.",
                            "Identify missing approval and reporting procedures.",
                            "Recommend restrictions and appropriate scanning controls.",
                            "Write a short response checklist for unknown media."
                        ],
                        "safety": "Do not connect unknown devices to personal or production computers. Use written scenarios or approved, inert training devices."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What should an employee do with an unknown USB drive found at work?",
                                "options": [
                                    "Report it and follow the organisation's safe-handling procedure",
                                    "Connect it to a work computer immediately",
                                    "Open every file to identify the owner",
                                    "Pass it to another employee to test"
                                ],
                                "answer": "Report it and follow the organisation's safe-handling procedure",
                                "explanation": "Unknown removable media should be handled through an approved process rather than trusted automatically."
                            },
                            {
                                "question": "Why can an unfamiliar USB device be risky?",
                                "options": [
                                    "Its contents or device behaviour may be untrusted",
                                    "Every USB device is guaranteed to be malicious",
                                    "USB devices cannot exchange information",
                                    "A USB connection always disables security controls"
                                ],
                                "answer": "Its contents or device behaviour may be untrusted",
                                "explanation": "The risk depends on the device and how it is used; unknown devices should not be trusted without proper checks."
                            }
                        ]
                    },

                    "prevention": [
                        "Use only authorised removable media.",
                        "Report unknown devices rather than connecting them.",
                        "Apply endpoint controls for removable storage and peripherals.",
                        "Scan approved media using authorised security tools.",
                        "Encrypt sensitive data stored on permitted removable devices.",
                        "Maintain clear procedures for found or suspicious hardware."
                    ],

                    "conclusion": "Untrusted USB devices and peripherals can introduce avoidable security risks. Approved-device policies and safe handling procedures help protect endpoints and organisational information."
                },

                "data_theft_from_lost_device": {
                    "id": "data-theft-from-lost-device",
                    "name": "Data Exposure from Lost or Stolen Devices",
                    "overview": "Lost or stolen laptops, phones, tablets and removable drives can expose sensitive information when the devices contain accessible data or lack appropriate security protections. The impact depends on the data stored, device configuration and the controls available to the organisation.",

                    "how_it_works": [
                        "A device containing organisational or personal information is lost or stolen.",
                        "The device may be accessed if authentication and encryption protections are insufficient.",
                        "Information or active sessions may be exposed, depending on the device's security state.",
                        "The owner or organisation reports the loss and activates appropriate containment measures."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Lost Work Laptop",
                            "description": "An employee leaves a laptop containing work documents in a public place and cannot recover it."
                        },
                        {
                            "title": "A Stolen Unlocked Phone",
                            "description": "A phone containing active work sessions is stolen while unlocked, potentially exposing email or business applications."
                        }
                    ],

                    "case_study": {
                        "title": "The Missing Travel Laptop",
                        "scenario": "A travelling employee reports that a work laptop containing confidential documents is missing.",
                        "findings": [
                            "The device contained files that required protection.",
                            "The incident response team needed to determine whether encryption was enabled.",
                            "The organisation had to consider account sessions, data exposure and reporting obligations."
                        ],
                        "lesson": "Device encryption, screen locks and a tested lost-device response process can reduce the consequences of device loss."
                    },

                    "simulation": {
                        "title": "Lost Device Response Exercise",
                        "scenario": "A fictional employee reports a missing work phone with access to email and internal applications.",
                        "tasks": [
                            "Identify which team should be notified.",
                            "Determine whether sessions or credentials should be revoked.",
                            "Consider whether remote locking or wiping is appropriate under policy.",
                            "Assess what information may have been exposed and document the incident."
                        ],
                        "expected_learning": "Understand timely containment and exposure assessment following device loss."
                    },

                    "practical_lab": {
                        "title": "Lost Device Response Planning",
                        "objective": "Create a safe response checklist for missing organisational devices.",
                        "activities": [
                            "Review a fictional device inventory and security configuration.",
                            "Identify encryption, screen-lock and management controls.",
                            "Map the reporting and containment steps.",
                            "Draft a checklist for device recovery, account protection and incident documentation."
                        ],
                        "safety": "Use fictional cases and test-device settings only. Do not attempt to access another person's lost or stolen device."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which control helps protect information on a lost laptop?",
                                "options": [
                                    "Full-disk encryption combined with strong authentication",
                                    "Keeping the laptop permanently unlocked",
                                    "Saving all passwords in a plain-text file",
                                    "Disabling device security updates"
                                ],
                                "answer": "Full-disk encryption combined with strong authentication",
                                "explanation": "Encryption helps protect stored information if a device is lost, while authentication restricts access."
                            },
                            {
                                "question": "What is an appropriate first response to a missing work device?",
                                "options": [
                                    "Report it promptly and follow the organisation's response procedure",
                                    "Wait several weeks before notifying anyone",
                                    "Publish account credentials online",
                                    "Ignore the incident if the device looks ordinary"
                                ],
                                "answer": "Report it promptly and follow the organisation's response procedure",
                                "explanation": "Early reporting allows the organisation to secure accounts, assess exposure and take appropriate containment measures."
                            }
                        ]
                    },

                    "prevention": [
                        "Encrypt laptops, phones and removable storage containing sensitive data.",
                        "Use strong screen locks and multifactor authentication.",
                        "Enable approved device-management and remote-lock capabilities.",
                        "Avoid storing unnecessary sensitive information locally.",
                        "Report missing devices immediately.",
                        "Review sessions and credentials that may have been exposed."
                    ],

                    "conclusion": "A lost or stolen device can become a data security incident even when the device itself is never recovered. Encryption, secure authentication and prompt reporting reduce the potential impact."
                }
            }
        }
    }
}