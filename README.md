## Simple python script
This is a very simple and “rough” Python script created for quick reachability tests using ICMP ping.

The program reads a list of hosts/IPs from an ip.txt file and pings them sequentially.

The script automatically detects the operating system using the platform library:

* Windows → uses -n as the ping count parameter
* Linux/macOS → uses -c

Console output is suppressed with:
```bash
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
```
Reachability results are printed in real time, indicating whether each host responded successfully to the ICMP request.