## Simple python script

The code is intentionally rough and not particularly well structured, as it was written mainly for learning and experimentation purposes to better understand the overall mechanisms and workflow behind this type of automation.

## ICMP Reachability Script

This is a very simple Python script created for quick reachability tests using ICMP ping.

The program reads a list of hosts/IPs from an `ip.txt` file and pings them sequentially.

The script automatically detects the operating system using the `platform` library:

* Windows → uses `-n` as the ping count parameter
* Linux/macOS → uses `-c`

Console output is suppressed with:
```python
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
```
Reachability results are printed in real time, indicating whether each host responded successfully to the ICMP request.

# Ansible Reachability Script

This script performs the same type of reachability validation, but through Ansible using the built-in `ping` module.
