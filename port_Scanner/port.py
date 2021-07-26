import socket
import termcolor
import subprocess

def scan(target,ports):
    print(termcolor.colored("\n" + ' Starting Scan For ' + str(target),'red'))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened: " + str(port),' Service: ' + socket.getservbyport(port))
        sock.close()
    except:
        pass
def manual_scan():
    print(termcolor.colored("[*] Enter Targets To Scan (split them by ,): ",'blue'))
    targets = input(termcolor.colored("-->",'blue'))
    ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

    if "," in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
        for ip_addr in targets.split((",")):
            scan(ip_addr.strip(''),ports)
    else:
        scan(targets,ports)

def automatic_scan():
    def IPAdd():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    ip = str(IPAdd())
    NetIP = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.'

    for ping in range(1, 254):
        address = NetIP + str(ping)
        res = subprocess.call(['ping', '-c', '1', '-W', '0.1', address], stdout=subprocess.DEVNULL)
        if res == 0:
            print(termcolor.colored(f"[*] Scanning Network: {NetIP + '0'}", 'green'))
            print(termcolor.colored(f"\n[*] Host Found! {address} - Online", 'green'))
            print(termcolor.colored("[*] Scanning host...",'green'))
            scan(address,ports= 1000)
        elif res == 2:
            pass
        else:
            print("ping to", address, "failed!")


if __name__ == "__main__":
    print('Would you like to perform manual or automatic scan?')
    print('1. Manual scan')
    print('2. Automatic scan')
    ans = input("-->")

    if ans == "1":
        manual_scan()
    elif ans == "2":
        subprocess.call('clear')
        automatic_scan()
    else:
        print('Incorrect answer')