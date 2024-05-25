import socket
import termcolor

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        banner = grab_banner(sock)
        if banner:
            print(termcolor.colored(f"[+] Port {port} is open: {banner.strip()}", 'green'))
        else:
            print(termcolor.colored(f"[+] Port {port} is open, but no banner retrieved", 'yellow'))
        sock.close()
    except:
        pass

def grab_banner(sock):
    try:
        return sock.recv(1024).decode().strip()
    except:
        return None

targets = input("[*] Enter Target To Scan (split them by , in order to scan more than 1 target): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
    for ip_address in targets.split(','):
        scan(ip_address.strip(), ports)
else:
    scan(targets, ports)