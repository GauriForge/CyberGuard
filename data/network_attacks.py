
NETWORK_ATTACKS = {
    "id": "network",
    "name": "Network Attacks",
    "description": (
        "Explore attacks against network infrastructure, communication "
        "protocols, network services, and connected systems, together "
        "with their detection and prevention."
    ),
    "types": {
        "traffic_interception": {
            "id": "traffic-interception",
            "name": "Traffic Interception and Manipulation",
            "description": (
                "Attacks that intercept, observe, or manipulate network "
                "communications between devices."
            ),
            "types": {
                "man_in_the_middle": {
                    "id": "man-in-the-middle",
                    "name": "Man-in-the-Middle (MITM) Attack",
                    "overview": (
                        "A man-in-the-middle attack occurs when an unauthorized "
                        "party positions itself between communicating endpoints "
                        "to observe or alter information. Weak encryption, "
                        "untrusted networks, and certificate warnings can "
                        "increase the risk."
                    ),
                    "how_it_works": [
                        "A victim connects to a network or service.",
                        "An attacker gains an unauthorized position in the "
                        "communication path.",
                        "If protections are insufficient, the attacker may "
                        "observe or manipulate transmitted information.",
                        "Strong encryption and certificate validation can "
                        "prevent or limit the attack."
                    ],
                    "real_world_examples": [
                        {
                            "title": "A Risky Public Wi-Fi Connection",
                            "content": (
                                "A traveler connects to an untrusted wireless "
                                "network and encounters a certificate warning "
                                "while accessing an account. Ignoring the warning "
                                "could expose the traveler to interception or "
                                "an impersonated service."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Suspicious Traffic on a Public Network",
                        "content": (
                            "Employees report unexpected certificate warnings "
                            "while using a public network. The security team "
                            "advises them to stop using the affected connection, "
                            "verify the service through a trusted network, and "
                            "investigate the network and affected accounts."
                        ),
                        "discussion": [
                            "Why should certificate warnings never be ignored?",
                            "How does HTTPS help protect communications?",
                            "What should an employee do before accessing sensitive accounts?"
                        ]
                    },
                    "simulation": {
                        "title": "Identify a Possible MITM Attack",
                        "scenario": (
                            "A user connects to public Wi-Fi and receives an "
                            "unexpected certificate warning on a familiar website."
                        ),
                        "tasks": [
                            "Identify the warning as a possible security indicator.",
                            "Choose whether to continue or stop the connection.",
                            "Recommend a safer way to access the service.",
                            "Explain how encryption and certificate validation help."
                        ],
                        "expected_outcome": (
                            "The learner stops the suspicious connection and "
                            "uses a trusted network and verified service."
                        )
                    },
                    "practical_lab": {
                        "title": "Analyze Network and Certificate Alerts",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied set of fictional network-security logs.",
                            "Identify certificate errors and unexpected connection changes.",
                            "Separate normal events from suspicious indicators.",
                            "Write recommendations for secure communication."
                        ],
                        "expected_result": (
                            "A short report identifying possible interception "
                            "indicators and appropriate defensive actions."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What characterizes a man-in-the-middle attack?",
                            "options": [
                                "An attacker intercepts or manipulates communication",
                                "A computer runs out of storage",
                                "A user forgets a password",
                                "A server performs a normal backup"
                            ],
                            "answer": 0,
                            "explanation": (
                                "The attacker attempts to position themselves "
                                "between communicating parties."
                            )
                        },
                        {
                            "question": "What should you do when a trusted website shows an unexpected certificate warning?",
                            "options": [
                                "Ignore it",
                                "Enter credentials immediately",
                                "Stop and verify the connection through a trusted route",
                                "Disable all browser security"
                            ],
                            "answer": 2,
                            "explanation": (
                                "Unexpected certificate warnings can indicate "
                                "a connection or identity problem."
                            )
                        }
                    ],
                    "prevention": [
                        "Use HTTPS and valid certificate verification.",
                        "Avoid sensitive transactions on untrusted networks.",
                        "Use an organization-approved VPN when appropriate.",
                        "Never bypass unexplained certificate warnings.",
                        "Keep network devices and client software updated."
                    ],
                    "conclusion": (
                        "Secure communication depends on encryption, verified "
                        "server identity, and careful handling of network warnings."
                    )
                },

                "packet_sniffing": {
                    "id": "packet-sniffing",
                    "name": "Packet Sniffing",
                    "overview": (
                        "Packet sniffing is the capture and inspection of network "
                        "traffic. Administrators use it for troubleshooting and "
                        "security monitoring, but unauthorized capture can expose "
                        "sensitive information when traffic is inadequately protected."
                    ),
                    "how_it_works": [
                        "A packet-capture tool observes traffic available to a device.",
                        "The captured packets are examined for protocol and connection details.",
                        "Unencrypted or improperly protected information may be exposed.",
                        "Defenders analyze captures to troubleshoot problems or investigate incidents."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Sensitive Information on an Unsecured Network",
                            "content": (
                                "A security review finds that an internal service "
                                "transmits sensitive information without adequate "
                                "encryption. The organization secures the service "
                                "and reviews whether information may have been exposed."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Unexpected Exposure in a Packet Capture",
                        "content": (
                            "During an authorized network audit, an analyst finds "
                            "sensitive information in a traffic capture. Access to "
                            "the capture is restricted, the service is investigated, "
                            "and encrypted communication is enforced."
                        ),
                        "discussion": [
                            "Why can packet captures themselves contain sensitive data?",
                            "How does encryption reduce exposure?",
                            "Who should be allowed to access captured traffic?"
                        ]
                    },
                    "simulation": {
                        "title": "Review a Sample Packet Capture",
                        "scenario": (
                            "A fictional packet-capture report contains normal "
                            "encrypted connections and a service using an insecure protocol."
                        ),
                        "tasks": [
                            "Identify the insecure protocol.",
                            "Determine what information the capture reveals.",
                            "Recommend a safer protocol.",
                            "Explain how capture files should be protected."
                        ],
                        "expected_outcome": (
                            "The learner recognizes insecure communication and "
                            "recommends encryption and restricted access to evidence."
                        )
                    },
                    "practical_lab": {
                        "title": "Packet Capture Analysis",
                        "mode": "defensive",
                        "steps": [
                            "Use a provided, sanitized packet-capture file or sample report.",
                            "Identify common protocols and connection metadata.",
                            "Flag unencrypted services and unusual traffic patterns.",
                            "Document findings without collecting other people's traffic."
                        ],
                        "expected_result": (
                            "A network-analysis report with protocol observations "
                            "and remediation recommendations."
                        )
                    },
                    "assessment": [
                        {
                            "question": "When is packet sniffing a legitimate activity?",
                            "options": [
                                "When used without permission on any network",
                                "When performed with proper authorization for troubleshooting or security",
                                "When it is used to steal credentials",
                                "When it bypasses organizational policies"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Packet capture is a legitimate diagnostic and "
                                "security technique when properly authorized."
                            )
                        }
                    ],
                    "prevention": [
                        "Encrypt sensitive network communications.",
                        "Restrict packet-capture permissions.",
                        "Protect captured files because they may contain sensitive metadata.",
                        "Monitor for unauthorized traffic-capture activity.",
                        "Use secure protocols instead of plaintext alternatives."
                    ],
                    "conclusion": (
                        "Packet analysis helps defenders understand network "
                        "behavior, but authorization, encryption, and evidence "
                        "protection are essential."
                    )
                },

                "arp_spoofing": {
                    "id": "arp-spoofing",
                    "name": "ARP Spoofing",
                    "overview": (
                        "ARP spoofing occurs when a device sends forged Address "
                        "Resolution Protocol messages on a local network. This "
                        "can associate an attacker's hardware address with another "
                        "device's IP address and redirect local traffic."
                    ),
                    "how_it_works": [
                        "Devices use ARP to map local IPv4 addresses to hardware addresses.",
                        "A malicious device sends misleading ARP messages.",
                        "Other devices may update their ARP caches with incorrect mappings.",
                        "Traffic may be redirected or disrupted."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Traffic Redirected on an Office LAN",
                            "content": (
                                "A monitoring system detects repeated changes in "
                                "IP-to-MAC address mappings. Administrators inspect "
                                "the affected network segment and identify the "
                                "source of the suspicious announcements."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Conflicting Address Mappings",
                        "content": (
                            "Users on a local network experience intermittent "
                            "connectivity. Network logs show one IP address "
                            "associated with multiple hardware addresses. The "
                            "administrator isolates the affected port and "
                            "reviews switch security settings."
                        ),
                        "discussion": [
                            "Why are unexpected ARP changes worth investigating?",
                            "How can network segmentation reduce exposure?",
                            "What role can switch security controls play?"
                        ]
                    },
                    "simulation": {
                        "title": "Recognize Suspicious ARP Changes",
                        "scenario": (
                            "A fictional network-monitoring report shows repeated "
                            "ARP changes involving the default gateway."
                        ),
                        "tasks": [
                            "Identify the conflicting mappings.",
                            "Determine which devices require investigation.",
                            "Select appropriate containment measures.",
                            "Recommend controls that reduce ARP spoofing risk."
                        ],
                        "expected_outcome": (
                            "The learner identifies suspicious address mappings "
                            "and proposes a controlled network investigation."
                        )
                    },
                    "practical_lab": {
                        "title": "Inspect ARP Tables and Switch Alerts",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied ARP-table snapshot.",
                            "Compare gateway mappings with the approved network inventory.",
                            "Identify unexpected or changing mappings.",
                            "Recommend switch-level protections and monitoring."
                        ],
                        "expected_result": (
                            "A report identifying suspicious mappings and "
                            "recommended network protections."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What does ARP spoofing attempt to manipulate?",
                            "options": [
                                "IP-to-hardware address mappings on a local network",
                                "A user's desktop wallpaper",
                                "A file's font size",
                                "A website's color scheme"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Forged ARP messages can cause incorrect IP-to-MAC mappings."
                            )
                        }
                    ],
                    "prevention": [
                        "Enable Dynamic ARP Inspection where supported.",
                        "Use DHCP snooping and appropriate switch protections.",
                        "Segment networks and restrict physical access.",
                        "Monitor unexpected changes in gateway mappings.",
                        "Investigate repeated connectivity anomalies."
                    ],
                    "conclusion": (
                        "Monitoring address mappings and configuring network "
                        "switches securely can reduce ARP spoofing risk."
                    )
                }
            }
        },

        "availability_attacks": {
            "id": "availability-attacks",
            "name": "Network Availability Attacks",
            "description": (
                "Attacks that overload, disrupt, or exhaust network and service resources."
            ),
            "types": {
                "dos": {
                    "id": "dos",
                    "name": "Denial-of-Service (DoS)",
                    "overview": (
                        "A denial-of-service attack attempts to make a service "
                        "unavailable by exhausting its bandwidth, processing "
                        "capacity, connection limits, or other resources."
                    ),
                    "how_it_works": [
                        "An attacker directs excessive or malformed requests at a service.",
                        "The target consumes resources processing the requests.",
                        "Legitimate users experience delays or failed connections.",
                        "Defenders identify the traffic pattern and apply mitigation."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unavailable Online Service",
                            "content": (
                                "A public website becomes slow during a sudden "
                                "traffic spike. The operations team checks traffic "
                                "patterns, service health, and infrastructure "
                                "metrics to distinguish an attack from legitimate demand."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Service Disruption During Peak Hours",
                        "content": (
                            "A business portal becomes unavailable and its request "
                            "rate rises sharply. The team activates traffic filtering, "
                            "reviews logs, and coordinates with its hosting provider "
                            "to restore availability."
                        ),
                        "discussion": [
                            "How can teams distinguish an attack from a traffic surge?",
                            "Why is coordination with a hosting provider useful?",
                            "Which metrics help assess recovery?"
                        ]
                    },
                    "simulation": {
                        "title": "Respond to a DoS Alert",
                        "scenario": (
                            "A service-health dashboard shows a sharp increase "
                            "in failed requests and response times."
                        ),
                        "tasks": [
                            "Review request rates and service-health metrics.",
                            "Identify possible resource exhaustion.",
                            "Select proportionate mitigation actions.",
                            "Prepare a brief incident summary."
                        ],
                        "expected_outcome": (
                            "The learner follows a structured availability-incident "
                            "response and monitors recovery."
                        )
                    },
                    "practical_lab": {
                        "title": "Analyze Service Availability Metrics",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied dataset of request rates and response times.",
                            "Identify the time window when service health deteriorated.",
                            "Compare traffic patterns with error rates and resource usage.",
                            "Recommend filtering, rate limiting, or capacity adjustments."
                        ],
                        "expected_result": (
                            "An availability incident report based on supplied metrics."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the main objective of a DoS attack?",
                            "options": [
                                "To improve server performance",
                                "To make a service unavailable to legitimate users",
                                "To organize files",
                                "To update a browser"
                            ],
                            "answer": 1,
                            "explanation": (
                                "DoS attacks attempt to disrupt access to a service."
                            )
                        }
                    ],
                    "prevention": [
                        "Use rate limiting and appropriate traffic filtering.",
                        "Monitor service health and traffic patterns.",
                        "Maintain capacity plans and recovery procedures.",
                        "Use provider-level protection when appropriate.",
                        "Test incident-response plans."
                    ],
                    "conclusion": (
                        "Monitoring, resilient infrastructure, and prepared "
                        "mitigation procedures help maintain service availability."
                    )
                },

                "ddos": {
                    "id": "ddos",
                    "name": "Distributed Denial-of-Service (DDoS)",
                    "overview": (
                        "A distributed denial-of-service attack sends disruptive "
                        "traffic from multiple sources, often compromised devices. "
                        "The distributed volume can make filtering and mitigation "
                        "more difficult than with a single source."
                    ),
                    "how_it_works": [
                        "Multiple devices or systems send traffic toward a target.",
                        "The combined traffic consumes bandwidth or service resources.",
                        "Legitimate requests may be delayed or blocked.",
                        "Defenders coordinate filtering and mitigation across the network."
                    ],
                    "real_world_examples": [
                        {
                            "title": "A Distributed Traffic Flood",
                            "content": (
                                "An online service receives traffic from many "
                                "unrelated addresses and becomes unavailable. "
                                "The provider applies upstream filtering and "
                                "works with the organization to restore service."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "A Multi-Source Availability Incident",
                        "content": (
                            "A company experiences a sudden flood of requests "
                            "from numerous sources. Its incident team contacts "
                            "the hosting provider, activates mitigation services, "
                            "and tracks service restoration."
                        ),
                        "discussion": [
                            "Why can blocking one source be insufficient?",
                            "What role does upstream filtering play?",
                            "Which recovery metrics should be recorded?"
                        ]
                    },
                    "simulation": {
                        "title": "Coordinate a DDoS Response",
                        "scenario": (
                            "A fictional dashboard shows a large traffic increase "
                            "across several regions and a drop in service availability."
                        ),
                        "tasks": [
                            "Identify the distributed traffic pattern.",
                            "Choose when to involve the network provider.",
                            "Recommend layered traffic mitigation.",
                            "Verify whether legitimate traffic can reach the service."
                        ],
                        "expected_outcome": (
                            "The learner creates a coordinated response that "
                            "balances mitigation with legitimate service access."
                        )
                    },
                    "practical_lab": {
                        "title": "DDoS Metrics and Mitigation Review",
                        "mode": "defensive",
                        "steps": [
                            "Inspect a supplied traffic dashboard and incident timeline.",
                            "Compare traffic volume, source distribution, and error rates.",
                            "Identify when mitigation was activated.",
                            "Recommend upstream protection and recovery checks."
                        ],
                        "expected_result": (
                            "A defensive review of a distributed availability incident."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What distinguishes a DDoS attack from a basic DoS attack?",
                            "options": [
                                "A DDoS attack uses multiple distributed sources",
                                "A DDoS attack never affects availability",
                                "A DDoS attack only targets printers",
                                "A DDoS attack is always accidental"
                            ],
                            "answer": 0,
                            "explanation": (
                                "DDoS traffic originates from multiple distributed sources."
                            )
                        }
                    ],
                    "prevention": [
                        "Use DDoS protection from reputable network providers.",
                        "Apply layered filtering and rate controls.",
                        "Maintain scalable infrastructure where appropriate.",
                        "Prepare escalation paths with hosting and network providers.",
                        "Monitor recovery and verify legitimate access."
                    ],
                    "conclusion": (
                        "DDoS resilience requires coordinated mitigation, "
                        "provider support, and well-tested recovery procedures."
                    )
                }
            }
        },

        "network_access_attacks": {
            "id": "network-access-attacks",
            "name": "Network Access and Configuration Attacks",
            "description": (
                "Threats that exploit weaknesses in network access controls, "
                "services, or device configuration."
            ),
            "types": {
                "dns_spoofing": {
                    "id": "dns-spoofing",
                    "name": "DNS Spoofing",
                    "overview": (
                        "DNS spoofing involves supplying false DNS information "
                        "so a domain name resolves to an unintended address. "
                        "It may redirect users toward fraudulent services."
                    ),
                    "how_it_works": [
                        "A user or application requests a domain's address.",
                        "False DNS information is supplied or a DNS cache is manipulated.",
                        "The domain may resolve to an unexpected destination.",
                        "The user could be exposed to an impersonated service."
                    ],
                    "real_world_examples": [
                        {
                            "title": "A Familiar Name Opens the Wrong Site",
                            "content": (
                                "A user enters a familiar domain but reaches an "
                                "unexpected page. The security team checks DNS "
                                "responses, domain configuration, and certificate details."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Unexpected DNS Resolution",
                        "content": (
                            "Several devices resolve an internal service to an "
                            "unrecognized address. Administrators compare DNS "
                            "records with approved configurations and investigate "
                            "the resolver and affected clients."
                        ),
                        "discussion": [
                            "Why should DNS answers be checked against trusted records?",
                            "How can secure DNS operations reduce risk?",
                            "Why is certificate validation still important?"
                        ]
                    },
                    "simulation": {
                        "title": "Review a Suspicious DNS Record",
                        "scenario": (
                            "A sample monitoring report shows a domain resolving "
                            "to an address that differs from the approved record."
                        ),
                        "tasks": [
                            "Compare the observed and expected DNS answers.",
                            "Identify which systems require further checks.",
                            "Recommend safe validation and remediation.",
                            "Explain how users should handle unexpected destinations."
                        ],
                        "expected_outcome": (
                            "The learner identifies a DNS anomaly and recommends "
                            "verification through trusted records and services."
                        )
                    },
                    "practical_lab": {
                        "title": "DNS Record Verification",
                        "mode": "defensive",
                        "steps": [
                            "Review a fictional DNS inventory and resolver log.",
                            "Compare observed answers with approved records.",
                            "Identify unexplained changes.",
                            "Document corrective actions and monitoring requirements."
                        ],
                        "expected_result": (
                            "A DNS-integrity report containing findings and recommendations."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is a possible consequence of DNS spoofing?",
                            "options": [
                                "A domain may resolve to a fraudulent destination",
                                "A monitor changes its brightness",
                                "A keyboard types faster",
                                "A file is automatically compressed"
                            ],
                            "answer": 0,
                            "explanation": (
                                "False DNS information can direct users to an unintended address."
                            )
                        }
                    ],
                    "prevention": [
                        "Secure DNS administration and restrict record changes.",
                        "Monitor for unexpected DNS responses.",
                        "Use DNSSEC validation where supported and appropriate.",
                        "Maintain reliable DNS logs and approved records.",
                        "Use HTTPS and validate certificates."
                    ],
                    "conclusion": (
                        "DNS integrity checks, secure administration, and "
                        "certificate validation help reduce redirection risks."
                    )
                },

                "port_scanning_and_service_discovery": {
                    "id": "port-scanning-and-service-discovery",
                    "name": "Port Scanning and Service Discovery",
                    "overview": (
                        "Port scanning checks which network ports respond on "
                        "a host. Administrators and security testers use it "
                        "for authorized inventory and assessment, while attackers "
                        "may use the same technique to find exposed services."
                    ),
                    "how_it_works": [
                        "A scanner sends connection probes to selected ports.",
                        "Responses help indicate whether ports are open, closed, or filtered.",
                        "Service discovery may identify exposed applications.",
                        "Defenders compare the results with the approved network inventory."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unexpectedly Exposed Service",
                            "content": (
                                "A routine security review discovers a management "
                                "service reachable from an untrusted network. "
                                "Administrators restrict access and verify whether "
                                "the exposure was authorized."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Reducing the Exposed Attack Surface",
                        "content": (
                            "An organization discovers several unnecessary "
                            "services on a public-facing server. The team verifies "
                            "business requirements, disables unused services, "
                            "and repeats an authorized exposure review."
                        ),
                        "discussion": [
                            "Why should scans be limited to authorized systems?",
                            "How can unnecessary open ports increase risk?",
                            "Why is a follow-up scan useful?"
                        ]
                    },
                    "simulation": {
                        "title": "Review a Port-Scan Report",
                        "scenario": (
                            "A fictional scan report lists open services on "
                            "a server that should expose only a web application."
                        ),
                        "tasks": [
                            "Identify services that do not match the intended role.",
                            "Determine which findings need verification.",
                            "Recommend access restrictions or service removal.",
                            "Prepare a prioritized remediation list."
                        ],
                        "expected_outcome": (
                            "The learner identifies unnecessary exposure and "
                            "proposes authorized corrective actions."
                        )
                    },
                    "practical_lab": {
                        "title": "Network Exposure Audit",
                        "mode": "defensive",
                        "steps": [
                            "Inspect a supplied port-scan report from a lab environment.",
                            "Compare exposed services with an approved baseline.",
                            "Prioritize unnecessary or risky services.",
                            "Document firewall and service-hardening recommendations."
                        ],
                        "expected_result": (
                            "An exposure-audit report with prioritized findings."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Why is port scanning useful to a defender?",
                            "options": [
                                "It identifies potentially exposed network services",
                                "It guarantees that a server is invulnerable",
                                "It replaces all security monitoring",
                                "It automatically fixes every vulnerability"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Port scanning helps identify exposed services "
                                "that may require verification or restriction."
                            )
                        }
                    ],
                    "prevention": [
                        "Disable services that are not required.",
                        "Restrict management interfaces to trusted networks.",
                        "Apply firewall rules based on business requirements.",
                        "Keep exposed services patched.",
                        "Perform regular authorized exposure reviews."
                    ],
                    "conclusion": (
                        "Knowing which services are exposed helps organizations "
                        "reduce their attack surface and prioritize hardening."
                    )
                }
            }
        }
    }
}