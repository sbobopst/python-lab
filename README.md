## Simple python script

The code is intentionally rough and not particularly well structured, as these scripts were written mainly for learning and experimentation purposes to better understand the overall mechanisms and workflows behind this type of automation.

## ICMP Reachability Script 
**File:** [`main.py`](./main.py)

This is a very simple Python script created for quick reachability tests using ICMP ping.

The program reads a list of hosts/IPs from an [ip.txt](./ip.txt) file and pings them sequentially.

The script automatically detects the operating system using the `platform` library:

* Windows → uses `-n` as the ping count parameter
* Linux/macOS → uses `-c`

Console output is suppressed with:
```python
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
```
Reachability results are printed in real time, indicating whether each host responded successfully to the ICMP request.

# Ansible Reachability Script
**Files:**
- [`ansibleip.py`](./ansibleip.py)
- [`main.py`](./main.py)

These scripts perform the same type of reachability validation, but through Ansible using the built-in `ping` module.

# Port scanner 
**Files:**
- [`scanport.py`](./scanport.py)
 
This script performs multi-threaded port scanning using Python sockets to identify open ports on target hosts. Targets are loaded from an [](./ip.txt) file, allowing automated scanning first 100 ports of multiple IP addresses.

# Log parser
**Files:**
- [`logparser.py`](./logparser.py)
- [`auth.log`](./auth.log)

This script parses a local authentication log file (auth.log) and extracts only failed login attempts together with the source IP addresses.
 
