import dns.resolver
import whois
import requests
import random
import string
import ssl
import socket
import os
from datetime import datetime


def banner():

    print("""
===================================
       MobileRecon-Termux
===================================
""")


def generate_password():

    length = int(input("\nPassword length: "))

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("\nGenerated Password:")
    print(password)


def dns_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] DNS Lookup for {domain}")

    try:

        ip = socket.gethostbyname(domain)

        print("IP Address:", ip)

    except:

        print("Unable to resolve domain")

def whois_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] WHOIS Information for {domain}")

    try:

        data = whois.whois(domain)

        print("\nRegistrar:")
        print(data.registrar)

        print("\nCreation Date:")
        print(data.creation_date)

        print("\nExpiration Date:")
        print(data.expiration_date)

    except Exception as e:

        print("WHOIS Error:", e)



def security_header():

    domain = input("\nEnter domain: ")

    print(f"\n[+] Security Headers for {domain}")

    try:

        response = requests.get(
            "https://" + domain,
            timeout=5
        )

        headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security",
            "X-Content-Type-Options"
        ]

        for header in headers:

            print(
                header,
                ":",
                response.headers.get(header)
            )

    except:

        print("Unable to check headers")



def ssl_check():

    domain = input("\nEnter domain: ")

    print(f"\n[+] SSL Certificate Information for {domain}")

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain,443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ) as ssock:

                cert = ssock.getpeercert()

                print("\nIssuer:")
                print(cert.get("issuer"))

                print("\nValid From:")
                print(cert.get("notBefore"))

                print("\nValid Until:")
                print(cert.get("notAfter"))

    except Exception as e:

        print("SSL Error:", e)



def ip_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] IP Information for {domain}")

    try:

        ip = socket.gethostbyname(domain)

        print("IP Address:", ip)

    except:

        print("Unable to resolve IP")

def dns_records():

    domain = input("\nEnter domain: ")

    print(f"\n[+] DNS Records for {domain}")

    resolver = dns.resolver.Resolver(configure=False)

    resolver.nameservers = [
        "8.8.8.8",
        "1.1.1.1"
    ]

    records = [
        "A",
        "MX",
        "NS",
        "TXT"
    ]

    for record in records:

        try:

            answers = resolver.resolve(domain, record)

            print(f"\n{record} Records:")

            for answer in answers:

                print(answer)

        except:

            print(f"\n{record} Records: Not Found")



def subdomain_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] Checking subdomains for {domain}")

    subdomains = [
        "www",
        "mail",
        "smtp",
        "ftp",
        "api",
        "blog",
        "ns1",
        "ns2"
    ]

    for sub in subdomains:

        full_domain = f"{sub}.{domain}"

        try:

            ip = socket.gethostbyname(full_domain)

            print(
                f"[FOUND] {full_domain} -> {ip}"
            )

        except:

            pass



def generate_report():

    target = input("\nEnter target domain: ")

    folder = "reports"

    if not os.path.exists(folder):

        os.makedirs(folder)


    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    filename = (
        f"{folder}/"
        f"{target}_{timestamp}_report.txt"
    )


    report = f"""
MobileRecon-Termux Security Report

Target:
{target}

Generated:
{timestamp}

"""


    try:

        ip = socket.gethostbyname(target)

        report += f"""
IP Information:
{ip}
"""

    except:

        report += """
IP Information:
Unable to resolve
"""


    try:

        cert = ssl.create_default_context()

        report += """
SSL:
Enabled
"""

    except:

        report += """
SSL:
Failed
"""


    try:

        data = whois.whois(target)

        report += f"""
WHOIS:

Registrar:
{data.registrar}

Expiration:
{data.expiration_date}

"""

    except:

        report += """
WHOIS:
Unavailable
"""


    with open(filename,"w") as file:

        file.write(report)


    print("\n[+] Report saved:")
    print(filename)



def menu():

    while True:

        banner()

        print("""
1. Generate Password
2. DNS Lookup
3. WHOIS Lookup
4. Security Header
5. SSL Certificate Check
6. IP Information Lookup
7. Generate Report
8. DNS Records
9. Subdomain Lookup
10. Exit
""")


        choice = input("Select option: ")


        if choice == "1":

            generate_password()

        elif choice == "2":

            dns_lookup()

        elif choice == "3":

            whois_lookup()

        elif choice == "4":

            security_header()

        elif choice == "5":

            ssl_check()

        elif choice == "6":

            ip_lookup()

        elif choice == "7":

            generate_report()

        elif choice == "8":

            dns_records()

        elif choice == "9":

            subdomain_lookup()

        elif choice == "10":

            print("Exit MobileRecon")

            break

        else:

            print("Invalid choice")



if __name__ == "__main__":

    menu()
