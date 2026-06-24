from utils import check_password_strength, check_pwned_api
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main():
    print(f"\n{Fore.YELLOW}🔐 Password Strength & Breach Checker 🔐\n")
    password = input("Enter a password to check: ")

    # Check strength
    score, level, entropy, feedback = check_password_strength(password)
    print("\nAnalyzing password...\n")
    print("\n" + "=" * 45)
    print("PASSWORD SECURITY REPORT")
    print("=" * 45)

    print(f"Strength Score : {score}/5")
    print(f"Strength Level : {level}")
    print(f"Entropy Score  : {entropy} bits")

    if feedback:
        print(f"\n{Fore.YELLOW}Recommendations:")

    for tip in feedback:
        print(f"{Fore.RED}- {tip}")



    # Check breach
    breached, count = check_pwned_api(password)
    if breached:
        print(f"{Fore.RED}❌ This password has been found in {count} breaches! Change it immediately.")
    elif breached is False:
        print(f"{Fore.GREEN}✅ This password has not been found in known breaches.")
    else:
        print(f"{Fore.YELLOW}⚠ Could not check breach status. Please try again later.")

if __name__ == "__main__":
    main()
