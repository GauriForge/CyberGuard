
# 🛡️ CyberGuard
### Interactive Cybersecurity Learning and Incident Management Platform

CyberGuard is a web-based cybersecurity platform designed to help users understand cybersecurity threats, develop practical security knowledge, assess their learning progress, and manage cybersecurity incidents through a centralized interface.

The project combines interactive cybersecurity education with incident reporting and administrative management.

---

## 🎯 Project Objectives

- Provide structured cybersecurity learning resources.
- Help users understand different types of cyberattacks.
- Offer practical cybersecurity labs and guided exercises.
- Evaluate cybersecurity knowledge through interactive assessments.
- Track assessment scores and learning progress.
- Allow users to report and monitor cybersecurity incidents.
- Provide administrators with tools to monitor and manage incidents.

---

## ✨ Key Features

### 1. User Authentication
- User registration and login.
- Secure password hashing.
- Session-based authentication.
- Role-based access for regular users and administrators.

### 2. User Dashboard
- Centralized dashboard.
- Overview of learning and activity.
- Recent assessments and incident activity.

### 3. Cybersecurity Learning Roadmap
- Structured learning roadmap.
- Organized cybersecurity learning topics.
- Guided progression through learning concepts.

### 4. Career Guidance
- Cybersecurity career information.
- Career paths and relevant skills.
- Guidance for exploring cybersecurity opportunities.

### 5. Attack Categories
- Organized cybersecurity attack categories.
- Information about different cyber threats.
- Educational content explaining attack concepts and defensive practices.

### 6. Practical Labs
- Interactive cybersecurity learning activities.
- Guided practical exercises.
- Opportunities to apply cybersecurity concepts.

### 7. Assessments and Results
- Multiple assessment difficulty levels.
- Attack-specific assessments.
- Interactive multiple-choice questions.
- Automatic score calculation.
- Assessment result history and performance tracking.

### 8. Incident Management
- Report cybersecurity incidents.
- View submitted incidents.
- Track incident status.
- Administrative incident management.

### 9. Learning Resources
- Centralized cybersecurity learning resources.
- Reference material for improving security knowledge.

### 10. Help Centre
- Dedicated help and support section.
- Guidance for using the platform.

### 11. Notifications
- Notification system for platform updates and activities.

### 12. User Profile
- View and update profile information.
- Change account password.

### 13. Admin Dashboard
- Separate administrator interface.
- Overview of users and incidents.
- Access to incident management features.
- Administrative access control.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python |
| Web Framework | Flask |
| Frontend | HTML5 |
| Styling | CSS3 |
| Client-side functionality | JavaScript |
| Database | SQLite |
| Database access | Python SQLite3 |
| Authentication | Flask Sessions |
| Password Security | Werkzeug Password Hashing |
| Templates | Jinja2 |
| Development Environment | Visual Studio Code |

---

## 📁 Project Structure

```text
CyberGuard/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── database/
│   └── db.py
│
├── models/
│   ├── user_model.py
│   └── assessment_model.py
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── assessments.py
│   ├── attacks.py
│   ├── incidents.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── assessments.html
│   ├── assessment_results.html
│   ├── incident_management.html
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── data/
    └── assessment_question_bank.py
```

*Note: This is an overview of the main project files and folders.*

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip
- Visual Studio Code
- Git

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd CyberGuard
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

---

## 🔐 Security Features

- Password hashing.
- Session-based authentication.
- Role-based access control.
- Protected administrative routes.
- User-specific incident access.
- Input validation.
- Environment-based application configuration.

---

## 👥 User Roles

### Regular User
- Access cybersecurity learning modules.
- Explore attack categories.
- Complete practical labs.
- Take assessments and view results.
- Report and track incidents.
- Manage profile information.

### Administrator
- Access the Admin Dashboard.
- View platform incident information.
- Monitor and manage reported incidents.
- Update incident status and severity.

---

## 🎓 Project Information

**Project Name:** CyberGuard – Interactive Cybersecurity Learning and Incident Management Platform

**Project Type:** Individual Academic Project

**Degree:** Bachelor of Computer Applications (BCA)

**Academic Year:** 2026–2027

**Developed By:** Gauri Chawla

**Project Supervisor:** Mr. Ajay Tomar

**Institution:** Gateway Institute of Engineering and Technology

---

## 🚀 Future Enhancements

- Integration with external cybersecurity threat intelligence services.
- Advanced incident analytics and reporting.
- Expanded practical cybersecurity exercises.
- Additional assessment categories.
- Enhanced notification capabilities.
- Improved security monitoring and reporting.

---

## 📌 Project Purpose

CyberGuard aims to make cybersecurity learning more accessible and interactive while providing a structured platform for cybersecurity awareness, practical learning, knowledge assessment, and incident management.

---

**CyberGuard – Learn. Practise. Assess. Protect.**
