
WIRELESS_ATTACKS = {
    "id": "wireless",
    "name": "Wireless Attacks",
    "description": (
        "Understand security threats affecting Wi-Fi networks, wireless "
        "authentication, Bluetooth communication, and nearby wireless devices."
    ),
    "types": {
        "wifi_network_attacks": {
            "id": "wifi-network-attacks",
            "name": "Wi-Fi Network Attacks",
            "description": (
                "Attacks that exploit weaknesses in wireless network access, "
                "configuration, encryption, or user trust."
            ),
            "types": {
                "rogue_access_point": {
                    "id": "rogue-access-point",
                    "name": "Rogue Access Point",
                    "overview": (
                        "A rogue access point is an unauthorized wireless access "
                        "point connected to or operating within an organization's "
                        "network environment. It can bypass approved security "
                        "controls and create an entry point for unauthorized access."
                    ),
                    "how_it_works": [
                        "An unauthorized access point is introduced into a wireless environment.",
                        "Users or devices connect to it, sometimes without realizing it is unapproved.",
                        "The access point may expose internal resources or bypass network controls.",
                        "Security teams identify the device and investigate its connections."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unapproved Router in an Office",
                            "content": (
                                "An employee connects a personal wireless router "
                                "to an office network to improve coverage. The device "
                                "creates an unmanaged access path that does not follow "
                                "the organization's wireless security policies."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Unknown Access Point",
                        "content": (
                            "A wireless audit identifies an access point that is "
                            "not listed in the organization's inventory. The IT team "
                            "checks its physical location, owner, network connection, "
                            "and connected devices before removing or approving it."
                        ),
                        "discussion": [
                            "Why can an unmanaged access point bypass security controls?",
                            "How can an organization maintain an accurate wireless inventory?",
                            "What should the team verify before disconnecting the device?"
                        ]
                    },
                    "simulation": {
                        "title": "Investigate an Unknown Wireless Device",
                        "scenario": (
                            "A fictional wireless monitoring dashboard reports a "
                            "new access point connected to an office network."
                        ),
                        "tasks": [
                            "Compare the device with the approved access-point inventory.",
                            "Review its location and connection details.",
                            "Decide what evidence should be collected.",
                            "Recommend safe containment and authorization checks."
                        ],
                        "expected_outcome": (
                            "The learner identifies an unapproved access point "
                            "and proposes a documented investigation."
                        )
                    },
                    "practical_lab": {
                        "title": "Wireless Inventory and Rogue AP Review",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied wireless inventory and monitoring report.",
                            "Identify access points missing from the approved inventory.",
                            "Compare device identifiers and locations.",
                            "Document verification and remediation recommendations."
                        ],
                        "expected_result": (
                            "A wireless inventory report highlighting unapproved "
                            "devices and appropriate corrective actions."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What makes an access point a rogue access point?",
                            "options": [
                                "It uses a modern encryption standard",
                                "It operates without appropriate authorization",
                                "It is listed in the approved inventory",
                                "It is managed by the organization's IT team"
                            ],
                            "answer": 1,
                            "explanation": (
                                "A rogue access point is unauthorized within the "
                                "relevant network environment."
                            )
                        },
                        {
                            "question": "What is a sensible first step after detecting an unknown access point?",
                            "options": [
                                "Ignore the alert",
                                "Immediately delete all wireless records",
                                "Verify the device against the approved inventory",
                                "Disable security monitoring"
                            ],
                            "answer": 2,
                            "explanation": (
                                "Verification helps distinguish an unauthorized "
                                "device from a legitimate but undocumented one."
                            )
                        }
                    ],
                    "prevention": [
                        "Maintain an approved wireless-device inventory.",
                        "Restrict who can connect access points to internal networks.",
                        "Use wireless intrusion detection or prevention where appropriate.",
                        "Conduct regular physical and wireless audits.",
                        "Apply network segmentation and access controls."
                    ],
                    "conclusion": (
                        "Wireless inventory management, monitoring, and controlled "
                        "deployment help prevent unauthorized access points."
                    )
                },

                "evil_twin": {
                    "id": "evil-twin",
                    "name": "Evil Twin Attack",
                    "overview": (
                        "An evil twin is a fraudulent wireless access point "
                        "designed to imitate a legitimate network. Users may "
                        "connect because its name resembles a familiar Wi-Fi "
                        "network, potentially exposing their activity or credentials."
                    ),
                    "how_it_works": [
                        "A fraudulent access point imitates the name of a trusted network.",
                        "A user connects because the network appears familiar.",
                        "The fraudulent network may observe unprotected traffic or present deceptive sign-in pages.",
                        "Network verification and secure authentication help users avoid the trap."
                    ],
                    "real_world_examples": [
                        {
                            "title": "A Fake Airport Wi-Fi Network",
                            "content": (
                                "A traveler sees two networks with similar names "
                                "at an airport. The fraudulent network imitates "
                                "the official service and requests information "
                                "through an unexpected sign-in page."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Lookalike Network",
                        "content": (
                            "Employees report a wireless network with a name "
                            "similar to the corporate network. The security team "
                            "checks the approved access-point list, verifies "
                            "network identifiers, and advises users not to connect "
                            "until the network is confirmed."
                        ),
                        "discussion": [
                            "Why is a familiar network name not sufficient proof of legitimacy?",
                            "How can staff verify an organization's wireless network?",
                            "Why should unexpected login pages be treated cautiously?"
                        ]
                    },
                    "simulation": {
                        "title": "Choose the Trusted Wi-Fi Network",
                        "scenario": (
                            "A fictional screen lists an approved network and "
                            "two lookalike networks with unfamiliar details."
                        ),
                        "tasks": [
                            "Compare the displayed networks with the approved details.",
                            "Identify warning signs of an impersonated access point.",
                            "Choose a safe connection decision.",
                            "Explain how to report the suspicious network."
                        ],
                        "expected_outcome": (
                            "The learner avoids the unverified network and reports "
                            "the potential impersonation."
                        )
                    },
                    "practical_lab": {
                        "title": "Review a Wireless Impersonation Report",
                        "mode": "defensive",
                        "steps": [
                            "Examine a supplied list of wireless network names and approved access points.",
                            "Identify suspicious lookalike names and unexpected devices.",
                            "Review the fictional incident notes for user reports.",
                            "Prepare a response and user-awareness recommendation."
                        ],
                        "expected_result": (
                            "A report describing possible evil-twin indicators "
                            "and safe user actions."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the main characteristic of an evil twin?",
                            "options": [
                                "It imitates a legitimate wireless network",
                                "It increases the battery life of a device",
                                "It automatically encrypts every application",
                                "It repairs damaged network cables"
                            ],
                            "answer": 0,
                            "explanation": (
                                "An evil twin impersonates a trusted wireless "
                                "network to encourage users to connect."
                            )
                        }
                    ],
                    "prevention": [
                        "Verify public Wi-Fi details with the legitimate provider.",
                        "Avoid connecting to lookalike or unexplained networks.",
                        "Use HTTPS and approved VPN services when appropriate.",
                        "Do not submit credentials to unexpected captive portals.",
                        "Use enterprise authentication and certificate validation where supported."
                    ],
                    "conclusion": (
                        "Checking network legitimacy and recognizing deceptive "
                        "sign-in requests helps reduce evil-twin risks."
                    )
                },

                "wifi_deauthentication": {
                    "id": "wifi-deauthentication",
                    "name": "Wi-Fi Deauthentication Attack",
                    "overview": (
                        "A deauthentication attack abuses wireless management "
                        "frames to disconnect clients from a Wi-Fi network. "
                        "Repeated disconnections can interrupt work and may "
                        "be used to encourage users to reconnect to an unsafe network."
                    ),
                    "how_it_works": [
                        "Wireless clients and access points exchange management frames.",
                        "An attacker sends forged or otherwise unauthorized disconnect messages.",
                        "Affected devices may lose their wireless connection.",
                        "Defenders examine wireless logs and use supported management-frame protections."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Repeated Wi-Fi Disconnections",
                            "content": (
                                "Staff members repeatedly lose connectivity in "
                                "one office area. The IT team checks access-point "
                                "logs, interference, device health, and management-frame "
                                "events to determine the cause."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "A Disrupted Wireless Office",
                        "content": (
                            "Several employees experience simultaneous Wi-Fi "
                            "disconnections. Investigators compare access-point "
                            "logs with wireless monitoring data, check for "
                            "interference, and assess whether suspicious "
                            "management-frame activity is occurring."
                        ),
                        "discussion": [
                            "What other issues can cause repeated disconnections?",
                            "Why should investigators correlate multiple sources of evidence?",
                            "How can protected management frames improve security?"
                        ]
                    },
                    "simulation": {
                        "title": "Investigate a Wireless Disconnection Alert",
                        "scenario": (
                            "A fictional monitoring report shows repeated client "
                            "disconnections in a limited area."
                        ),
                        "tasks": [
                            "Compare disconnection times across affected devices.",
                            "Review interference and access-point health indicators.",
                            "Identify evidence that may indicate malicious activity.",
                            "Recommend an appropriate defensive response."
                        ],
                        "expected_outcome": (
                            "The learner investigates multiple possible causes "
                            "rather than assuming every disconnection is an attack."
                        )
                    },
                    "practical_lab": {
                        "title": "Analyze Wireless Disconnection Logs",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied wireless event log.",
                            "Identify repeated disconnection patterns.",
                            "Compare events with access-point health and interference reports.",
                            "Recommend monitoring and supported management-frame protections."
                        ],
                        "expected_result": (
                            "An incident report identifying suspicious patterns "
                            "and reasonable next steps."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is a common effect of a deauthentication attack?",
                            "options": [
                                "Wireless clients may be disconnected",
                                "A computer receives unlimited storage",
                                "All wireless traffic becomes encrypted automatically",
                                "A router gains additional physical ports"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Deauthentication attacks can force wireless "
                                "clients off a network."
                            )
                        }
                    ],
                    "prevention": [
                        "Enable Protected Management Frames (802.11w) where supported.",
                        "Keep wireless infrastructure firmware updated.",
                        "Monitor repeated and unusual disconnection events.",
                        "Investigate radio interference and hardware faults as alternative causes.",
                        "Maintain a documented wireless incident-response procedure."
                    ],
                    "conclusion": (
                        "Wireless monitoring and supported management-frame "
                        "protections help reduce disruption and improve investigation."
                    )
                }
            }
        },

        "wireless_authentication_attacks": {
            "id": "wireless-authentication-attacks",
            "name": "Wireless Authentication and Encryption Attacks",
            "description": (
                "Threats involving weak wireless passwords, insecure "
                "authentication configurations, or outdated encryption."
            ),
            "types": {
                "weak_wifi_passwords": {
                    "id": "weak-wifi-passwords",
                    "name": "Weak Wi-Fi Password Attacks",
                    "overview": (
                        "Weak or reused Wi-Fi passwords can make unauthorized "
                        "network access easier. The risk depends on the wireless "
                        "security protocol, password strength, and network configuration."
                    ),
                    "how_it_works": [
                        "A wireless network uses a weak, predictable, or reused password.",
                        "An unauthorized person obtains information that permits an attempt to guess the password.",
                        "If the password and security configuration are inadequate, access may be compromised.",
                        "Strong credentials and modern authentication reduce the risk."
                    ],
                    "real_world_examples": [
                        {
                            "title": "A Shared Password That Never Changes",
                            "content": (
                                "A small office uses the same short Wi-Fi password "
                                "for years. Former visitors still know the password, "
                                "and the organization has no clear process for "
                                "revoking access."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Updating an Outdated Wireless Password",
                        "content": (
                            "A security review finds that a wireless password is "
                            "widely shared and has not been changed after staff "
                            "departures. The organization introduces stronger "
                            "credentials and a controlled access process."
                        ),
                        "discussion": [
                            "Why are short or reused passwords risky?",
                            "How does enterprise authentication differ from a shared password?",
                            "Why should access be reviewed when people leave an organization?"
                        ]
                    },
                    "simulation": {
                        "title": "Assess Wireless Password Policy",
                        "scenario": (
                            "A fictional organization uses a short shared password "
                            "and cannot identify who still has access."
                        ),
                        "tasks": [
                            "Identify weaknesses in the current policy.",
                            "Recommend stronger authentication.",
                            "Explain how former users' access should be removed.",
                            "Prepare a wireless credential policy."
                        ],
                        "expected_outcome": (
                            "The learner recommends strong credentials and "
                            "appropriate access management."
                        )
                    },
                    "practical_lab": {
                        "title": "Wireless Credential Policy Review",
                        "mode": "defensive",
                        "steps": [
                            "Review a fictional wireless-access policy.",
                            "Identify shared-password and access-revocation weaknesses.",
                            "Compare the policy with modern authentication practices.",
                            "Write prioritized recommendations."
                        ],
                        "expected_result": (
                            "A wireless authentication review with actionable improvements."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Which practice best reduces the risk of unauthorized Wi-Fi access?",
                            "options": [
                                "Use a short password shared publicly",
                                "Use strong credentials and appropriate modern authentication",
                                "Disable wireless security",
                                "Reuse the same password everywhere"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Strong credentials and appropriate authentication "
                                "make unauthorized access more difficult."
                            )
                        }
                    ],
                    "prevention": [
                        "Use modern Wi-Fi security such as WPA3 where supported.",
                        "Use long, unique passwords when a shared password is required.",
                        "Prefer enterprise authentication for managed organizations.",
                        "Review access when employees or contractors leave.",
                        "Avoid reusing wireless credentials across unrelated networks."
                    ],
                    "conclusion": (
                        "Strong authentication and controlled access management "
                        "are central to wireless network security."
                    )
                },

                "legacy_wireless_encryption": {
                    "id": "legacy-wireless-encryption",
                    "name": "Weak or Outdated Wireless Encryption",
                    "overview": (
                        "Older wireless security protocols and insecure "
                        "configurations may expose communications or permit "
                        "unauthorized network access. WEP is obsolete, and "
                        "modern networks should use supported, secure alternatives."
                    ),
                    "how_it_works": [
                        "A network relies on an outdated protocol or weak configuration.",
                        "Known weaknesses reduce the protection provided to wireless communications.",
                        "An attacker may exploit these weaknesses under suitable conditions.",
                        "Defenders migrate to modern protocols and remove legacy configurations."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Old Router Still Using WEP",
                            "content": (
                                "A routine inventory finds a legacy router "
                                "configured with WEP for compatibility with an "
                                "older device. The team replaces the device or "
                                "updates the environment to support modern security."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Retiring an Insecure Wireless Configuration",
                        "content": (
                            "A business discovers that a legacy wireless network "
                            "uses outdated encryption. The security team identifies "
                            "dependent devices, plans a controlled migration, and "
                            "verifies that the replacement configuration works."
                        ),
                        "discussion": [
                            "Why is WEP no longer considered secure?",
                            "What should be considered before retiring legacy equipment?",
                            "How can administrators verify the new configuration?"
                        ]
                    },
                    "simulation": {
                        "title": "Choose a Secure Wireless Configuration",
                        "scenario": (
                            "A fictional network inventory lists WEP, WPA2, "
                            "and WPA3 configurations across several devices."
                        ),
                        "tasks": [
                            "Identify obsolete configurations.",
                            "Recommend supported modern security options.",
                            "Plan how incompatible devices will be handled.",
                            "Define post-migration verification steps."
                        ],
                        "expected_outcome": (
                            "The learner prioritizes the removal of obsolete "
                            "encryption while maintaining a controlled migration."
                        )
                    },
                    "practical_lab": {
                        "title": "Wireless Configuration Audit",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied wireless configuration inventory.",
                            "Identify obsolete protocols and weak settings.",
                            "Check which devices require migration.",
                            "Produce a secure configuration recommendation."
                        ],
                        "expected_result": (
                            "A configuration audit identifying insecure settings "
                            "and a migration plan."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Which wireless security protocol is obsolete and should not be used?",
                            "options": [
                                "WEP",
                                "WPA3",
                                "A properly configured modern enterprise solution",
                                "A supported secure configuration"
                            ],
                            "answer": 0,
                            "explanation": (
                                "WEP has serious known weaknesses and should be retired."
                            )
                        }
                    ],
                    "prevention": [
                        "Retire WEP and other obsolete wireless security configurations.",
                        "Use WPA3 where supported or an appropriately configured WPA2 solution when necessary.",
                        "Update router and access-point firmware.",
                        "Inventory devices that depend on legacy protocols.",
                        "Verify security settings after migration."
                    ],
                    "conclusion": (
                        "Modern encryption and planned retirement of legacy "
                        "equipment help protect wireless communications."
                    )
                }
            }
        },

        "bluetooth_and_nearby_device_attacks": {
            "id": "bluetooth-and-nearby-device-attacks",
            "name": "Bluetooth and Nearby Device Attacks",
            "description": (
                "Threats involving Bluetooth discovery, pairing, and wireless "
                "communication between nearby devices."
            ),
            "types": {
                "bluetooth_pairing_abuse": {
                    "id": "bluetooth-pairing-abuse",
                    "name": "Bluetooth Pairing Abuse",
                    "overview": (
                        "Bluetooth pairing abuse occurs when an attacker takes "
                        "advantage of weak pairing practices, unnecessary "
                        "discoverability, or vulnerable device implementations "
                        "to attempt unauthorized connections."
                    ),
                    "how_it_works": [
                        "A Bluetooth device is left discoverable or accepts unexpected pairing requests.",
                        "A nearby device attempts to establish an unauthorized connection.",
                        "If pairing or device security is inadequate, access may be exposed.",
                        "Users and administrators restrict pairing and keep devices updated."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Unexpected Pairing Requests",
                            "content": (
                                "An employee receives repeated pairing prompts "
                                "in a shared office. The employee rejects unknown "
                                "requests and reports the behavior to IT."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "An Unfamiliar Device Appears",
                        "content": (
                            "A staff member notices a device paired with a "
                            "workstation without a clear business reason. The "
                            "support team reviews paired-device history, removes "
                            "unrecognized devices, and checks relevant security logs."
                        ),
                        "discussion": [
                            "Why should unexpected pairing requests be rejected?",
                            "When should discoverability be enabled?",
                            "Why is reviewing paired devices useful?"
                        ]
                    },
                    "simulation": {
                        "title": "Handle an Unexpected Bluetooth Request",
                        "scenario": (
                            "A laptop receives a pairing request from an "
                            "unrecognized nearby device."
                        ),
                        "tasks": [
                            "Choose whether to accept or reject the request.",
                            "Identify the appropriate reporting process.",
                            "Review the device's discoverability settings.",
                            "Recommend secure pairing practices."
                        ],
                        "expected_outcome": (
                            "The learner rejects an unverified request and "
                            "follows safe device-management practices."
                        )
                    },
                    "practical_lab": {
                        "title": "Review Bluetooth Device Security",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied inventory of paired devices.",
                            "Identify unfamiliar or unnecessary pairings.",
                            "Check discoverability and update policies.",
                            "Document actions for securing the devices."
                        ],
                        "expected_result": (
                            "A Bluetooth security checklist and remediation report."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What should you do with an unexpected Bluetooth pairing request?",
                            "options": [
                                "Accept it immediately",
                                "Reject it unless its legitimacy is verified",
                                "Share your device password",
                                "Disable all security updates"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Unexpected pairing requests should be verified "
                                "before a connection is accepted."
                            )
                        }
                    ],
                    "prevention": [
                        "Disable Bluetooth when it is not needed.",
                        "Limit discoverability to the period when pairing is required.",
                        "Reject unexpected pairing requests.",
                        "Remove unrecognized paired devices.",
                        "Install manufacturer security updates."
                    ],
                    "conclusion": (
                        "Careful pairing, limited discoverability, and updated "
                        "devices reduce the risk of Bluetooth misuse."
                    )
                },

                "bluetooth_information_exposure": {
                    "id": "bluetooth-information-exposure",
                    "name": "Bluetooth Information Exposure",
                    "overview": (
                        "Bluetooth information exposure can occur when devices "
                        "broadcast unnecessary identifying information or run "
                        "vulnerable software. Depending on the device and its "
                        "configuration, this information may help an observer "
                        "identify devices or discover potential weaknesses."
                    ),
                    "how_it_works": [
                        "A Bluetooth device advertises or exposes information during discovery or communication.",
                        "An observer collects available device details.",
                        "Excessive exposure may reveal device type or other identifying metadata.",
                        "Defenders reduce unnecessary broadcasts and maintain updated software."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Devices Revealing Unnecessary Details",
                            "content": (
                                "A workplace assessment finds that some devices "
                                "remain discoverable throughout the day. The "
                                "organization reviews whether constant discovery "
                                "is necessary and updates device policies."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Reviewing Wireless Privacy Settings",
                        "content": (
                            "A privacy review identifies several devices "
                            "broadcasting unnecessary information. The team "
                            "checks manufacturer guidance, reduces avoidable "
                            "exposure, and explains safe settings to employees."
                        ),
                        "discussion": [
                            "What information can wireless discovery reveal?",
                            "Why should only necessary information be exposed?",
                            "How can organizations balance convenience and privacy?"
                        ]
                    },
                    "simulation": {
                        "title": "Identify Unnecessary Device Exposure",
                        "scenario": (
                            "A fictional inventory lists devices that advertise "
                            "more information than required for normal operation."
                        ),
                        "tasks": [
                            "Identify unnecessary discoverability.",
                            "Determine which settings can safely be restricted.",
                            "Recommend an update and review process.",
                            "Explain the privacy benefit of minimizing exposure."
                        ],
                        "expected_outcome": (
                            "The learner recommends reducing unnecessary wireless "
                            "exposure without disrupting required device functions."
                        )
                    },
                    "practical_lab": {
                        "title": "Bluetooth Privacy Settings Review",
                        "mode": "defensive",
                        "steps": [
                            "Review a sample device inventory and privacy checklist.",
                            "Identify devices with unnecessary discoverability.",
                            "Check whether firmware and operating systems are current.",
                            "Write practical recommendations for reducing exposure."
                        ],
                        "expected_result": (
                            "A device-privacy review with prioritized recommendations."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Why should Bluetooth discoverability be limited when it is not needed?",
                            "options": [
                                "It can reduce unnecessary wireless exposure",
                                "It guarantees that every device is invulnerable",
                                "It automatically updates all software",
                                "It increases the device's storage capacity"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Limiting unnecessary discovery can reduce "
                                "identifying information exposed to nearby observers."
                            )
                        }
                    ],
                    "prevention": [
                        "Disable unnecessary Bluetooth discovery and broadcasting.",
                        "Remove unused Bluetooth services and pairings.",
                        "Apply operating-system and firmware updates.",
                        "Review privacy settings on laptops, phones, and accessories.",
                        "Follow manufacturer guidance for secure wireless operation."
                    ],
                    "conclusion": (
                        "Minimizing wireless exposure and maintaining updated "
                        "devices improve Bluetooth privacy and security."
                    )
                }
            }
        }
    }
}