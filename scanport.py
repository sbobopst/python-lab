import threading
import socket


with open("ip.txt") as f:
    target = f.read().split('\n')

def portscan(port):
    for ip in target:
        if(ip!=""):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            try:    
                con = s.connect((ip,port))
                print('Port:',port,'from', ip, "is open.")
                con.close()
            except:         
                pass


def main():
    r = 1
    for x in range(1,101): 
        t = threading.Thread(target=portscan,kwargs={'port':r}) 
        r += 1     
        t.start() 

if __name__ == "__main__":
    main()