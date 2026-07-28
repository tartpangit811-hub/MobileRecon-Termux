import os
import random
import string

def banner():
    print("=" * 40)
    print("      MobileRecon-Termux")
    print("=" * 40)

def dns_lookup():
    domain = input("Enter domain: ")
    print(f"\n[+] DNS Lookup for {domain}")
    print("Feature under development.\n")

def whois_lookup():
    domain = input("Enter domain: ")
    print(f"\n[+] WHOIS Lookup for {domain}")
    print("Feature under development.\n")

def ssl_checker():
    domain = input("Enter domain: ")
    print(f"\n[+] SSL Check for {domain}")
    print("Feature under development.\n")

def security_headers():
    domain = input("Enter domain: ")
    print(f"\n[+] Security Headers for {domain}")
    print("Feature under development.\n")

def generate_password():
    length = 16
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))

    print("\nGenerated Password:")
    print(password)
    print()

while True:
    os.system("clear")
    banner()

    print("1. DNS Lookup")
    print("2. WHOIS Lookup")
    print("3. SSL Checker")
    print("4. Security Headers")
    print("5. Generate Password")
    print("6. Exit")

    choice = input("\nSelect Option: ")

    if choice == "1":
        dns_lookup()
    elif choice == "2":
        whois_lookup()
    elif choice == "3":
        ssl_checker()
    elif choice == "4":
        security_headers()
    elif choice == "5":
        generate_password()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

    input("Press Enter to continue...")
