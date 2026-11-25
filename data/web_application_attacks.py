
WEB_APPLICATION_ATTACKS = {
    "id": "web-application",
    "name": "Web Application Attacks",
    "description": (
        "Explore vulnerabilities in websites, web applications, APIs, "
        "authentication systems, and the handling of user-supplied data."
    ),
    "types": {
        "injection_attacks": {
            "id": "injection-attacks",
            "name": "Injection Attacks",
            "description": (
                "Attacks that exploit applications which treat untrusted input "
                "as part of a database query or another command."
            ),
            "types": {
                "sql_injection": {
                    "id": "sql-injection",
                    "name": "SQL Injection",
                    "overview": (
                        "SQL injection occurs when an application builds database "
                        "queries unsafely using user-supplied input. Depending on "
                        "the vulnerability and database permissions, an attacker "
                        "may read, modify, or delete data or bypass authentication."
                    ),
                    "how_it_works": [
                        "A web application accepts input, such as a username or search term.",
                        "The application combines that input with a database query unsafely.",
                        "The database interprets part of the input as query syntax rather than ordinary data.",
                        "The result may expose information or alter database operations.",
                        "Parameterized queries keep user input separate from SQL instructions."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unsafe Login Form",
                            "content": (
                                "A fictional shopping website constructs its login "
                                "query by concatenating values from a submitted form. "
                                "A security review identifies that the query can be "
                                "altered because the application does not use "
                                "parameterized statements."
                            )
                        },
                        {
                            "title": "A Vulnerable Product Search",
                            "content": (
                                "A product search feature inserts search text "
                                "directly into a database query. Unexpected input "
                                "causes database errors, revealing that input "
                                "handling needs improvement."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Exposed Customer Database",
                        "content": (
                            "A fictional retailer discovers suspicious database "
                            "queries after reviewing application logs. Investigators "
                            "trace the issue to an unsafe search endpoint, restrict "
                            "unnecessary database privileges, and correct the query "
                            "construction. They also review access logs to determine "
                            "whether customer information was accessed."
                        ),
                        "discussion": [
                            "Why is concatenating user input into SQL queries dangerous?",
                            "How do parameterized queries prevent SQL injection?",
                            "Why should database permissions be limited?",
                            "What evidence should investigators preserve?"
                        ]
                    },
                    "simulation": {
                        "title": "Investigate a Database Error",
                        "scenario": (
                            "A fictional web application records repeated database "
                            "errors associated with its product search feature."
                        ),
                        "tasks": [
                            "Identify the affected endpoint from the supplied logs.",
                            "Determine whether user input is handled safely.",
                            "Recommend parameterized queries and input validation.",
                            "Choose appropriate logging and incident-response actions."
                        ],
                        "expected_outcome": (
                            "The learner identifies unsafe query construction and "
                            "recommends secure database access."
                        )
                    },
                    "practical_lab": {
                        "title": "Secure Database Query Handling",
                        "mode": "defensive",
                        "environment": (
                            "Use a local training application or a deliberately "
                            "vulnerable educational application in an isolated lab."
                        ),
                        "steps": [
                            "Review a supplied example of unsafe query construction.",
                            "Identify where untrusted input enters the query.",
                            "Rewrite the example using parameterized queries.",
                            "Test normal searches and invalid input.",
                            "Confirm that database errors do not expose sensitive details."
                        ],
                        "expected_result": (
                            "A corrected query implementation that treats user "
                            "input as data rather than SQL instructions."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the main cause of SQL injection?",
                            "options": [
                                "Using parameterized queries",
                                "Combining untrusted input with SQL unsafely",
                                "Keeping a database updated",
                                "Limiting database privileges"
                            ],
                            "answer": 1,
                            "explanation": (
                                "SQL injection occurs when untrusted input can "
                                "change the meaning of a database query."
                            )
                        },
                        {
                            "question": "Which measure most directly prevents SQL injection?",
                            "options": [
                                "Hiding the website logo",
                                "Using parameterized queries",
                                "Increasing the number of database tables",
                                "Disabling application logs"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Parameterized queries separate SQL instructions "
                                "from values supplied by users."
                            )
                        }
                    ],
                    "prevention": [
                        "Use parameterized queries or prepared statements.",
                        "Avoid constructing SQL by concatenating untrusted input.",
                        "Apply least-privilege permissions to database accounts.",
                        "Validate input according to the expected data type and format.",
                        "Avoid exposing detailed database errors to users.",
                        "Test database-facing code during security reviews."
                    ],
                    "conclusion": (
                        "Safe query construction, restricted database privileges, "
                        "and careful error handling significantly reduce SQL injection risk."
                    )
                },

                "command_injection": {
                    "id": "command-injection",
                    "name": "OS Command Injection",
                    "overview": (
                        "OS command injection occurs when an application passes "
                        "untrusted input into operating-system commands unsafely. "
                        "Depending on the application's permissions, exploitation "
                        "can expose files, interrupt services, or compromise a system."
                    ),
                    "how_it_works": [
                        "An application accepts input for a task such as file processing.",
                        "The application passes the input into an operating-system command.",
                        "Unsafe command construction allows the input to affect command execution.",
                        "The application may perform operations that were not intended by its developer.",
                        "Safer APIs and strict input handling reduce this risk."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unsafe Diagnostic Feature",
                            "content": (
                                "A fictional administration page accepts a hostname "
                                "for a connectivity check and inserts it directly "
                                "into a shell command. The security review finds "
                                "that arbitrary input could affect command execution."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Vulnerable File Processor",
                        "content": (
                            "A web service uses an external command to process "
                            "uploaded documents. Investigators discover that "
                            "user-controlled filenames are included in the command "
                            "without safe handling. The service is restricted while "
                            "developers replace the unsafe implementation."
                        ),
                        "discussion": [
                            "Why should user-controlled data not be treated as command syntax?",
                            "When can a library API replace a shell command?",
                            "Why does running a service with limited privileges matter?"
                        ]
                    },
                    "simulation": {
                        "title": "Review an Unsafe System Integration",
                        "scenario": (
                            "A fictional application review reveals that a web "
                            "endpoint builds operating-system commands from form input."
                        ),
                        "tasks": [
                            "Identify the untrusted input and command-building operation.",
                            "Determine whether a dedicated library API is available.",
                            "Recommend safe argument handling and strict validation.",
                            "Define tests to verify the corrected implementation."
                        ],
                        "expected_outcome": (
                            "The learner identifies the unsafe integration and "
                            "proposes a safer implementation."
                        )
                    },
                    "practical_lab": {
                        "title": "Replace Unsafe Command Construction",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied code sample containing unsafe command construction.",
                            "Identify the source of user-controlled input.",
                            "Replace shell invocation with a suitable library API where possible.",
                            "If a subprocess is necessary, use a fixed executable and safely separated arguments.",
                            "Test invalid input and verify that unexpected commands cannot execute."
                        ],
                        "expected_result": (
                            "A safer implementation that prevents input from "
                            "altering intended operating-system operations."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What can cause OS command injection?",
                            "options": [
                                "Passing untrusted input unsafely into system commands",
                                "Using a dedicated file-processing library",
                                "Running a service with limited privileges",
                                "Keeping software patched"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Unsafe command construction may allow user input "
                                "to change the commands being executed."
                            )
                        }
                    ],
                    "prevention": [
                        "Prefer dedicated library APIs instead of shell commands.",
                        "Use fixed executables and safely separated arguments when subprocesses are necessary.",
                        "Validate input against strict allowlists.",
                        "Run applications with the minimum required privileges.",
                        "Avoid exposing command output or sensitive system details.",
                        "Review integrations that invoke external processes."
                    ],
                    "conclusion": (
                        "Safe APIs, careful argument handling, and least privilege "
                        "help prevent command injection."
                    )
                }
            }
        },

        "browser_side_attacks": {
            "id": "browser-side-attacks",
            "name": "Browser-Side Attacks",
            "description": (
                "Attacks that exploit unsafe browser-facing content, scripts, "
                "or trust between a user and a website."
            ),
            "types": {
                "cross_site_scripting": {
                    "id": "cross-site-scripting",
                    "name": "Cross-Site Scripting (XSS)",
                    "overview": (
                        "Cross-site scripting occurs when an application includes "
                        "untrusted content in a webpage without appropriate "
                        "contextual encoding or sanitization. A browser may then "
                        "interpret that content as executable script in the site's "
                        "security context."
                    ),
                    "how_it_works": [
                        "A website accepts or stores content supplied by a user.",
                        "The content is included in a page without appropriate safeguards.",
                        "A browser interprets the unsafe content as script or active markup.",
                        "The script may perform actions available to the affected page or expose accessible information.",
                        "Contextual output encoding and safe templating prevent unsafe interpretation."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Unsafe User Comments",
                            "content": (
                                "A fictional discussion website displays comments "
                                "without correctly encoding user-supplied content. "
                                "A security review finds that specially crafted "
                                "markup could execute in other users' browsers."
                            )
                        },
                        {
                            "title": "A Search Page Reflects Input",
                            "content": (
                                "A search page places the submitted search term "
                                "directly into its HTML response. Developers "
                                "correct the output handling so the term is "
                                "displayed as text."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Unsafe Content in a Discussion Forum",
                        "content": (
                            "Users report unexpected browser behavior while "
                            "viewing a discussion thread. The security team "
                            "reproduces the issue in a controlled test environment, "
                            "identifies unsafe rendering, corrects output encoding, "
                            "and reviews other templates that display user content."
                        ),
                        "discussion": [
                            "How does XSS differ from SQL injection?",
                            "Why must output encoding match the HTML context?",
                            "Why should developers review every place user content is rendered?"
                        ]
                    },
                    "simulation": {
                        "title": "Identify Unsafe Webpage Rendering",
                        "scenario": (
                            "A fictional application displays user comments and "
                            "search terms. A review identifies one template that "
                            "does not safely encode content."
                        ),
                        "tasks": [
                            "Identify which template renders untrusted input.",
                            "Determine whether the content is displayed as text or interpreted as markup.",
                            "Choose a safe rendering approach.",
                            "Retest normal text and special characters."
                        ],
                        "expected_outcome": (
                            "The learner identifies unsafe rendering and recommends "
                            "context-appropriate output encoding."
                        )
                    },
                    "practical_lab": {
                        "title": "Secure User-Generated Content",
                        "mode": "defensive",
                        "steps": [
                            "Use a local training page that displays sample comments.",
                            "Review how comments are inserted into the page.",
                            "Apply the template engine's autoescaping or suitable contextual encoding.",
                            "Sanitize HTML only when HTML input is an intentional requirement.",
                            "Test special characters and confirm they display safely."
                        ],
                        "expected_result": (
                            "User-supplied content is displayed safely without "
                            "being interpreted as unintended executable markup."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is a primary defense against XSS?",
                            "options": [
                                "Contextual output encoding",
                                "Disabling all user accounts",
                                "Storing every password in plain text",
                                "Removing database indexes"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Contextual output encoding helps browsers treat "
                                "untrusted content as data instead of executable markup."
                            )
                        },
                        {
                            "question": "Where can stored XSS content remain before another user views it?",
                            "options": [
                                "Only in a user's keyboard",
                                "In application storage, such as a database",
                                "Only in a network cable",
                                "Only in a browser's hardware"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Stored XSS commonly involves unsafe content "
                                "saved by an application and later rendered to users."
                            )
                        }
                    ],
                    "prevention": [
                        "Use templates with automatic escaping enabled.",
                        "Apply context-appropriate output encoding.",
                        "Sanitize HTML with a reputable sanitizer when rich HTML is required.",
                        "Avoid unsafe DOM manipulation and dangerous HTML insertion APIs.",
                        "Use Content Security Policy as an additional protective layer.",
                        "Test stored, reflected, and DOM-based rendering paths."
                    ],
                    "conclusion": (
                        "Safe rendering and contextual encoding help prevent "
                        "untrusted webpage content from becoming executable script."
                    )
                },

                "cross_site_request_forgery": {
                    "id": "cross-site-request-forgery",
                    "name": "Cross-Site Request Forgery (CSRF)",
                    "overview": (
                        "CSRF tricks an authenticated user's browser into sending "
                        "an unwanted request to a website where the user is already "
                        "signed in. The risk is greatest when the application relies "
                        "on automatically attached credentials without adequate "
                        "request verification."
                    ),
                    "how_it_works": [
                        "A user signs in to a website and receives an authenticated session.",
                        "The user visits another page that causes a request to the original website.",
                        "The browser may attach the original site's session credentials.",
                        "If the application does not verify the request appropriately, an unwanted action may occur.",
                        "CSRF tokens and suitable cookie settings help protect state-changing requests."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unwanted Account Change",
                            "content": (
                                "A fictional website changes account settings using "
                                "a request that relies only on the user's session "
                                "cookie. The developers correct the flow by verifying "
                                "that each state-changing request was intentionally submitted."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Protecting Account Settings",
                        "content": (
                            "A security review finds that a profile-update endpoint "
                            "does not validate request authenticity. The team adds "
                            "CSRF protection, reviews cookie settings, and confirms "
                            "that invalid requests cannot change account data."
                        ),
                        "discussion": [
                            "Why can a browser automatically attach session cookies?",
                            "Why should GET requests not perform state-changing operations?",
                            "How do CSRF tokens help verify legitimate requests?"
                        ]
                    },
                    "simulation": {
                        "title": "Review a State-Changing Request",
                        "scenario": (
                            "A fictional account settings page accepts updates "
                            "without verifying a request token."
                        ),
                        "tasks": [
                            "Identify the endpoint that changes account information.",
                            "Determine whether it verifies request authenticity.",
                            "Recommend CSRF protection and suitable cookie settings.",
                            "Test that requests with missing or invalid tokens are rejected."
                        ],
                        "expected_outcome": (
                            "The learner identifies missing request verification "
                            "and recommends appropriate safeguards."
                        )
                    },
                    "practical_lab": {
                        "title": "Add CSRF Protection to a Form",
                        "mode": "defensive",
                        "steps": [
                            "Review a local training application's state-changing form.",
                            "Enable the framework's supported CSRF protection.",
                            "Confirm that forms include valid tokens.",
                            "Submit requests with missing or invalid tokens in the test environment.",
                            "Verify that rejected requests do not change stored data."
                        ],
                        "expected_result": (
                            "State-changing requests require valid CSRF protection."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What does CSRF attempt to abuse?",
                            "options": [
                                "A user's authenticated browser session",
                                "A computer's screen resolution",
                                "The number of database tables",
                                "A website's image dimensions"
                            ],
                            "answer": 0,
                            "explanation": (
                                "CSRF can abuse the browser's existing authenticated "
                                "session to submit unwanted requests."
                            )
                        }
                    ],
                    "prevention": [
                        "Use framework-supported CSRF tokens on state-changing requests.",
                        "Use appropriate SameSite cookie settings.",
                        "Require authentication and authorization for sensitive operations.",
                        "Avoid state-changing actions through GET requests.",
                        "Validate request origin where appropriate as an additional defense.",
                        "Test rejected requests to ensure no changes occur."
                    ],
                    "conclusion": (
                        "Request verification, appropriate cookie settings, and "
                        "secure application design help prevent CSRF."
                    )
                }
            }
        },

        "authentication_and_session_attacks": {
            "id": "authentication-and-session-attacks",
            "name": "Authentication and Session Attacks",
            "description": (
                "Threats involving weak login controls, exposed sessions, "
                "and inadequate protection of user accounts."
            ),
            "types": {
                "broken_authentication": {
                    "id": "broken-authentication",
                    "name": "Broken Authentication",
                    "overview": (
                        "Broken authentication describes weaknesses in login, "
                        "identity verification, credential recovery, or account "
                        "management that may let unauthorized users access accounts."
                    ),
                    "how_it_works": [
                        "An application implements an incomplete or insecure authentication process.",
                        "Weak controls allow credentials or account-recovery flows to be abused.",
                        "An unauthorized user may gain access to an account.",
                        "Secure authentication, recovery controls, and monitoring reduce the risk."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Insecure Password Reset Flow",
                            "content": (
                                "A fictional service allows password resets after "
                                "checking only easily guessed personal information. "
                                "The team replaces this process with secure, "
                                "time-limited recovery tokens."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "A Weak Account Recovery Process",
                        "content": (
                            "A security assessment finds that account recovery "
                            "does not adequately verify the account owner. The "
                            "team introduces short-lived recovery tokens, rate "
                            "limits, and alerts for suspicious recovery activity."
                        ),
                        "discussion": [
                            "Why should password recovery be as secure as login?",
                            "Why should recovery tokens expire?",
                            "How can monitoring detect suspicious account activity?"
                        ]
                    },
                    "simulation": {
                        "title": "Review Login and Recovery Controls",
                        "scenario": (
                            "A fictional service receives repeated login failures "
                            "and unusual password-reset requests."
                        ),
                        "tasks": [
                            "Review the supplied authentication event summary.",
                            "Identify weaknesses in login and recovery procedures.",
                            "Recommend rate limiting and secure recovery tokens.",
                            "Define when suspicious activity should trigger an alert."
                        ],
                        "expected_outcome": (
                            "The learner identifies authentication weaknesses and "
                            "recommends secure account-management controls."
                        )
                    },
                    "practical_lab": {
                        "title": "Authentication Security Review",
                        "mode": "defensive",
                        "steps": [
                            "Review a sample login and password-reset design.",
                            "Check password storage and recovery-token handling.",
                            "Recommend rate limiting and multi-factor authentication.",
                            "Test token expiration and invalid recovery requests.",
                            "Document the required security improvements."
                        ],
                        "expected_result": (
                            "An authentication review covering login, recovery, "
                            "credential storage, and account protection."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Which practice improves account security?",
                            "options": [
                                "Using secure password hashing and multi-factor authentication",
                                "Storing passwords in plain text",
                                "Using predictable recovery tokens",
                                "Allowing unlimited login attempts"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Secure password hashing and multi-factor "
                                "authentication improve account protection."
                            )
                        }
                    ],
                    "prevention": [
                        "Use established authentication libraries and framework features.",
                        "Store passwords using an appropriate password-hashing algorithm.",
                        "Enable multi-factor authentication where practical.",
                        "Rate-limit login and recovery attempts.",
                        "Use short-lived, single-use password-reset tokens.",
                        "Monitor unusual authentication and recovery events."
                    ],
                    "conclusion": (
                        "Secure login, recovery, credential storage, and monitoring "
                        "reduce the risk of account compromise."
                    )
                },

                "session_hijacking": {
                    "id": "session-hijacking",
                    "name": "Session Hijacking",
                    "overview": (
                        "Session hijacking occurs when an unauthorized party "
                        "obtains or misuses a valid session identifier to act "
                        "as an authenticated user. Exposed cookies, insecure "
                        "transport, or compromised devices can increase the risk."
                    ),
                    "how_it_works": [
                        "A user authenticates and receives a session identifier.",
                        "The identifier is exposed or improperly protected.",
                        "An unauthorized party may attempt to reuse the identifier.",
                        "Secure cookies, session rotation, and expiration help reduce the risk."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Exposed Session Cookie",
                            "content": (
                                "A fictional web application fails to mark its "
                                "session cookie as Secure. A security review "
                                "identifies the configuration weakness and "
                                "corrects the cookie settings."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "An Unusual Authenticated Session",
                        "content": (
                            "An application records unexpected activity associated "
                            "with an existing session. The team reviews session "
                            "logs, invalidates affected sessions when appropriate, "
                            "and checks cookie handling and transport security."
                        ),
                        "discussion": [
                            "Why should session identifiers be treated as secrets?",
                            "What is the purpose of session rotation after login?",
                            "When should a session be invalidated?"
                        ]
                    },
                    "simulation": {
                        "title": "Respond to Suspicious Session Activity",
                        "scenario": (
                            "A fictional security dashboard reports unusual "
                            "activity associated with a valid authenticated session."
                        ),
                        "tasks": [
                            "Review the supplied session and authentication events.",
                            "Identify whether the activity warrants further investigation.",
                            "Recommend session invalidation where justified.",
                            "Review cookie attributes and session expiration."
                        ],
                        "expected_outcome": (
                            "The learner identifies suspicious session activity "
                            "and proposes a proportionate response."
                        )
                    },
                    "practical_lab": {
                        "title": "Harden Web Session Management",
                        "mode": "defensive",
                        "steps": [
                            "Review a local application's session configuration.",
                            "Enable HttpOnly and Secure cookie attributes where appropriate.",
                            "Configure suitable SameSite behavior.",
                            "Rotate session identifiers after authentication or privilege changes.",
                            "Verify expiration and logout invalidation."
                        ],
                        "expected_result": (
                            "A session configuration that reduces exposure and "
                            "prevents unnecessary reuse of old sessions."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What should happen to a user's session after logout?",
                            "options": [
                                "It should remain valid indefinitely",
                                "It should be invalidated by the application",
                                "It should be printed in the page",
                                "It should be shared with other users"
                            ],
                            "answer": 1,
                            "explanation": (
                                "Logout should invalidate the session so the "
                                "previous authenticated session cannot be reused."
                            )
                        }
                    ],
                    "prevention": [
                        "Use HTTPS throughout authenticated sessions.",
                        "Set Secure, HttpOnly, and suitable SameSite cookie attributes.",
                        "Rotate session identifiers after login and privilege changes.",
                        "Apply appropriate idle and absolute session timeouts.",
                        "Invalidate sessions during logout and incident response.",
                        "Avoid exposing session identifiers in URLs or logs."
                    ],
                    "conclusion": (
                        "Secure cookie handling, session rotation, expiration, "
                        "and invalidation help protect authenticated sessions."
                    )
                }
            }
        },

        "access_control_and_file_attacks": {
            "id": "access-control-and-file-attacks",
            "name": "Access Control and File Handling Attacks",
            "description": (
                "Threats caused by missing authorization checks and unsafe "
                "handling of uploaded files or requested resources."
            ),
            "types": {
                "broken_access_control": {
                    "id": "broken-access-control",
                    "name": "Broken Access Control",
                    "overview": (
                        "Broken access control occurs when an application fails "
                        "to enforce the permissions required for a resource or "
                        "action. A user may access another person's information "
                        "or perform an operation beyond their role."
                    ),
                    "how_it_works": [
                        "A user requests a resource or operation.",
                        "The application fails to verify the user's permissions for that specific resource.",
                        "The application returns protected data or performs an unauthorized action.",
                        "Server-side authorization checks enforce access rules on every relevant request."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Accessing Another User's Record",
                            "content": (
                                "A fictional portal uses a record identifier from "
                                "the URL but does not verify ownership. A user "
                                "could potentially view a record belonging to "
                                "someone else."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "The Missing Ownership Check",
                        "content": (
                            "A security assessment finds that a customer endpoint "
                            "checks whether a user is logged in but does not verify "
                            "whether the requested record belongs to that user. "
                            "Developers add server-side ownership checks and test "
                            "different user roles."
                        ),
                        "discussion": [
                            "Why is authentication different from authorization?",
                            "Why should authorization be enforced on the server?",
                            "How can automated tests check access between user accounts?"
                        ]
                    },
                    "simulation": {
                        "title": "Review Resource Permissions",
                        "scenario": (
                            "A fictional application has customer, staff, and "
                            "administrator roles with different permissions."
                        ),
                        "tasks": [
                            "Review a table of requested actions and user roles.",
                            "Identify actions that exceed a user's permissions.",
                            "Recommend server-side authorization checks.",
                            "Define tests for resource ownership and role boundaries."
                        ],
                        "expected_outcome": (
                            "The learner identifies unauthorized access and "
                            "recommends appropriate permission enforcement."
                        )
                    },
                    "practical_lab": {
                        "title": "Implement Resource-Level Authorization",
                        "mode": "defensive",
                        "steps": [
                            "Review a local endpoint that retrieves a user-owned record.",
                            "Identify whether the endpoint checks authentication and authorization.",
                            "Add a server-side ownership or role check.",
                            "Test access using two separate test accounts.",
                            "Verify that unauthorized requests are denied."
                        ],
                        "expected_result": (
                            "Users can access only resources and operations "
                            "permitted by their assigned privileges."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the difference between authentication and authorization?",
                            "options": [
                                "Authentication verifies identity; authorization checks permissions",
                                "They always mean exactly the same thing",
                                "Authorization verifies screen resolution",
                                "Authentication determines database table size"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Authentication identifies the user, while "
                                "authorization determines what that user may do."
                            )
                        }
                    ],
                    "prevention": [
                        "Enforce authorization on the server for every protected operation.",
                        "Check resource ownership as well as user identity.",
                        "Apply least privilege and deny access by default.",
                        "Avoid relying on hidden buttons or client-side checks for security.",
                        "Test access boundaries across users and roles.",
                        "Log and investigate suspicious authorization failures."
                    ],
                    "conclusion": (
                        "Consistent server-side authorization prevents users from "
                        "accessing resources or actions beyond their permissions."
                    )
                },

                "unrestricted_file_upload": {
                    "id": "unrestricted-file-upload",
                    "name": "Unrestricted File Upload",
                    "overview": (
                        "Unrestricted file upload occurs when an application "
                        "accepts files without adequate validation, storage "
                        "controls, or restrictions on how the files can be accessed. "
                        "Malicious files may expose users or the server to risk."
                    ),
                    "how_it_works": [
                        "An application accepts a file from a user.",
                        "Validation or storage restrictions are incomplete.",
                        "An unsafe file may be stored, served, or processed in an unintended way.",
                        "Strict validation and isolated storage reduce the risk."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Unsafe Profile Image Upload",
                            "content": (
                                "A fictional website checks only the uploaded "
                                "filename when accepting profile pictures. A review "
                                "finds that the server should also verify file "
                                "content, size, and storage behavior."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Securing a Document Upload Portal",
                        "content": (
                            "A company discovers that its document portal accepts "
                            "file types that were never intended to be processed. "
                            "The team restricts permitted formats, validates file "
                            "content, isolates storage, and reviews existing uploads."
                        ),
                        "discussion": [
                            "Why is a filename extension not sufficient validation?",
                            "Why should uploaded files be stored outside executable web directories?",
                            "When should uploaded files be scanned?"
                        ]
                    },
                    "simulation": {
                        "title": "Evaluate an Uploaded File",
                        "scenario": (
                            "A fictional portal receives several documents, "
                            "including oversized files and files with mismatched "
                            "extensions and content types."
                        ),
                        "tasks": [
                            "Compare each file with the portal's allowed formats.",
                            "Identify mismatched or oversized files.",
                            "Choose safe rejection and logging behavior.",
                            "Recommend isolated storage and content scanning."
                        ],
                        "expected_outcome": (
                            "The learner identifies unsafe uploads and recommends "
                            "a controlled file-handling process."
                        )
                    },
                    "practical_lab": {
                        "title": "Implement Safe File Upload Validation",
                        "mode": "defensive",
                        "steps": [
                            "Review a local training application's upload handler.",
                            "Define an allowlist of permitted file formats.",
                            "Validate file size and inspect file content where practical.",
                            "Generate safe server-side filenames and isolate storage.",
                            "Test invalid files and verify that rejected files cannot be accessed."
                        ],
                        "expected_result": (
                            "A file-upload workflow that validates content and "
                            "stores accepted files safely."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Why is checking only a file extension insufficient?",
                            "options": [
                                "The extension can disagree with the file's actual content",
                                "Extensions always guarantee file safety",
                                "It automatically scans every file",
                                "It prevents oversized uploads automatically"
                            ],
                            "answer": 0,
                            "explanation": (
                                "A filename extension can be misleading and does "
                                "not establish that a file is safe."
                            )
                        }
                    ],
                    "prevention": [
                        "Allow only file types required by the application.",
                        "Validate file content rather than trusting extensions alone.",
                        "Set appropriate upload size and request limits.",
                        "Use generated filenames and safe storage locations.",
                        "Keep uploaded files outside executable web directories where possible.",
                        "Scan files when appropriate and restrict access to stored uploads."
                    ],
                    "conclusion": (
                        "Strict file validation, isolated storage, and controlled "
                        "access reduce risks from uploaded files."
                    )
                }
            }
        },

        "server_configuration_and_availability": {
            "id": "server-configuration-and-availability",
            "name": "Server Configuration and Availability Attacks",
            "description": (
                "Threats involving insecure server settings, exposed resources, "
                "or excessive requests that affect application availability."
            ),
            "types": {
                "security_misconfiguration": {
                    "id": "security-misconfiguration",
                    "name": "Security Misconfiguration",
                    "overview": (
                        "Security misconfiguration occurs when servers, frameworks, "
                        "applications, or cloud services use unsafe settings. "
                        "Examples include debug mode in production, default "
                        "credentials, unnecessary services, and exposed error details."
                    ),
                    "how_it_works": [
                        "A server or application is deployed with unsafe or unnecessary settings.",
                        "An external user discovers an exposed service, default account, or detailed error.",
                        "The weakness may reveal information or provide an opportunity for unauthorized access.",
                        "Secure baselines, configuration reviews, and patching reduce exposure."
                    ],
                    "real_world_examples": [
                        {
                            "title": "Debug Mode Left Enabled",
                            "content": (
                                "A fictional website is deployed with debugging "
                                "features enabled. Error pages expose internal "
                                "implementation details, so administrators disable "
                                "debug mode and review logs for sensitive disclosures."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "A Production Server Exposes Internal Details",
                        "content": (
                            "A routine security review finds that a production "
                            "server displays detailed error messages and runs "
                            "unnecessary services. The team applies a hardened "
                            "configuration, removes unused services, and verifies "
                            "that sensitive diagnostics are no longer public."
                        ),
                        "discussion": [
                            "Why should debug mode be disabled in production?",
                            "How do default credentials increase risk?",
                            "Why should configuration changes be tested before deployment?"
                        ]
                    },
                    "simulation": {
                        "title": "Audit a Server Configuration",
                        "scenario": (
                            "A fictional configuration report lists debug mode, "
                            "a default account, outdated software, and unused services."
                        ),
                        "tasks": [
                            "Identify the highest-priority configuration weaknesses.",
                            "Recommend secure production settings.",
                            "Prioritize software updates and removal of unnecessary services.",
                            "Create a verification checklist."
                        ],
                        "expected_outcome": (
                            "The learner produces a prioritized server-hardening plan."
                        )
                    },
                    "practical_lab": {
                        "title": "Production Configuration Hardening",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied server configuration report.",
                            "Identify debug settings, default credentials, and unnecessary services.",
                            "Apply secure settings in a local training environment.",
                            "Confirm that detailed errors are logged privately rather than exposed publicly.",
                            "Recheck the configuration against a security baseline."
                        ],
                        "expected_result": (
                            "A hardened configuration with unnecessary exposure removed."
                        )
                    },
                    "assessment": [
                        {
                            "question": "Which configuration is inappropriate for a production web application?",
                            "options": [
                                "Debug mode exposed to ordinary users",
                                "Current security updates",
                                "Restricted administrative access",
                                "Generic public error messages"
                            ],
                            "answer": 0,
                            "explanation": (
                                "Production debug output can disclose internal "
                                "details and should not be exposed to ordinary users."
                            )
                        }
                    ],
                    "prevention": [
                        "Disable debug mode and verbose public errors in production.",
                        "Remove default credentials and unnecessary services.",
                        "Apply security updates promptly.",
                        "Use documented secure configuration baselines.",
                        "Restrict administrative interfaces and management ports.",
                        "Review configuration changes and monitor for drift."
                    ],
                    "conclusion": (
                        "Secure deployment settings, regular reviews, and timely "
                        "updates reduce risks caused by misconfiguration."
                    )
                },

                "denial_of_service": {
                    "id": "denial-of-service",
                    "name": "Denial-of-Service (DoS)",
                    "overview": (
                        "A denial-of-service attack attempts to make a website "
                        "or service unavailable by exhausting bandwidth, connection "
                        "capacity, processing time, or another limited resource. "
                        "Distributed attacks may involve many systems."
                    ),
                    "how_it_works": [
                        "A service has finite processing, connection, or bandwidth capacity.",
                        "Excessive or expensive requests consume available resources.",
                        "Legitimate users experience slow responses or failed requests.",
                        "Rate limiting, caching, capacity planning, and upstream protection reduce impact."
                    ],
                    "real_world_examples": [
                        {
                            "title": "An Overloaded Booking Website",
                            "content": (
                                "A fictional booking service experiences a sudden "
                                "surge in requests and becomes slow. The operations "
                                "team examines traffic patterns, application "
                                "performance, and upstream network capacity before "
                                "selecting appropriate mitigation."
                            )
                        }
                    ],
                    "case_study": {
                        "title": "Restoring an Unavailable Service",
                        "content": (
                            "A web application becomes intermittently unavailable "
                            "during an unusual traffic spike. The team compares "
                            "request rates with normal usage, checks expensive "
                            "endpoints, enables appropriate rate limits, and "
                            "coordinates with its hosting provider."
                        ),
                        "discussion": [
                            "How can legitimate traffic spikes resemble an attack?",
                            "Why should mitigation consider both application and network capacity?",
                            "What information helps distinguish a DoS event from an application failure?"
                        ]
                    },
                    "simulation": {
                        "title": "Respond to a Traffic Surge",
                        "scenario": (
                            "A fictional monitoring dashboard shows rising request "
                            "rates, increased latency, and growing server resource use."
                        ),
                        "tasks": [
                            "Compare current traffic with the established baseline.",
                            "Identify the endpoints experiencing the greatest load.",
                            "Recommend safe rate limits and caching where appropriate.",
                            "Define recovery and post-incident review steps."
                        ],
                        "expected_outcome": (
                            "The learner identifies availability risks and proposes "
                            "proportionate defensive mitigation."
                        )
                    },
                    "practical_lab": {
                        "title": "Analyze Availability Metrics",
                        "mode": "defensive",
                        "steps": [
                            "Review a supplied set of request-rate, latency, and resource metrics.",
                            "Identify when service performance deteriorates.",
                            "Compare traffic patterns with normal operating levels.",
                            "Recommend rate limits, caching, and capacity improvements.",
                            "Prepare a recovery and monitoring checklist."
                        ],
                        "expected_result": (
                            "An availability incident report with evidence-based "
                            "mitigation recommendations."
                        )
                    },
                    "assessment": [
                        {
                            "question": "What is the main objective of a DoS attack?",
                            "options": [
                                "To make a service unavailable to legitimate users",
                                "To improve the application's usability",
                                "To increase storage capacity",
                                "To update server software"
                            ],
                            "answer": 0,
                            "explanation": (
                                "DoS attacks attempt to disrupt service availability "
                                "by exhausting or obstructing resources."
                            )
                        }
                    ],
                    "prevention": [
                        "Use rate limiting and request-size limits.",
                        "Apply caching and optimize expensive endpoints.",
                        "Monitor traffic, latency, and resource consumption.",
                        "Use suitable CDN, hosting-provider, or upstream DDoS protection.",
                        "Maintain capacity plans and an availability response procedure.",
                        "Test resilience in authorized environments."
                    ],
                    "conclusion": (
                        "Layered monitoring, capacity planning, and traffic controls "
                        "help maintain web application availability."
                    )
                }
            }
        }
    }
}