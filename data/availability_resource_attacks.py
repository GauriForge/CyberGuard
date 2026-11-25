
AVAILABILITY_RESOURCE_ATTACKS = {
    "id": "availability-resource",
    "name": "Availability and Resource Attacks",
    "description": "Attacks that disrupt the availability, reliability or performance of systems, networks and digital services by overwhelming resources or exploiting weaknesses in resource management.",

    "subcategories": {
        "service_disruption_attacks": {
            "id": "service-disruption-attacks",
            "name": "Service Disruption Attacks",
            "description": "Attacks that make websites, applications, servers or networks slow or unavailable to legitimate users.",

            "types": {
                "denial_of_service": {
                    "id": "denial-of-service",
                    "name": "Denial-of-Service (DoS) Attack",
                    "overview": "A denial-of-service attack attempts to make a system or service unavailable by exhausting its resources or disrupting its normal operation. The impact may include slow responses, failed requests or complete service interruption.",

                    "how_it_works": [
                        "An attacker targets a service, network connection or system resource.",
                        "The target receives excessive requests or encounters activity that consumes its available capacity.",
                        "Legitimate users experience delays, errors or an inability to access the service.",
                        "Defenders identify the affected resource, filter malicious activity and restore normal service."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Unavailable Online Store",
                            "description": "A fictional online store receives an abnormal volume of requests and becomes too slow to serve genuine customers."
                        },
                        {
                            "title": "An Overloaded Public Website",
                            "description": "A public information website experiences a surge of unwanted traffic that prevents some visitors from accessing important information."
                        }
                    ],

                    "case_study": {
                        "title": "The Website That Stopped Responding",
                        "scenario": "A fictional organisation notices that its public website is responding slowly and then begins returning errors during an unusual traffic surge.",
                        "findings": [
                            "The number of incoming requests increased sharply.",
                            "Application response times rose and some requests failed.",
                            "The team needed to distinguish legitimate demand from malicious traffic."
                        ],
                        "lesson": "Capacity planning, traffic monitoring and an incident response process help organisations respond to service disruption."
                    },

                    "simulation": {
                        "title": "Respond to a Service Availability Incident",
                        "scenario": "A simulated monitoring dashboard shows increased request volume, high resource usage and a growing error rate.",
                        "tasks": [
                            "Identify which service metrics have changed.",
                            "Determine whether the incident affects all users or only particular functions.",
                            "Choose appropriate traffic filtering and escalation steps.",
                            "Recommend recovery and post-incident monitoring."
                        ],
                        "expected_learning": "Recognise service disruption indicators and select proportionate defensive responses."
                    },

                    "practical_lab": {
                        "title": "DoS Incident Analysis",
                        "objective": "Investigate a simulated service disruption using synthetic monitoring data.",
                        "activities": [
                            "Review fictional request-volume and response-time charts.",
                            "Identify the period when service performance deteriorated.",
                            "Compare traffic patterns with a normal baseline.",
                            "Prepare a containment, recovery and communication plan."
                        ],
                        "safety": "Use synthetic logs or an isolated local simulation. Do not flood real systems or send disruptive traffic to public services."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is the primary objective of a DoS attack?",
                                "options": [
                                    "To make a service unavailable to legitimate users",
                                    "To improve server performance",
                                    "To create a secure backup",
                                    "To update application software"
                                ],
                                "answer": "To make a service unavailable to legitimate users",
                                "explanation": "A DoS attack attempts to disrupt the availability of a targeted service or resource."
                            },
                            {
                                "question": "What should a defender examine during a suspected DoS incident?",
                                "options": [
                                    "Traffic patterns, resource usage and service errors",
                                    "Only the website's colours",
                                    "The number of employees on holiday",
                                    "Unrelated document formatting"
                                ],
                                "answer": "Traffic patterns, resource usage and service errors",
                                "explanation": "These indicators help identify the scope and possible cause of service disruption."
                            }
                        ]
                    },

                    "prevention": [
                        "Monitor traffic volume, error rates and resource utilisation.",
                        "Use rate limiting and suitable traffic filtering.",
                        "Configure infrastructure capacity and timeouts appropriately.",
                        "Deploy protective services suited to the application's exposure.",
                        "Maintain incident response and service recovery procedures.",
                        "Coordinate with hosting providers or network operators when necessary."
                    ],

                    "conclusion": "DoS attacks threaten service availability and can interrupt essential operations. Monitoring, traffic controls and a tested response plan help reduce their impact."
                },

                "distributed_denial_of_service": {
                    "id": "distributed-denial-of-service",
                    "name": "Distributed Denial-of-Service (DDoS) Attack",
                    "overview": "A distributed denial-of-service attack attempts to overwhelm a target using traffic or requests from many sources. Because activity originates from multiple systems, distinguishing malicious traffic from legitimate demand can be more difficult than with a single-source attack.",

                    "how_it_works": [
                        "An attacker coordinates traffic from multiple systems, sometimes including compromised devices.",
                        "The target receives a large volume of traffic or requests across one or more services.",
                        "Network bandwidth, connection capacity or application resources become strained.",
                        "Defenders use traffic analysis, filtering and upstream mitigation to restore availability."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Online Service Facing Distributed Traffic",
                            "description": "A fictional online platform experiences a large traffic surge from many unrelated source addresses and becomes intermittently unavailable."
                        },
                        {
                            "title": "A Public Information Portal Under Pressure",
                            "description": "A public portal receives traffic from distributed sources, affecting access for ordinary visitors."
                        }
                    ],

                    "case_study": {
                        "title": "The Distributed Traffic Surge",
                        "scenario": "A fictional service provider detects a sudden increase in incoming traffic from many networks while legitimate users report connection failures.",
                        "findings": [
                            "The traffic originated from numerous sources.",
                            "The affected service showed increased latency and failed connections.",
                            "Filtering at the application alone was insufficient to address all incoming traffic."
                        ],
                        "lesson": "DDoS readiness should include upstream protection, provider coordination and clear service recovery procedures."
                    },

                    "simulation": {
                        "title": "Coordinate a DDoS Response",
                        "scenario": "Learners act as a defensive team responding to synthetic traffic statistics for a fictional public website.",
                        "tasks": [
                            "Compare normal and abnormal traffic levels.",
                            "Identify affected services and user-facing symptoms.",
                            "Select appropriate escalation and mitigation options.",
                            "Plan how to verify recovery and communicate service status."
                        ],
                        "expected_learning": "Understand why distributed attacks require coordinated defensive measures."
                    },

                    "practical_lab": {
                        "title": "Distributed Traffic Log Investigation",
                        "objective": "Analyse synthetic traffic summaries and prepare a defensive response.",
                        "activities": [
                            "Examine fictional source-distribution and request-volume reports.",
                            "Identify abnormal changes in traffic and service health.",
                            "Recommend upstream mitigation and application-level controls.",
                            "Write an incident timeline and recovery checklist."
                        ],
                        "safety": "Use prepared datasets or a closed simulation only. Do not generate DDoS traffic or target external systems."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What distinguishes a DDoS attack from a basic DoS attack?",
                                "options": [
                                    "It uses multiple sources to coordinate the disruption",
                                    "It always targets only one user's device",
                                    "It is a method of encrypting backups",
                                    "It cannot affect online services"
                                ],
                                "answer": "It uses multiple sources to coordinate the disruption",
                                "explanation": "DDoS attacks distribute disruptive traffic across multiple sources."
                            },
                            {
                                "question": "Why might upstream DDoS mitigation be useful?",
                                "options": [
                                    "It can help filter traffic before it reaches the affected infrastructure",
                                    "It guarantees that software will never contain vulnerabilities",
                                    "It removes the need for monitoring",
                                    "It prevents legitimate users from accessing every service"
                                ],
                                "answer": "It can help filter traffic before it reaches the affected infrastructure",
                                "explanation": "Filtering traffic upstream can reduce the load reaching the target network."
                            }
                        ]
                    },

                    "prevention": [
                        "Use a suitable DDoS protection or content delivery service.",
                        "Coordinate response arrangements with hosting and network providers.",
                        "Apply rate limiting and application-level traffic controls.",
                        "Monitor network and application health continuously.",
                        "Maintain resilient infrastructure and tested recovery procedures.",
                        "Document escalation contacts and communication responsibilities."
                    ],

                    "conclusion": "DDoS attacks can overwhelm services through distributed traffic. Layered mitigation, provider coordination and tested incident procedures improve resilience."
                },

                "application_resource_exhaustion": {
                    "id": "application-resource-exhaustion",
                    "name": "Application Resource Exhaustion",
                    "overview": "Application resource exhaustion occurs when requests or operations consume excessive memory, processing time, database connections or other finite resources. It may result from malicious activity, inefficient code, unexpected demand or a combination of these factors.",

                    "how_it_works": [
                        "A request or operation consumes more resources than the application can safely provide.",
                        "Repeated or expensive operations increase resource usage.",
                        "The application slows down, queues requests or stops responding.",
                        "Defenders identify the costly operation, control demand and correct the underlying weakness."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Expensive Search Function",
                            "description": "A poorly optimised search feature consumes excessive database resources when many users search at the same time."
                        },
                        {
                            "title": "Exhausted Application Connections",
                            "description": "An application fails to release database connections properly, eventually leaving new users unable to obtain one."
                        }
                    ],

                    "case_study": {
                        "title": "The Application Running Out of Connections",
                        "scenario": "A fictional learning platform begins returning errors after repeated requests cause its database connection pool to become exhausted.",
                        "findings": [
                            "The connection pool reached its configured limit.",
                            "Some operations held connections longer than expected.",
                            "Increasing the connection limit alone did not resolve the underlying inefficiency."
                        ],
                        "lesson": "Resource limits, efficient code, timeouts and careful connection management work together to improve reliability."
                    },

                    "simulation": {
                        "title": "Diagnose an Overloaded Application",
                        "scenario": "A synthetic dashboard shows increasing memory use, slow database queries and a growing request queue.",
                        "tasks": [
                            "Identify which resources are approaching their limits.",
                            "Compare response times with resource utilisation.",
                            "Choose suitable containment measures, such as limiting expensive operations.",
                            "Recommend a longer-term application fix."
                        ],
                        "expected_learning": "Connect resource metrics to application reliability and identify practical defensive improvements."
                    },

                    "practical_lab": {
                        "title": "Resource Utilisation Analysis",
                        "objective": "Investigate a prepared application performance dataset.",
                        "activities": [
                            "Review synthetic memory, CPU and connection-pool metrics.",
                            "Identify resource saturation and its relationship to failed requests.",
                            "Recommend suitable timeouts, quotas and resource limits.",
                            "Prepare a remediation checklist for developers."
                        ],
                        "safety": "Use synthetic metrics or a local test application. Do not overload production systems."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is resource exhaustion?",
                                "options": [
                                    "When an application consumes available resources and cannot serve requests reliably",
                                    "When all application resources are backed up securely",
                                    "When an administrator updates a password",
                                    "When a website changes its visual theme"
                                ],
                                "answer": "When an application consumes available resources and cannot serve requests reliably",
                                "explanation": "Resource exhaustion can prevent an application from handling legitimate work."
                            },
                            {
                                "question": "Which measure helps prevent application resource exhaustion?",
                                "options": [
                                    "Use appropriate limits, timeouts and efficient resource management",
                                    "Remove all request limits",
                                    "Ignore connection leaks",
                                    "Allow every operation to run indefinitely"
                                ],
                                "answer": "Use appropriate limits, timeouts and efficient resource management",
                                "explanation": "Limits and timeouts help keep individual operations from consuming resources indefinitely."
                            }
                        ]
                    },

                    "prevention": [
                        "Set appropriate request limits, quotas and timeouts.",
                        "Optimise expensive application and database operations.",
                        "Release connections, memory and other resources correctly.",
                        "Monitor resource utilisation and queue lengths.",
                        "Test applications under representative workloads.",
                        "Use graceful degradation and recovery mechanisms where appropriate."
                    ],

                    "conclusion": "Resource exhaustion can interrupt a service even without a large network attack. Efficient application design, sensible limits and monitoring help maintain reliable performance."
                }
            }
        },

        "resource_misuse_attacks": {
            "id": "resource-misuse-attacks",
            "name": "Resource Misuse and Availability Threats",
            "description": "Threats involving excessive resource consumption, inefficient operations or failures that reduce the availability of systems and services.",

            "types": {
                "algorithmic_complexity_abuse": {
                    "id": "algorithmic-complexity-abuse",
                    "name": "Algorithmic Complexity Abuse",
                    "overview": "Algorithmic complexity abuse occurs when input or usage patterns cause an application to perform disproportionately expensive computations. A feature that works normally with typical input may consume excessive CPU time or memory when given unusual or deliberately selected input.",

                    "how_it_works": [
                        "An application processes user-controlled input using an inefficient or vulnerable algorithm.",
                        "Certain inputs cause processing costs to grow significantly.",
                        "Repeated requests or unusually expensive operations degrade application performance.",
                        "Developers identify the expensive code path and introduce safer algorithms, validation or limits."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Slow Input-Processing Function",
                            "description": "A fictional service experiences long processing delays because a particular class of input triggers unexpectedly expensive computation."
                        },
                        {
                            "title": "An Inefficient Data Query",
                            "description": "A search function performs a costly operation for broad queries, consuming resources needed by other users."
                        }
                    ],

                    "case_study": {
                        "title": "The Request That Took Too Long",
                        "scenario": "A fictional web application becomes slow when processing certain valid-looking inputs, even though the overall request count remains moderate.",
                        "findings": [
                            "A small subset of requests consumed a disproportionate amount of CPU time.",
                            "Typical test inputs did not reveal the performance problem.",
                            "The team needed tests covering unusual inputs and worst-case processing costs."
                        ],
                        "lesson": "Worst-case performance testing and safe algorithm design can prevent unexpectedly expensive operations from affecting service availability."
                    },

                    "simulation": {
                        "title": "Find an Expensive Processing Path",
                        "scenario": "Learners receive a fictional performance report containing request durations, input sizes and CPU measurements.",
                        "tasks": [
                            "Identify operations with unusually high processing times.",
                            "Compare input size with processing cost.",
                            "Recommend input validation and computational limits.",
                            "Explain how regression tests can prevent the issue from returning."
                        ],
                        "expected_learning": "Recognise performance weaknesses without attempting to disrupt a real application."
                    },

                    "practical_lab": {
                        "title": "Worst-Case Performance Review",
                        "objective": "Review a prepared performance dataset and identify disproportionate computational costs.",
                        "activities": [
                            "Compare normal and unusually expensive synthetic test cases.",
                            "Identify processing paths that require investigation.",
                            "Recommend safer algorithms and bounded operations.",
                            "Create a test checklist for worst-case performance."
                        ],
                        "safety": "Use pre-generated results or a small local demonstration. Do not test unapproved public services."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is a key characteristic of algorithmic complexity abuse?",
                                "options": [
                                    "Certain inputs cause disproportionately high processing costs",
                                    "Every input consumes exactly the same resources",
                                    "It always involves stolen passwords",
                                    "It only affects physical devices"
                                ],
                                "answer": "Certain inputs cause disproportionately high processing costs",
                                "explanation": "Expensive processing paths can reduce availability even when request volume is not unusually high."
                            },
                            {
                                "question": "Which development practice helps reduce this risk?",
                                "options": [
                                    "Test worst-case inputs and use bounded, efficient algorithms",
                                    "Ignore slow requests",
                                    "Remove all input validation",
                                    "Allow unbounded computation"
                                ],
                                "answer": "Test worst-case inputs and use bounded, efficient algorithms",
                                "explanation": "Worst-case testing helps reveal operations that may consume excessive resources."
                            }
                        ]
                    },

                    "prevention": [
                        "Choose efficient algorithms with understood worst-case behaviour.",
                        "Validate input size and complexity.",
                        "Set execution timeouts and computational limits.",
                        "Profile performance using representative and edge-case inputs.",
                        "Apply regression tests to expensive code paths.",
                        "Monitor unusually long-running operations."
                    ],

                    "conclusion": "Algorithmic complexity weaknesses can turn ordinary application features into availability risks. Efficient algorithms, input bounds and worst-case testing reduce this exposure."
                },

                "cryptocurrency_mining_abuse": {
                    "id": "cryptocurrency-mining-abuse",
                    "name": "Unauthorised Cryptocurrency Mining",
                    "overview": "Unauthorised cryptocurrency mining occurs when a person or malicious program uses computing resources without permission to perform cryptocurrency-related calculations. It can increase CPU or GPU utilisation, electricity costs and hardware wear while reducing performance for legitimate workloads.",

                    "how_it_works": [
                        "An unauthorised program or process begins using a device's computing resources.",
                        "CPU or GPU utilisation and power consumption may increase.",
                        "Legitimate applications may become slower or less responsive.",
                        "Defenders investigate processes, remove unauthorised software and address the initial compromise."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unexpected CPU Usage on a Workstation",
                            "description": "A fictional employee's workstation remains unusually busy when no demanding application is running."
                        },
                        {
                            "title": "Unapproved Cloud Resource Consumption",
                            "description": "A cloud account experiences unexplained compute usage that increases operational costs and reduces capacity available for approved workloads."
                        }
                    ],

                    "case_study": {
                        "title": "The Computer That Never Rested",
                        "scenario": "A fictional organisation observes persistent high CPU usage and rising cloud costs despite normal business activity.",
                        "findings": [
                            "Several processes were not associated with approved workloads.",
                            "Resource usage continued outside expected working periods.",
                            "The organisation needed to investigate both software execution and account access."
                        ],
                        "lesson": "Resource monitoring, access controls and software inventories help identify and prevent unauthorised computing activity."
                    },

                    "simulation": {
                        "title": "Investigate Unusual Compute Usage",
                        "scenario": "A fictional monitoring dashboard shows elevated CPU usage, increased power consumption and unexpected cloud charges.",
                        "tasks": [
                            "Compare resource usage with normal operating patterns.",
                            "Identify processes or workloads requiring verification.",
                            "Recommend containment and account review.",
                            "Develop measures to prevent recurrence."
                        ],
                        "expected_learning": "Identify suspicious resource consumption and respond using authorised defensive procedures."
                    },

                    "practical_lab": {
                        "title": "Compute Usage Investigation",
                        "objective": "Analyse synthetic process and cloud billing reports for unauthorised resource use.",
                        "activities": [
                            "Review a mock process inventory and CPU utilisation report.",
                            "Identify workloads that lack an approved owner or purpose.",
                            "Compare expected and actual cloud resource consumption.",
                            "Prepare a response and cost-control checklist."
                        ],
                        "safety": "Use synthetic reports or an authorised local test environment. Do not install mining software on systems without permission."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which sign may indicate unauthorised cryptocurrency mining?",
                                "options": [
                                    "Persistent unexplained CPU or GPU utilisation",
                                    "A documented operating system update",
                                    "Normal resource usage from an approved application",
                                    "A scheduled backup completing successfully"
                                ],
                                "answer": "Persistent unexplained CPU or GPU utilisation",
                                "explanation": "Unexplained sustained compute usage can indicate an unauthorised workload and warrants investigation."
                            },
                            {
                                "question": "What is an appropriate defensive response to suspected unauthorised mining?",
                                "options": [
                                    "Investigate the process, contain the issue and check for compromise",
                                    "Ignore the resource usage",
                                    "Give the process more privileges immediately",
                                    "Disable all security monitoring permanently"
                                ],
                                "answer": "Investigate the process, contain the issue and check for compromise",
                                "explanation": "Investigation and containment help identify the cause and prevent continued resource misuse."
                            }
                        ]
                    },

                    "prevention": [
                        "Monitor CPU, GPU, memory and cloud spending for unusual patterns.",
                        "Restrict software installation and execution privileges.",
                        "Protect cloud credentials and apply least-privilege access.",
                        "Maintain an inventory of approved software and workloads.",
                        "Investigate unexplained resource use promptly.",
                        "Review cloud budgets, alerts and workload ownership."
                    ],

                    "conclusion": "Unauthorised mining consumes resources that should support legitimate work. Monitoring, access control and timely investigation help protect performance and control costs."
                },

                "service_misconfiguration": {
                    "id": "service-misconfiguration",
                    "name": "Availability-Related Service Misconfiguration",
                    "overview": "Availability-related service misconfiguration occurs when settings such as resource limits, timeouts, capacity thresholds or recovery policies are unsuitable for the service's workload. These mistakes can cause preventable outages, even without malicious activity.",

                    "how_it_works": [
                        "A service is deployed with inadequate or unsuitable operational settings.",
                        "Normal demand changes or a component fails.",
                        "The service cannot handle the workload or recover correctly.",
                        "Administrators identify the configuration weakness and validate corrected settings."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Server with an Inadequate Connection Limit",
                            "description": "A service rejects legitimate requests because its configured connection pool is too small for expected usage."
                        },
                        {
                            "title": "A Missing Recovery Policy",
                            "description": "An application fails after a component interruption because its restart or recovery procedure was not configured correctly."
                        }
                    ],

                    "case_study": {
                        "title": "The Preventable Service Outage",
                        "scenario": "A fictional learning platform experiences repeated outages during busy periods because its resource limits and recovery settings do not match actual demand.",
                        "findings": [
                            "Capacity settings were based on outdated usage estimates.",
                            "Monitoring did not alert administrators before resource exhaustion.",
                            "Recovery procedures had not been tested under realistic conditions."
                        ],
                        "lesson": "Configuration reviews, capacity planning and recovery testing are important parts of operational security."
                    },

                    "simulation": {
                        "title": "Review Service Availability Settings",
                        "scenario": "Learners receive a fictional service configuration and a report describing intermittent outages.",
                        "tasks": [
                            "Identify unsuitable limits and missing alerts.",
                            "Compare configured capacity with expected workload.",
                            "Recommend safe changes and validation steps.",
                            "Develop a recovery test plan."
                        ],
                        "expected_learning": "Understand how configuration errors can affect availability and how to prevent repeated outages."
                    },

                    "practical_lab": {
                        "title": "Service Reliability Configuration Review",
                        "objective": "Evaluate a mock service configuration for availability risks.",
                        "activities": [
                            "Review fictional timeout, capacity and restart settings.",
                            "Identify missing monitoring thresholds.",
                            "Recommend suitable changes based on the stated workload.",
                            "Prepare a rollback and validation checklist."
                        ],
                        "safety": "Use sample configuration files or an isolated development environment. Do not modify production settings without authorisation."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "How can a service misconfiguration affect availability?",
                                "options": [
                                    "It can cause a service to fail under expected demand or during recovery",
                                    "It guarantees unlimited capacity",
                                    "It automatically eliminates all software defects",
                                    "It prevents the need for monitoring"
                                ],
                                "answer": "It can cause a service to fail under expected demand or during recovery",
                                "explanation": "Unsuitable operational settings can prevent a service from handling normal workloads or recovering from failures."
                            },
                            {
                                "question": "Which practice helps prevent availability-related configuration failures?",
                                "options": [
                                    "Review settings and test recovery procedures",
                                    "Make untested changes directly in production",
                                    "Remove capacity monitoring",
                                    "Ignore repeated outages"
                                ],
                                "answer": "Review settings and test recovery procedures",
                                "explanation": "Configuration reviews and recovery testing expose weaknesses before they cause larger incidents."
                            }
                        ]
                    },

                    "prevention": [
                        "Review resource limits and timeouts against realistic workloads.",
                        "Monitor service health and alert on early warning indicators.",
                        "Test recovery, restart and failover procedures.",
                        "Use controlled configuration changes and rollback plans.",
                        "Reassess capacity as usage patterns change.",
                        "Document operational settings and assign clear ownership."
                    ],

                    "conclusion": "Availability problems are not always caused by attackers. Suitable configuration, monitoring and tested recovery processes help keep services dependable."
                }
            }
        }
    }
}