#!/usr/bin/env python
import socket
import curl
import urllib2
import sys
import os
import ftplib
from datetime import datetime


def write_banner():
    """Writes the banner to report file"""
    file = open("output.txt", "w+")

    file.write( "  _____ _                    _              __   ______                          \n")
    file.write( " / ____| |                  | |            / _| |  ____|                         \n")
    file.write( "| |    | |__  _   _ _ __ ___| |__     ___ | |_  | |__   _ __ ___   __ _  ___ ___ \n")
    file.write( "| |    | '_ \| | | | '__/ __| '_ \   / _ \|  _| |  __| | '_ ` _ \ / _` |/ __/ __|\n")
    file.write( "| |____| | | | |_| | | | (__| | | | | (_) | |   | |____| | | | | | (_| | (__\__ \ \n")
    file.write( " \_____|_| |_|\__,_|_|  \___|_| |_|  \___/|_|   |______|_| |_| |_|\__,_|\___|___/\n")
    file.write("\n")
    file.close()
    return 0
def banner():
    """Displays the banner"""
    print "  _____ _                    _              __   ______                          "
    print " / ____| |                  | |            / _| |  ____|                         "
    print "| |    | |__  _   _ _ __ ___| |__     ___ | |_  | |__   _ __ ___   __ _  ___ ___ "
    print "| |    | '_ \| | | | '__/ __| '_ \   / _ \|  _| |  __| | '_ ` _ \ / _` |/ __/ __|"
    print "| |____| | | | |_| | | | (__| | | | | (_) | |   | |____| | | | | | (_| | (__\__ \ "
    print " \_____|_| |_|\__,_|_|  \___|_| |_|  \___/|_|   |______|_| |_| |_|\__,_|\___|___/"
    print"\n"
    return 0
def url_format(target):
    """formats urls correctly"""
    if not target.startswith("http://"):
        target = "http://" + target
    if not target.endswith("/"):
        target = target + ("/")
    return target
def tcp_port_scan(port, target):
    """Returns a True value if the specified TCP port is open"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket using IVP4 addresses and TCP ports
    try:
        s.connect((target, port))
        return True
    except socket.error:
        return False
    s.close()
def check_ports_tcp(target):
    """Returns a list of open TCP ports on the target"""
    print "Would you like to scan: "
    print "A. first 100 ports"
    print "B. most common ports"
    print "C. all ports"
    print "Q. quit\n"
    port_scan_menu = raw_input(">>>")
    if port_scan_menu.lower() == "a":
        ports = range(1, 101) #ports 1 - 100

    elif port_scan_menu.lower() == "b":
        ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 29, 37, 42, 43, 49, 53,
                 69, 70, 79, 80, 103, 108, 109, 110, 115, 118, 119, 137, 139, 143,
                 150, 156, 161, 179, 190, 194, 197, 389, 396, 443, 444, 445, 458,
                 546, 547, 563, 569, 1080] #most common ports
    elif port_scan_menu.lower() == "c":
        ports = range(0, 65536) #every port
    elif port_scan_menu.lower() == "q":
        quit()
    else:
        print("invalid")

    open_ports = []
    print("Scanning...\n")
    s = datetime.now()
    for i in ports:
        if tcp_port_scan(i, target):
            open_ports.append(i)
        else:
            continue
    f = datetime.now()
    uinput = raw_input("Would you like to output results to a txt file? [Y/N]")
    if uinput.lower() == "y":
        if not os.path.isfile(os.getcwd()+"/output.txt"): #does this file already exist?
            write_banner()
        else:
            pass
        file = open("output.txt", "a")
        file.write("\n{} open TCP ports found on target: {}\n".format(len(open_ports), target))
        for x in open_ports:
            try:
                y = socket.getservbyport(x)
                file.write("{} : {}\t\n".format(x, y))
            except socket.error:
                y = "Unknown port service"
                file.write("{} : {}\t\n".format(x, y))
        file.close()
    else:
        pass
    return (open_ports, (f - s))
def udp_port_scan(port, target):
    """Returns a True value if the specified UDP port is open"""
    port = str(port)
    response = os.system("nc -vnzu "+target+" "+port+" > /dev/null 2>&1") #/dev/null 2>&1 suppresses any terminal output including errors
    if response == 0:
        return True
    elif response != 0:
        return False
def check_ports_udp(target):
    """Returns a list of open UDP ports on the target"""
    open_ports = []
    s = datetime.now()
    for i in range(0, 65536):
        if udp_port_scan(i, target):
            open_ports.append(i)
        else:
            continue
    f = datetime.now()
    uinput = raw_input("Would you like to output results to a txt file? [Y/N]")
    if uinput.lower() == "y":
        if not os.path.isfile(os.getcwd()+"/output.txt"):
            write_banner()
        else:
            pass
        file = open("output.txt", "a")
        file.write("\n{} open UDP ports found on target: {}\n".format(len(open_ports), target))
        for x in open_ports:
            try:
                y = socket.getservbyport(x, "UDP")
                file.write("{} : {}\t\n".format(x, y))
            except socket.error:
                y = "Unknown port service"
                file.write("{} : {}\t\n".format(x, y))
        file.close()
    else:
        pass
    return (open_ports, (f - s))
def directory(target):
    """Checks to see if a specified directory is present on the server"""
    try:
        c = curl.Curl()
        site = c.get(target)
        response_code = c.info()["http-code"]
        if response_code == 404:
            return False
        elif not response_code == 404:
            return True
    except Exception:
        return 0 #target unreachable
def dir_check(target):
    """Returns a list of present directories from the list below on the server"""

    directories=["admin", "administrator", "backup", "config",
          "cpanel", "data", "images", "panel", "proxy", "staff",
          "uploads", "upload", "user", "users", "webmaster"]
    target = url_format(target)
    true_dirs = []
    d = directory(target)
    if type(d) == int:
        return "Error connecting to target"

    for x in directories:
        if directory(target + x):
            true_dirs.append(target + x)
        else:
            pass
    uinput = raw_input("Would you like to output results to file? [Y/N]")
    if uinput.lower() == "y":
        if not os.path.isfile(os.getcwd()+"/output.txt"):
            write_banner()
        else:
            pass
        file = open("output.txt", "a")
        file.write("\n{} of the specified directories found on {}".format(len(true_dirs), target))
        for i in true_dirs:
            file.write("\nPresent : {}/".format(i))
        file.close()
    else:
        pass
    return true_dirs
def set_target():
    return raw_input("Set a target: \n").strip() #strip the white space and return user input
def find_SUID_SGID():

    print("Displaying files with SUID enabled\n")
    os.system("find /bin /sbin /usr/bin . -perm /4000")
    print("\nDisplaying files with GSID enabled\n")
    os.system("find /bin /sbin /usr/bin . -perm /2000")

    return 0
def FTP_anon(target):
    try:
        f = ftplib.FTP(target)
        f.login("anonymous", "anonymous")
        f.close()
        return True
    except Exception:
        return False
def listener():
    os.system("gnome-terminal -- nc -lnv 8765")
def menu(target):
    """Menu for selecting which feature to use in the program"""
    menu = ""
    while not menu.lower().startswith("q"):
        print "T. Set target"
        print "C. Create report file"
        print "\t1. TCP Port Scan"
        print "\t2. UDP Port Scan"
        print "\t3. Show files with SUID / SGID enabled"
        print "\t4. URL Directory Scanner"
        print "\t5. Check for Anonymous FTP"
        print "\t6. Listener on port 8765"
        print "Q. Quit \n"
        menu = raw_input(">>>")
        if menu == "1":
            res = check_ports_tcp(target)
            print "TCP Ports open on the target: {} \nTime elapsed: {}\n".format(res[0], res[1])
        elif menu == "4":
            x = dir_check(target)
            if type(x) == list:
                print "list of directories that exist: {} ".format(x)
            elif type(x) == str:
                print x
        elif menu == "3":
            find_SUID_SGID()
        elif menu == "2":
            print "UDP port scan may take some time"
            res = check_ports_udp(target)
            print "UDP Ports open on the target: {} \nTime elapsed: {}\n".format(res[0], res[1])
        elif menu == "5":
            if FTP_anon:
                print("Anonymous FTP login at {} was successful".format(target))
            else:
                print("Anonymous FTP login at {} was unsuccessful".format(target))
        elif menu == "6":
            listener()
        elif menu.lower() == "t":
            destination = set_target()
            print "Target currently set at {} \n".format(target)
        elif menu.lower() == "q":
            print("\n Exiting \n")
            quit()
        elif menu.lower() == "c":
            write_banner()
        else:
            print("\nNot a valid selection! \n")


try:
    if __name__ == "__main__":
        banner()
        destination = set_target()
        while destination is None:
            destination = set_target()
        print "Target currently set at {} \n".format(destination)
        menu(destination)
except KeyboardInterrupt:
    print("\nExiting the program")
    raise sys.exit()
#except Exception as e:
    #print("Unexpected error occurred: {}".format(e))

