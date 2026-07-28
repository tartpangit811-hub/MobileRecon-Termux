![MobileRecon-Termux Banner](01c89d9c-5bc8-4c69-8763-da63a88bc800.png)

# MobileRecon-Termux

## Overview

MobileRecon-Termux is an all-in-one information gathering and security reporting toolkit designed for Android Termux users.

This project provides useful security analysis tools for domain reconnaissance, DNS information gathering, WHOIS lookup, SSL certificate checking, security header analysis, and automated security report generation.

---

## Features

- DNS Lookup
- DNS Records Analysis (A, MX, NS, TXT)
- WHOIS Information Lookup
- IP Information Lookup
- SSL Certificate Check
- Security Header Analysis
- Subdomain Discovery
- Password Generator
- Security Report Generator
- Termux Friendly Interface

---

## Installation

```bash
pkg update -y
pkg upgrade -y

pkg install git python -y

git clone https://github.com/tartpangit811-hub/MobileRecon-Termux.git

cd MobileRecon-Termux

pip install -r requirements.txt
