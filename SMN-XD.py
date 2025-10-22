#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
import os
import subprocess

def main():
    bit = os.uname().machine
    changes = subprocess.getoutput("git status --porcelain")

    if changes:
        print("[*] Local changes detected, resetting repo...")
        os.system("git reset --hard")
        os.system("git clean -fd")
        os.system("git pull")

    os.system("chmod 755 *")  # safer than 777

    if '64' in bit:
        import loging
    elif '32' in bit:
        import login

if __name__ == "__main__":
    main()
