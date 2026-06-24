import re
import math
import hashlib
import requests

# Common weak passwords
COMMON_PASSWORDS = {
    "password",
    "password123",
    "admin",
    "admin123",
    "welcome",
    "welcome123",
    "qwerty",
    "qwerty123",
    "letmein",
    "123456",
    "12345678",
    "abc123"
}


def calculate_entropy(password):
    """Calculate password entropy in bits."""

    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26

    if re.search(r"[A-Z]", password):
        pool += 26

    if re.search(r"\d", password):
        pool += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)

    return round(entropy, 2)


def get_strength_level(score):
    """Convert score to human-readable strength level."""

    if score <= 2:
        return "Weak"

    elif score == 3:
        return "Moderate"

    elif score == 4:
        return "Strong"

    return "Very Strong"


def check_password_strength(password):
    strength = {
        "length": len(password) >= 12,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(strength.values())

    feedback = []

    if not strength["length"]:
        feedback.append("Password should be at least 12 characters long.")

    if not strength["uppercase"]:
        feedback.append("Add at least one uppercase letter.")

    if not strength["lowercase"]:
        feedback.append("Add at least one lowercase letter.")

    if not strength["numbers"]:
        feedback.append("Include at least one number.")

    if not strength["special"]:
        feedback.append("Use at least one special character.")

    entropy = round(len(password) * 4.7, 2)

    if score <= 2:
        level = "Weak"
    elif score == 3:
        level = "Moderate"
    elif score == 4:
        level = "Strong"
    else:
        level = "Very Strong"

    return score, level, entropy, feedback

    # Standard checks
    if not strength["length"]:
        feedback.append("Password should be at least 12 characters long.")

    if not strength["uppercase"]:
        feedback.append("Add at least one uppercase letter.")

    if not strength["lowercase"]:
        feedback.append("Add at least one lowercase letter.")

    if not strength["numbers"]:
        feedback.append("Include at least one number.")

    if not strength["special"]:
        feedback.append("Use at least one special character.")

    # Common password detection
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("Password appears in a list of commonly used passwords.")
        score = max(0, score - 2)

    # Sequential patterns
    sequential_patterns = [
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789",
        "abc",
        "bcd",
        "cde",
        "qwerty"
    ]

    if any(pattern in password.lower() for pattern in sequential_patterns):
        feedback.append("Sequential patterns detected.")
        score = max(0, score - 1)

    # Repeated characters
    if re.search(r"(.)\1{3,}", password):
        feedback.append("Repeated characters detected.")
        score = max(0, score - 1)

    entropy = calculate_entropy(password)
    level = get_strength_level(score)

    return score, level, entropy, feedback


def check_pwned_api(password):
    """Check if password exists in known data breaches using HIBP API."""

    sha1pwd = hashlib.sha1(
        password.encode("utf-8")
    ).hexdigest().upper()

    first5 = sha1pwd[:5]
    tail = sha1pwd[5:]

    url = f"https://api.pwnedpasswords.com/range/{first5}"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:
            return None, None

        hashes = (
            line.split(":")
            for line in response.text.splitlines()
        )

        for h, count in hashes:

            if h == tail:
                return True, int(count)

        return False, 0

    except requests.RequestException:
        return None, None