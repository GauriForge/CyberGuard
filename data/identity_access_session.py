
IDENTITY_ACCESS_SESSION = {
    "id": "identity-access-session",
    "name": "Identity, Access and Session Attacks",
    "description": "Attacks that exploit weaknesses in identity verification, authentication, authorisation and session management.",

    "subcategories": {
        "authentication_attacks": {
            "id": "authentication-attacks",
            "name": "Authentication Attacks",
            "description": "Attacks that target the methods used to verify a user's identity.",

            "types": {
                "credential_stuffing": {
                    "id": "credential-stuffing",
                    "name": "Credential Stuffing",

                    "overview": "Credential stuffing occurs when attackers use username and password combinations exposed in previous data breaches to attempt access to other accounts. It takes advantage of people reusing passwords across different services.",

                    "how_it_works": [
                        "Login credentials are exposed through a previous breach or obtained from another source.",
                        "Attackers attempt to reuse those credentials on other websites.",
                        "Automated tools may submit many login attempts across multiple accounts.",
                        "Accounts using the same password on multiple services may be compromised."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Reused passwords across online services",
                            "description": "A person uses the same password for an online shopping account and an email account. If the shopping service suffers a breach, attackers may try the exposed credentials against the email service."
                        }
                    ],

                    "case_study": {
                        "title": "The Reused Password Incident",
                        "scenario": "A company notices unusual login attempts against employee accounts. An investigation finds that several employees reused passwords from personal websites that had previously suffered data breaches.",
                        "findings": [
                            "Several login attempts originated from unfamiliar locations.",
                            "Multiple accounts used passwords previously exposed elsewhere.",
                            "Some accounts lacked multi-factor authentication."
                        ],
                        "lesson": "Unique passwords, multi-factor authentication and monitoring unusual login activity reduce the impact of credential stuffing."
                    },

                    "simulation": {
                        "title": "Identify a Credential Stuffing Attempt",
                        "scenario": "A login monitoring dashboard shows repeated sign-in attempts against several accounts using credentials associated with previous breaches.",
                        "tasks": [
                            "Identify the repeated login pattern.",
                            "Determine which accounts require additional verification.",
                            "Recommend appropriate account protection measures."
                        ],
                        "expected_learning": "Recognise repeated authentication attempts and explain how breached credentials can threaten unrelated accounts."
                    },

                    "practical_lab": {
                        "title": "Credential Stuffing Detection Lab",
                        "objective": "Identify suspicious authentication patterns using fictional login records.",
                        "activities": [
                            "Review a sample log containing successful and failed logins.",
                            "Identify repeated attempts against multiple accounts.",
                            "Flag unusual login patterns for investigation.",
                            "Recommend protective controls."
                        ],
                        "safety": "Use only fictional records in a local learning environment. Do not test credentials against real accounts or services."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What makes credential stuffing effective?",
                                "options": [
                                    "Users reuse passwords across services",
                                    "Websites always store passwords in plain text",
                                    "Attackers physically access every computer",
                                    "Every login automatically bypasses authentication"
                                ],
                                "answer": "Users reuse passwords across services",
                                "explanation": "Previously exposed credentials may work on another service when a person reuses the same password."
                            },
                            {
                                "question": "Which measure most directly reduces the risk of password reuse?",
                                "options": [
                                    "Using unique passwords for every account",
                                    "Disabling account notifications",
                                    "Sharing passwords with colleagues",
                                    "Using the same password with more symbols"
                                ],
                                "answer": "Using unique passwords for every account",
                                "explanation": "Unique passwords prevent a password exposed on one service from automatically unlocking another."
                            }
                        ]
                    },

                    "prevention": [
                        "Use a unique, strong password for each account.",
                        "Use a reputable password manager.",
                        "Enable multi-factor authentication.",
                        "Apply rate limiting and risk-based authentication.",
                        "Monitor unusual login patterns and alert users to suspicious activity."
                    ],

                    "conclusion": "Credential stuffing demonstrates why password reuse is dangerous. Unique passwords, multi-factor authentication and appropriate monitoring make accounts more resilient."
                },

                "brute_force_attack": {
                    "id": "brute-force-attack",
                    "name": "Brute-Force Attack",

                    "overview": "A brute-force attack attempts to discover a password by trying possible combinations until a correct one is found. Its effectiveness depends on factors such as password strength, available time and the protections applied by the authentication system.",

                    "how_it_works": [
                        "An attacker identifies an account or authentication system.",
                        "Multiple possible passwords are attempted.",
                        "Weak passwords may be discovered more easily than long, unpredictable ones.",
                        "Account protections may detect or block repeated failures."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Repeated attempts against an exposed account",
                            "description": "A publicly accessible login service receives a large number of failed attempts against an account with a weak password. Monitoring alerts the security team to the unusual activity."
                        }
                    ],

                    "case_study": {
                        "title": "The Weak Administrator Password",
                        "scenario": "A small organisation discovers repeated failed sign-ins to an administrative account. The account uses a short password and has no additional authentication factor.",
                        "findings": [
                            "The account was accessible over a public network.",
                            "Repeated failed attempts were not adequately monitored.",
                            "The password was too easy to guess."
                        ],
                        "lesson": "Strong authentication, restricted administrative access and login protections help prevent password guessing."
                    },

                    "simulation": {
                        "title": "Review Failed Login Events",
                        "scenario": "A fictional security log records dozens of failed login attempts against one account within a short period.",
                        "tasks": [
                            "Identify the unusual number of failures.",
                            "Distinguish suspicious activity from an isolated typing error.",
                            "Recommend suitable defensive actions."
                        ],
                        "expected_learning": "Recognise password-guessing patterns and explain how authentication controls limit them."
                    },

                    "practical_lab": {
                        "title": "Brute-Force Detection Lab",
                        "objective": "Analyse fictional authentication logs to identify repeated password guessing.",
                        "activities": [
                            "Inspect timestamps and authentication results.",
                            "Identify accounts with unusually frequent failures.",
                            "Configure or propose an appropriate alert threshold.",
                            "Document recommended account protections."
                        ],
                        "safety": "Use simulated logs or an isolated local training application. Do not run password-guessing tools against real systems."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is the main characteristic of a brute-force attack?",
                                "options": [
                                    "Repeatedly trying possible passwords",
                                    "Encrypting every network connection",
                                    "Creating backups of all files",
                                    "Updating a computer's operating system"
                                ],
                                "answer": "Repeatedly trying possible passwords",
                                "explanation": "Brute-force attacks attempt possible password combinations until a match is found or attempts are stopped."
                            },
                            {
                                "question": "Which control can help limit repeated password guessing?",
                                "options": [
                                    "Rate limiting and login attempt controls",
                                    "Removing all authentication logs",
                                    "Making administrator accounts public",
                                    "Reusing a single password"
                                ],
                                "answer": "Rate limiting and login attempt controls",
                                "explanation": "These controls limit repeated attempts and can help identify suspicious authentication activity."
                            }
                        ]
                    },

                    "prevention": [
                        "Use long, unpredictable passwords.",
                        "Enable multi-factor authentication.",
                        "Apply rate limiting and carefully designed lockout protections.",
                        "Monitor failed authentication attempts.",
                        "Restrict administrative login access."
                    ],

                    "conclusion": "Brute-force attacks exploit weak or inadequately protected authentication. Strong passwords and layered login controls reduce their likelihood of success."
                },

                "password_spraying": {
                    "id": "password-spraying",
                    "name": "Password Spraying",

                    "overview": "Password spraying involves trying a small number of commonly used passwords against many accounts. Unlike attacks that repeatedly target one account, this approach attempts to avoid account lockout controls by spreading attempts across users.",

                    "how_it_works": [
                        "An attacker identifies multiple account names.",
                        "A commonly used password is attempted against several accounts.",
                        "Attempts may be distributed over time.",
                        "Weak accounts may be exposed if monitoring and authentication controls are inadequate."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Unusual sign-ins across employee accounts",
                            "description": "A security team detects failed sign-ins against many employee accounts using a similar pattern. The investigation identifies password spraying as a possible explanation."
                        }
                    ],

                    "case_study": {
                        "title": "The Organisation-Wide Login Alert",
                        "scenario": "A company receives authentication alerts for many employee accounts. Each account has only a few failed attempts, but the combined pattern is unusual.",
                        "findings": [
                            "Failures were distributed across numerous accounts.",
                            "Attempts occurred within a related time window.",
                            "Several users had weak or commonly used passwords."
                        ],
                        "lesson": "Security monitoring should examine patterns across accounts, not just repeated failures against an individual account."
                    },

                    "simulation": {
                        "title": "Spot the Distributed Pattern",
                        "scenario": "Review a fictional log showing a small number of failed logins for many different users.",
                        "tasks": [
                            "Compare failures across accounts.",
                            "Identify shared timing or source patterns.",
                            "Recommend an appropriate security response."
                        ],
                        "expected_learning": "Distinguish password spraying from repeated password guessing against a single account."
                    },

                    "practical_lab": {
                        "title": "Password Spraying Log Analysis",
                        "objective": "Identify suspicious login patterns distributed across multiple fictional accounts.",
                        "activities": [
                            "Group failed logins by time and account.",
                            "Look for related patterns across users.",
                            "Prepare an incident summary.",
                            "Recommend stronger authentication controls."
                        ],
                        "safety": "Perform analysis on fictional logs only. Do not attempt authentication against real users or services."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "How does password spraying differ from a typical brute-force attack?",
                                "options": [
                                    "It tries a small number of passwords across many accounts",
                                    "It only targets encrypted files",
                                    "It requires physical access to every account",
                                    "It automatically disables multi-factor authentication"
                                ],
                                "answer": "It tries a small number of passwords across many accounts",
                                "explanation": "Password spraying distributes attempts across accounts rather than concentrating many guesses on one account."
                            },
                            {
                                "question": "What is useful when detecting password spraying?",
                                "options": [
                                    "Correlating authentication failures across accounts",
                                    "Checking only one user's password",
                                    "Deleting all login history",
                                    "Disabling security alerts"
                                ],
                                "answer": "Correlating authentication failures across accounts",
                                "explanation": "The distributed pattern may only become apparent when events from multiple accounts are analysed together."
                            }
                        ]
                    },

                    "prevention": [
                        "Block or screen commonly used passwords.",
                        "Enable multi-factor authentication.",
                        "Monitor authentication events across multiple accounts.",
                        "Apply risk-based access controls.",
                        "Investigate unusual sign-in patterns and protect affected accounts."
                    ],

                    "conclusion": "Password spraying can evade controls that focus on a single account. Cross-account monitoring and strong authentication help identify and prevent it."
                }
            }
        },

        "authorization_and_privilege_attacks": {
            "id": "authorization-and-privilege-attacks",
            "name": "Authorisation and Privilege Attacks",
            "description": "Attacks that exploit weaknesses in permissions, access restrictions or privilege management.",

            "types": {
                "privilege_escalation": {
                    "id": "privilege-escalation",
                    "name": "Privilege Escalation",

                    "overview": "Privilege escalation occurs when a user or process gains permissions beyond those it is intended to have. It may be vertical, such as gaining administrator privileges, or horizontal, such as accessing another user's resources.",

                    "how_it_works": [
                        "An attacker or unauthorised process obtains an initial level of access.",
                        "A weakness in permissions, software or configuration is identified.",
                        "The weakness is abused to obtain additional privileges.",
                        "Sensitive resources may become accessible if the issue is not contained."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Over-Privileged Application",
                            "description": "An application service runs with administrator-level permissions even though it only needs access to a limited set of files. A software vulnerability could therefore have a much greater impact."
                        }
                    ],

                    "case_study": {
                        "title": "Excessive Permissions in a Business Application",
                        "scenario": "During a security review, an organisation discovers that a routine application account can modify system settings that should be restricted to administrators.",
                        "findings": [
                            "The application account had unnecessary permissions.",
                            "Access controls were not reviewed regularly.",
                            "The potential impact extended beyond the application's intended role."
                        ],
                        "lesson": "Least privilege, timely patching and regular permission reviews reduce the risk of privilege escalation."
                    },

                    "simulation": {
                        "title": "Review a Permission Configuration",
                        "scenario": "A fictional access-control report shows an ordinary application account with permissions to modify protected settings.",
                        "tasks": [
                            "Identify permissions that exceed the account's purpose.",
                            "Determine which resources should be restricted.",
                            "Recommend corrective permissions and monitoring."
                        ],
                        "expected_learning": "Recognise excessive privileges and explain how least-privilege controls reduce risk."
                    },

                    "practical_lab": {
                        "title": "Least-Privilege Review Lab",
                        "objective": "Audit a sample permission table and identify excessive access.",
                        "activities": [
                            "Review fictional users, roles and permissions.",
                            "Compare granted permissions with job responsibilities.",
                            "Propose a least-privilege permission model.",
                            "Record the changes required for remediation."
                        ],
                        "safety": "Use a mock permission table or an isolated training system. Do not attempt to gain elevated access on systems without explicit authorisation."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is privilege escalation?",
                                "options": [
                                    "Gaining permissions beyond those intended",
                                    "Changing a website's colour scheme",
                                    "Creating a routine backup",
                                    "Reducing an account's access rights"
                                ],
                                "answer": "Gaining permissions beyond those intended",
                                "explanation": "Privilege escalation increases the level of access available to a user or process."
                            },
                            {
                                "question": "Which principle helps reduce privilege escalation risk?",
                                "options": [
                                    "Least privilege",
                                    "Shared administrator accounts",
                                    "Permanent unrestricted access",
                                    "Disabling software updates"
                                ],
                                "answer": "Least privilege",
                                "explanation": "Least privilege grants only the access required for a specific role or task."
                            }
                        ]
                    },

                    "prevention": [
                        "Apply the principle of least privilege.",
                        "Patch operating systems and applications promptly.",
                        "Review role assignments and permissions regularly.",
                        "Monitor sensitive administrative actions.",
                        "Separate routine accounts from administrative accounts."
                    ],

                    "conclusion": "Privilege escalation can turn a limited compromise into a serious incident. Careful permissions, patching and monitoring help limit its impact."
                },

                "broken_access_control": {
                    "id": "broken-access-control",
                    "name": "Broken Access Control",

                    "overview": "Broken access control occurs when an application fails to enforce the restrictions that determine which users may view or modify particular resources. A user may be able to access information or functions outside their authorised role.",

                    "how_it_works": [
                        "An application exposes a resource or action.",
                        "The application fails to verify the user's permissions correctly.",
                        "A user attempts to access a resource outside their authorised scope.",
                        "The missing or incorrect permission check may allow unauthorised access."
                    ],

                    "real_world_examples": [
                        {
                            "title": "Accessing Another User's Record",
                            "description": "A customer portal uses a record identifier in its URL but does not verify that the signed-in customer owns the requested record."
                        }
                    ],

                    "case_study": {
                        "title": "The Customer Record Exposure",
                        "scenario": "A business discovers that a logged-in customer can view a different customer's order by changing a record identifier in a test environment.",
                        "findings": [
                            "The application checked whether the user was logged in.",
                            "It did not consistently verify ownership of the requested record.",
                            "Sensitive customer information could be exposed."
                        ],
                        "lesson": "Authentication alone is not sufficient; every protected resource must also have appropriate authorisation checks."
                    },

                    "simulation": {
                        "title": "Test an Access-Control Matrix",
                        "scenario": "A fictional application defines customer, support and administrator roles. A test report shows that a customer can access a record assigned to another customer.",
                        "tasks": [
                            "Identify the incorrect access decision.",
                            "Determine which roles should access the record.",
                            "Specify the required server-side authorisation check."
                        ],
                        "expected_learning": "Understand the difference between authentication and authorisation."
                    },

                    "practical_lab": {
                        "title": "Access-Control Testing Lab",
                        "objective": "Review a mock application permission matrix and identify missing access checks.",
                        "activities": [
                            "List resources and their authorised roles.",
                            "Compare expected and actual access decisions.",
                            "Document unauthorised access scenarios.",
                            "Recommend server-side access checks."
                        ],
                        "safety": "Use a mock application or an authorised local training environment. Do not access other people's real accounts or records."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What is the difference between authentication and authorisation?",
                                "options": [
                                    "Authentication verifies identity; authorisation checks permitted actions",
                                    "They are exactly the same process",
                                    "Authorisation verifies identity; authentication grants every permission",
                                    "Neither process is related to access control"
                                ],
                                "answer": "Authentication verifies identity; authorisation checks permitted actions",
                                "explanation": "A user can be correctly authenticated but still lack permission to access a particular resource."
                            },
                            {
                                "question": "Where should sensitive resource permissions be enforced?",
                                "options": [
                                    "On the server for each protected resource and action",
                                    "Only by hiding buttons in the interface",
                                    "Only in a page title",
                                    "Only through the browser's appearance settings"
                                ],
                                "answer": "On the server for each protected resource and action",
                                "explanation": "Client-side interface restrictions can be bypassed, so the server must enforce access control."
                            }
                        ]
                    },

                    "prevention": [
                        "Enforce server-side authorisation on every protected request.",
                        "Verify resource ownership and role permissions.",
                        "Use deny-by-default access policies.",
                        "Test access controls across different user roles.",
                        "Log and investigate suspicious access attempts."
                    ],

                    "conclusion": "Broken access control can expose information even when users have valid accounts. Explicit server-side permission checks are essential for protecting resources."
                }
            }
        },

        "session_management_attacks": {
            "id": "session-management-attacks",
            "name": "Session Management Attacks",
            "description": "Attacks that exploit weaknesses in the creation, storage, validation or termination of authenticated sessions.",

            "types": {
                "session_hijacking": {
                    "id": "session-hijacking",
                    "name": "Session Hijacking",

                    "overview": "Session hijacking occurs when an attacker obtains or misuses a valid session token to act as an authenticated user. If a session token is stolen, the attacker may be able to bypass the normal login process until the session expires or is revoked.",

                    "how_it_works": [
                        "A user signs in and receives a session identifier.",
                        "The session identifier is exposed through an insecure implementation or compromised device.",
                        "An unauthorised party obtains the token.",
                        "The token may be reused to impersonate the user if the server does not detect or prevent the misuse."
                    ],

                    "real_world_examples": [
                        {
                            "title": "An Exposed Web Session",
                            "description": "A poorly secured application allows a session identifier to be exposed. An attacker who obtains the identifier may attempt to reuse the session without knowing the user's password."
                        }
                    ],

                    "case_study": {
                        "title": "The Reused Session Token",
                        "scenario": "A security team investigates suspicious activity on an account. The investigation finds that a session remained active after a user believed they had signed out on a shared device.",
                        "findings": [
                            "Session termination did not work as expected.",
                            "The session lifetime was longer than necessary.",
                            "The application lacked adequate session monitoring."
                        ],
                        "lesson": "Secure session cookies, server-side invalidation and appropriate session lifetimes help prevent session misuse."
                    },

                    "simulation": {
                        "title": "Review Session Security Events",
                        "scenario": "A fictional application log shows a session being used from an unexpected environment after the original user signed out.",
                        "tasks": [
                            "Identify the unusual session activity.",
                            "Determine whether the session should remain valid.",
                            "Recommend token invalidation and further investigation."
                        ],
                        "expected_learning": "Understand how exposed or improperly terminated sessions can be misused."
                    },

                    "practical_lab": {
                        "title": "Session Lifecycle Review Lab",
                        "objective": "Evaluate session creation, expiration and termination using a mock application.",
                        "activities": [
                            "Review the application's session lifecycle.",
                            "Check the expected behaviour after logout.",
                            "Review cookie security settings.",
                            "Document improvements to session expiration and revocation."
                        ],
                        "safety": "Use a local mock application with fictional accounts. Never capture or reuse real users' session tokens."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "What may an attacker do with a stolen valid session token?",
                                "options": [
                                    "Attempt to impersonate the authenticated user",
                                    "Automatically repair the application",
                                    "Guarantee access to every system",
                                    "Change the user's hardware"
                                ],
                                "answer": "Attempt to impersonate the authenticated user",
                                "explanation": "A stolen session token may allow impersonation while the session remains valid and usable."
                            },
                            {
                                "question": "What should happen when a user logs out?",
                                "options": [
                                    "The application should invalidate the relevant session",
                                    "The session should remain permanently valid",
                                    "The password should be displayed",
                                    "All security logging should stop"
                                ],
                                "answer": "The application should invalidate the relevant session",
                                "explanation": "Proper server-side session invalidation prevents continued use of a terminated session."
                            }
                        ]
                    },

                    "prevention": [
                        "Use HTTPS throughout authenticated sessions.",
                        "Set appropriate Secure, HttpOnly and SameSite cookie attributes.",
                        "Generate unpredictable session identifiers.",
                        "Invalidate sessions on logout and when compromise is suspected.",
                        "Use suitable session timeouts and monitor unusual session activity."
                    ],

                    "conclusion": "Session hijacking targets the trust established after login. Secure token handling, session invalidation and monitoring help protect authenticated users."
                },

                "session_fixation": {
                    "id": "session-fixation",
                    "name": "Session Fixation",

                    "overview": "Session fixation is a session-management weakness in which an attacker attempts to make a victim authenticate using a session identifier known to the attacker. If the application fails to issue a fresh session identifier after authentication, the attacker may be able to misuse that session.",

                    "how_it_works": [
                        "An application accepts a session identifier before login.",
                        "An attacker attempts to make a victim use a session identifier already known to the attacker.",
                        "The victim authenticates while the application retains the same identifier.",
                        "If the session remains usable by the attacker, the victim's authenticated session may be exposed."
                    ],

                    "real_world_examples": [
                        {
                            "title": "A Session Identifier That Never Changes",
                            "description": "A test of a fictional website shows that its session identifier remains unchanged before and after login, creating a potential session fixation weakness."
                        }
                    ],

                    "case_study": {
                        "title": "The Missing Session Rotation",
                        "scenario": "A web application review discovers that session identifiers are not regenerated after successful authentication.",
                        "findings": [
                            "Anonymous and authenticated sessions used the same identifier.",
                            "The application did not enforce session rotation.",
                            "The session lifecycle was not covered by security tests."
                        ],
                        "lesson": "Regenerating the session identifier after login prevents an attacker-controlled pre-authentication session from becoming an authenticated session."
                    },

                    "simulation": {
                        "title": "Compare Session Identifiers",
                        "scenario": "A fictional test report lists session identifiers before and after successful authentication.",
                        "tasks": [
                            "Determine whether the identifier changes after login.",
                            "Identify the potential weakness if it remains unchanged.",
                            "Recommend a secure session rotation policy."
                        ],
                        "expected_learning": "Recognise the role of session regeneration in preventing session fixation."
                    },

                    "practical_lab": {
                        "title": "Session Rotation Testing Lab",
                        "objective": "Verify that a mock application creates a fresh session after authentication.",
                        "activities": [
                            "Record the test session state before login.",
                            "Authenticate using a fictional account.",
                            "Verify that the session identifier is regenerated.",
                            "Confirm that the old session is no longer accepted where appropriate."
                        ],
                        "safety": "Perform tests only on an isolated application you own or are authorised to assess."
                    },

                    "assessment": {
                        "questions": [
                            {
                                "question": "Which behaviour helps prevent session fixation?",
                                "options": [
                                    "Regenerating the session identifier after authentication",
                                    "Keeping the same session identifier indefinitely",
                                    "Displaying session tokens in the page",
                                    "Disabling logout"
                                ],
                                "answer": "Regenerating the session identifier after authentication",
                                "explanation": "Session rotation prevents a pre-authentication identifier from simply becoming the authenticated session identifier."
                            },
                            {
                                "question": "When should an application consider rotating a session identifier?",
                                "options": [
                                    "After login and other important privilege changes",
                                    "Never after the first visit",
                                    "Only when the browser's colour changes",
                                    "Only when a user opens a public page"
                                ],
                                "answer": "After login and other important privilege changes",
                                "explanation": "Rotating session identifiers at important authentication boundaries reduces the risk of session abuse."
                            }
                        ]
                    },

                    "prevention": [
                        "Regenerate session identifiers after successful authentication.",
                        "Rotate identifiers after important privilege changes.",
                        "Invalidate the previous session identifier.",
                        "Use framework-supported session management.",
                        "Test session lifecycle behaviour during security reviews."
                    ],

                    "conclusion": "Session fixation exploits applications that fail to separate pre-authentication and authenticated sessions. Session rotation is a key defensive measure."
                }
            }
        }
    }
}