import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import ansibleip
with open("ip.txt") as f:
    val = f.read().split('\n')

def ping(host):
    
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Select parameter based on operating system
    param = '-n' if platform.system().lower()=='windows' else '-c'


    # Building the command. Ex: "ping -c 1 hostname"
    command = ['ping', param, '1', host]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def main():
    for i in val:
        if (i!="" and ping(i)):
            print("ICMP", i, "successful")
        elif (i!=""):
            print("ICMP", i, "not successful")
    ansibleip.ansibleping()
if __name__ == "__main__":
    main()
