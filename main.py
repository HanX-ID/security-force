import re
import string
from termcolor import colored

def load_common_passwords(filepath):
    try:
        with open(filepath, 'r') as file:
            return set(p.strip() for p in file.readlines())
    except FileNotFoundError:
        print(colored("[!] File tidak ditemukan: " + filepath, "red"))
        return set()

def check_email(email):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(pattern, email))

def check_password_strength(password, common_passwords):
    score = 0
    reasons = []

    if password.lower() in common_passwords:
        reasons.append("Password ini sangat umum & lemah")
        return 10, reasons

    if len(password) >= 8:
        score += 20
    else:
        reasons.append("Terlalu pendek")

    if any(c.islower() for c in password): score += 10
    else: reasons.append("Tidak ada huruf kecil")

    if any(c.isupper() for c in password): score += 10
    else: reasons.append("Tidak ada huruf besar")

    if any(c.isdigit() for c in password): score += 10
    else: reasons.append("Tidak ada angka")

    if any(c in string.punctuation for c in password): score += 10
    else: reasons.append("Tidak ada simbol")

    if len(set(password)) < len(password) // 2:
        reasons.append("Karakter terlalu berulang")

    if len(password) >= 12: score += 20
    if len(password) >= 16: score += 20

    return min(score, 100), reasons

def print_banner():
    banner = """\n
   _____                      _ __           ______
  / ___/___  _______  _______(_) /___  __   / ____/___  _____________
  \\__ \\/ _ \\/ ___/ / / / ___/ / __/ / / /  / /_  / __ \\/ ___/ ___/ _ \\
 ___/ /  __/ /__/ /_/ / /  / / /_/ /_/ /  / __/ / /_/ / /  / /__/  __/
/____/\\___/\\___/\\__,_/_/  /_/\\__/\\__, /  /_/    \\____/_/   \\___/\\___/
                                /____/
    """
    print(colored(banner, 'red'))

def main():
    common_passwords = load_common_passwords("password_umum.txt")
    print_banner()
    email = input(colored("Masukkan email: ", "blue"))
    password = input(colored("Masukkan password: ", "blue"))

    email_valid = check_email(email)
    email_score = 100 if email_valid else 0
    email_status = "Valid" if email_valid else "Tidak valid"

    strength, reasons = check_password_strength(password, common_passwords)
    total = (strength + email_score) // 2

    print(colored(f"\n[ Email    ] {email_status}", "blue"))
    print(colored(f"[ Password ] {strength}%", "green"))
    if reasons:
        for r in reasons:
            print(colored(f" - {r}", "yellow"))
    print(colored(f"\n[ Total Kekuatan ] {total}%", "green"))

if __name__ == "__main__":
    main()