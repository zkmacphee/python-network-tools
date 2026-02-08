# Python Network Health Check Tool

## Overview
This is a cross-platform network diagnostic tool developed using Python. It utilizes raw sockets and system subprocesses to identify connectivity issues at Layer 3 (ICMP).

## Key Features
* **OS Agnostic:** Automatically detects Windows vs. Linux to adjust ICMP packet flags (`-n` vs `-c`).
* **Source Identification:** Uses `socket` library to identify the specific Network Interface Card (NIC) being used for egress traffic.
* **Logic Logic:** Differentiates between "Target Down" (Remote Host Unreachable) and "Internet Down" (WAN Failure).

## Technologies Used
* Python 3.x
* Libraries: `subprocess`, `platform`, `socket`

## How to Run
```bash
python3 NetworkHealthCheck.py
