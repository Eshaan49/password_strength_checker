# 🔐 Password Strength & Breach Checker

A Python-based cybersecurity tool that evaluates password strength, estimates password entropy, and checks whether a password has been exposed in known data breaches using the Have I Been Pwned (HIBP) API.

This project demonstrates practical security concepts including password auditing, entropy analysis, secure API usage, SHA-1 hashing, and breach intelligence integration.

---

## 🚀 Features

### Password Strength Analysis
- Evaluates password complexity
- Checks for:
  - Minimum length requirements
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Generates actionable security recommendations

### Entropy Estimation
- Estimates password entropy in bits
- Provides a realistic indication of password resistance against brute-force attacks

### Breach Detection
- Checks passwords against the Have I Been Pwned Passwords database
- Uses the secure k-Anonymity model
- Passwords are never transmitted directly to the API

### Security Reporting
- Generates a clear security assessment report
- Displays:
  - Strength Score
  - Security Level
  - Entropy Score
  - Recommendations
  - Breach Status

### User-Friendly CLI Interface
- Colorized terminal output using Colorama
- Easy-to-read security reports

---

## 🛠 Technologies Used

- Python 3
- Requests
- Colorama
- SHA-1 Hashing
- Have I Been Pwned API

---

## 📂 Project Structure

```text
password_strength_checker/
│
├── main.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Eshaan49/password_strength_checker.git
cd password_strength_checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Enter a password when prompted.

---

## 📊 Sample Output

```text
🔐 Password Strength & Breach Checker 🔐

Enter a password to check: Ragnarok4!

=============================================
PASSWORD SECURITY REPORT
=============================================

Strength Score : 4/5
Strength Level : Strong
Entropy Score  : 47.0 bits

Recommendations:
- Password should be at least 12 characters long.

❌ This password has been found in 16 breaches!
```

---

## 🔒 Security Concepts Demonstrated

- Password Security Assessment
- Entropy-Based Analysis
- Breach Intelligence
- SHA-1 Hashing
- Secure API Consumption
- Defensive Security Practices
- Python Automation

---

## ⚠️ Limitations

- Entropy values are estimates and not exact attack-cost calculations
- Requires internet connectivity for breach verification
- Focused on password assessment rather than password generation

---

## 🎯 Future Enhancements

- Password History Analysis
- Export Security Reports
- GUI Version (Tkinter / PyQt)
- Batch Password Auditing
- Enterprise Password Policy Checks

---

## 👨‍💻 Author

**Eshaan Pilar**

Cybersecurity Undergraduate | Python Security Tool Development | SOC & SIEM Enthusiast

GitHub: https://github.com/Eshaan49

---

## Disclaimer

This project was developed for educational and defensive cybersecurity purposes only. It is intended to promote better password security awareness and secure password practices.
