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
    print("=" * 40)
    print("       MobileRecon-Termux")
    print("=" * 40)


def generate_password():

    length = int(input("\nPassword length: "))

    characters = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n[+] Generated Password:")
    print(password)



def dns_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] DNS Lookup for {domain}")

    try:

        ip = socket.gethostbyname(domain)

        print("IP Address:", ip)

    except Exception as e:
        print("Error:", e)



def whois_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] WHOIS Lookup for {domain}")

    try:

        result = whois.whois(domain)

        print("Registrar:", result.registrar)
        print("Creation Date:", result.creation_date)
        print("Expiration Date:", result.expiration_date)
        print("Name Servers:", result.name_servers)

    except Exception as e:
        print("Error:", e)



def security_header():

    url = input("\nEnter website URL (https://example.com): ")

    try:

        response = requests.get(url)

        print("\n[+] Security Headers")

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

    except Exception as e:
        print("Error:", e)



def ssl_certificate_check():

    domain = input("\nEnter domain: ")

    print(f"\n[+] SSL Certificate Check for {domain}")

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (domain,443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=domain
            ):

                print("[+] SSL Certificate is valid")


    except Exception as e:

        print("SSL Error:", e)



def ip_lookup():

    domain = input("\nEnter domain: ")

    print(f"\n[+] IP Information for {domain}")

    try:

        ip = socket.gethostbyname(domain)

        print("IP Address:", ip)

        hostname = socket.gethostbyaddr(ip)

        print("Hostname:", hostname[0])


    except Exception as e:

        print("Error:", e)

def dns_records():

    domain = input("\nEnter domain: ")

    print(f"\n[+] DNS Records for {domain}")

    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ["8.8.8.8", "1.1.1.1"]

    records = ["A", "MX", "NS", "TXT"]

    for record in records:

        try:

            answers = resolver.resolve(domain, record)

            print(f"\n{record} Records:")

            for answer in answers:
                print(answer)

        except Exception as e:
            print(f"\n{record} Records: Not Found")

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


    print("\n[+] Collecting information...")


    # IP Information

    try:

        ip = socket.gethostbyname(target)

    except:

        ip = "Unable to resolve"



    # WHOIS

    try:

        whois_data = whois.whois(target)

        registrar = whois_data.registrar
        expiry = whois_data.expiration_date


    except:

        registrar = "Unavailable"
        expiry = "Unavailable"



    # SSL

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (target,443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=target
            ):

                ssl_status = "Valid SSL Certificate"


    except:

        ssl_status = "SSL Check Failed"



    # Security Headers

    try:

        response = requests.get(
            "https://" + target,
            timeout=5
        )


        headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security",
            "X-Content-Type-Options"
        ]


        security = ""


        for header in headers:

            security += (
                f"{header}: "
                f"{response.headers.get(header)}\n"
            )


    except:

        security = "Unable to check headers"

    # DNS Records

    try:

        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = ["8.8.8.8", "1.1.1.1"]

        dns_info = ""

        for record in ["A", "MX", "NS"]:

            try:

                answers = resolver.resolve(target, record)

                dns_info += f"\n{record} Records:\n"

                for answer in answers:
                    dns_info += f"{answer}\n"

            except:
                dns_info += f"\n{record} Records: Not Found\n"

    except:

        dns_info = "Unable to collect DNS records"

    report = f"""

========================================
       MobileRecon-Termux Report
========================================


Target:
{target}


IP Address:
{ip}


WHOIS Registrar:
{registrar}


WHOIS Expiry:
{expiry}


SSL Status:
{ssl_status}


DNS Records:
{dns_info}


Security Headers:
{security}


Report Generated:
{datetime.now()}


========================================

"""


    try:

        with open(filename,"w") as file:

            file.write(report)


        print("\n[+] Report saved:")
        print(filename)


    except Exception as e:

        print("Error:", e)



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
9. Exit
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
            ssl_certificate_check()

        elif choice == "6":
            ip_lookup()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            dns_records()

        elif choice == "9":
            print("Exit MobileRecon")
            break

        else:
            print("Invalid choice")

menu()
